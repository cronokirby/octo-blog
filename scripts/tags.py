#!/usr/bin/env python3

import argparse
import re
import yaml
from pathlib import Path
from typing import Dict, List, Any


def parse_frontmatter(content: str) -> tuple[Dict[str, Any], str]:
    """Parse YAML frontmatter from markdown content."""
    lines = content.split('\n')
    
    if not lines or lines[0].strip() != '---':
        return {}, content
    
    # Find the end of frontmatter
    end_index = None
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '---':
            end_index = i + 1
            break
    
    if end_index is None:
        return {}, content
    
    # Extract frontmatter and body
    frontmatter_text = '\n'.join(lines[1:end_index-1])
    body = '\n'.join(lines[end_index:])
    
    try:
        frontmatter = yaml.safe_load(frontmatter_text) or {}
    except yaml.YAMLError:
        # Fallback to simple parsing if YAML fails
        frontmatter = {}
        for line in lines[1:end_index-1]:
            if ':' in line:
                key, value = line.split(':', 1)
                frontmatter[key.strip()] = value.strip().strip('"')
    
    return frontmatter, body


def serialize_frontmatter(frontmatter: Dict[str, Any]) -> str:
    """Serialize frontmatter to YAML format."""
    if not frontmatter:
        return ""
    
    lines = ['---']
    for key, value in frontmatter.items():
        if isinstance(value, list):
            lines.append(f'{key}:')
            for item in value:
                if isinstance(item, str):
                    lines.append(f'  - {item}')
                else:
                    lines.append(f'  - {item}')
        else:
            if isinstance(value, str) and any(char in value for char in [':', '"', "'"]):
                lines.append(f'{key}: "{value}"')
            else:
                lines.append(f'{key}: {value}')
    lines.append('---')
    return '\n'.join(lines)


def lowercase_tags_in_frontmatter(frontmatter: Dict[str, Any]) -> bool:
    """Lowercase all tags in frontmatter. Returns True if any changes were made."""
    changed = False
    
    # Check for 'tags' field
    if 'tags' in frontmatter:
        tags = frontmatter['tags']
        if isinstance(tags, list):
            new_tags = []
            for tag in tags:
                if isinstance(tag, str):
                    lowered = tag.lower()
                    new_tags.append(lowered)
                    if lowered != tag:
                        changed = True
                else:
                    new_tags.append(tag)
            frontmatter['tags'] = new_tags
        elif isinstance(tags, str):
            lowered = tags.lower()
            if lowered != tags:
                changed = True
            frontmatter['tags'] = lowered
    
    # Check for other tag-like fields (tag, note-tags, etc.)
    for field_name in list(frontmatter.keys()):
        if 'tag' in field_name.lower() and field_name != 'tags':
            tags = frontmatter[field_name]
            if isinstance(tags, list):
                new_tags = []
                for tag in tags:
                    if isinstance(tag, str):
                        lowered = tag.lower()
                        new_tags.append(lowered)
                        if lowered != tag:
                            changed = True
                    else:
                        new_tags.append(tag)
                frontmatter[field_name] = new_tags
            elif isinstance(tags, str):
                lowered = tags.lower()
                if lowered != tags:
                    changed = True
                frontmatter[field_name] = lowered
    
    return changed


def process_markdown_file(file_path: Path) -> bool:
    """Process a single markdown file, lowercasing all tags. Returns True if file was modified."""
    try:
        content = file_path.read_text(encoding='utf-8')
        frontmatter, body = parse_frontmatter(content)
        
        if not frontmatter:
            return False
        
        changed = lowercase_tags_in_frontmatter(frontmatter)
        
        if changed:
            new_content = serialize_frontmatter(frontmatter) + '\n' + body
            file_path.write_text(new_content, encoding='utf-8')
            return True
        
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def find_markdown_files(root_path: Path) -> List[Path]:
    """Find all markdown files in the given directory tree."""
    return list(root_path.rglob('*.md'))


def main():
    parser = argparse.ArgumentParser(
        description="Lowercase all tags in markdown files within a blog directory tree"
    )
    parser.add_argument(
        'blog_root', 
        type=Path, 
        help="Root directory of the blog to process"
    )
    parser.add_argument(
        '--dry-run', 
        action='store_true', 
        help="Show what would be changed without modifying files"
    )
    
    args = parser.parse_args()
    
    if not args.blog_root.exists():
        print(f"Error: Directory '{args.blog_root}' does not exist")
        return 1
    
    if not args.blog_root.is_dir():
        print(f"Error: '{args.blog_root}' is not a directory")
        return 1
    
    markdown_files = find_markdown_files(args.blog_root)
    
    if not markdown_files:
        print("No markdown files found")
        return 0
    
    modified_count = 0
    
    for file_path in markdown_files:
        if args.dry_run:
            # For dry run, just check if file would be modified
            try:
                content = file_path.read_text(encoding='utf-8')
                frontmatter, _ = parse_frontmatter(content)
                
                if frontmatter:
                    # Create a copy to test changes
                    test_frontmatter = frontmatter.copy()
                    changed = lowercase_tags_in_frontmatter(test_frontmatter)
                    if changed:
                        print(f"Would modify: {file_path}")
                        modified_count += 1
            except Exception as e:
                print(f"Error checking {file_path}: {e}")
        else:
            if process_markdown_file(file_path):
                modified_count += 1
    
    if args.dry_run:
        print(f"Would modify {modified_count} files out of {len(markdown_files)} markdown files")
    else:
        if modified_count > 0:
            print(f"Modified {modified_count} files out of {len(markdown_files)} markdown files")
    
    return 0


if __name__ == "__main__":
    exit(main())