#!/usr/bin/env python3
"""
Script to fix alias paths in markdown files by making them absolute (adding leading slash).
"""

import os
import re
from pathlib import Path

def fix_aliases_in_file(file_path):
    """Fix aliases in a single markdown file by making them absolute paths."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match aliases in frontmatter
    # This matches both single aliases and list items
    def fix_alias_line(match):
        line = match.group(0)
        # If the alias doesn't start with / or http, make it absolute
        if not line.strip().endswith('":') and not '/' in line[:line.find('"')]:
            # Find the quoted alias path
            alias_match = re.search(r'"([^"]+)"', line)
            if alias_match:
                alias_path = alias_match.group(1)
                # Only fix if it doesn't already start with / or http
                if not alias_path.startswith('/') and not alias_path.startswith('http'):
                    new_line = line.replace(f'"{alias_path}"', f'"/{alias_path}"')
                    return new_line
        return line
    
    # Find and fix aliases in frontmatter
    # This pattern matches lines like:   - "posts/2023/03/filename"
    alias_pattern = r'^(\s*-\s*"[^"]*")$'
    
    # Also match single alias lines like: aliases: "posts/2023/03/filename"
    single_alias_pattern = r'^(aliases:\s*"[^"]*")$'
    
    lines = content.split('\n')
    modified = False
    
    for i, line in enumerate(lines):
        # Check for list-style aliases
        if re.match(alias_pattern, line):
            alias_match = re.search(r'"([^"]+)"', line)
            if alias_match:
                alias_path = alias_match.group(1)
                if not alias_path.startswith('/') and not alias_path.startswith('http'):
                    lines[i] = line.replace(f'"{alias_path}"', f'"/{alias_path}"')
                    modified = True
        
        # Check for single alias
        elif re.match(single_alias_pattern, line):
            alias_match = re.search(r'"([^"]+)"', line)
            if alias_match:
                alias_path = alias_match.group(1)
                if not alias_path.startswith('/') and not alias_path.startswith('http'):
                    lines[i] = line.replace(f'"{alias_path}"', f'"/{alias_path}"')
                    modified = True
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        return True
    return False

def main():
    """Main function to process all markdown files."""
    content_dir = Path('content')
    if not content_dir.exists():
        print("Error: content directory not found")
        return
    
    modified_files = []
    
    # Process all .md files in content directory
    for md_file in content_dir.rglob('*.md'):
        if fix_aliases_in_file(md_file):
            modified_files.append(md_file)
            print(f"Fixed aliases in: {md_file}")
    
    if modified_files:
        print(f"\nModified {len(modified_files)} files:")
        for file in modified_files:
            print(f"  - {file}")
    else:
        print("No files needed modification")

if __name__ == '__main__':
    main()