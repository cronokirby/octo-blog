import argparse
import re
from pathlib import Path
from typing import Dict, List, Optional


def parse_frontmatter(content: str) -> tuple[Dict[str, str], str]:
    """Parse YAML frontmatter from markdown content."""
    lines = content.split('\n')
    
    if not lines or lines[0].strip() != '---':
        return {}, content
    
    frontmatter = {}
    body_start = 1
    
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '---':
            body_start = i + 1
            break
        
        # Simple YAML parsing for our use case
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"')
            
            # Handle tags (list format)
            if key == 'tag' and not value:
                # Multi-line tag list
                tag_lines = []
                for j in range(i + 1, len(lines)):
                    if lines[j].strip() == '---':
                        break
                    if lines[j].strip().startswith('- '):
                        tag_lines.append(lines[j].strip()[2:].strip('"'))
                    elif lines[j].strip() and not lines[j].strip().startswith(' '):
                        break
                frontmatter[key] = tag_lines
            else:
                frontmatter[key] = value
    
    body = '\n'.join(lines[body_start:]).strip()
    return frontmatter, body


def migrate_podcast_episodes(old_blog_dir: Path, output_dir: Path) -> int:
    """Migrate podcast episodes from old blog to new format."""
    podcast_dir = old_blog_dir / "content" / "podcast"
    
    if not podcast_dir.exists():
        print(f"Error: Podcast directory '{podcast_dir}' does not exist")
        return 1
    
    episodes = []
    
    # Find all episode directories (numbered folders)
    for episode_dir in sorted(podcast_dir.iterdir()):
        if not episode_dir.is_dir():
            continue
            
        # Check if directory name is numeric (episode number)
        if not re.match(r'^\d+$', episode_dir.name):
            continue
            
        index_file = episode_dir / "index.md"
        if not index_file.exists():
            print(f"Warning: No index.md found in {episode_dir}")
            continue
        
        try:
            content = index_file.read_text(encoding='utf-8')
            frontmatter, body = parse_frontmatter(content)
            
            episode = {
                'number': int(episode_dir.name),
                'title': frontmatter.get('title', 'Untitled'),
                'date': frontmatter.get('date', ''),
                'tags': frontmatter.get('tag', []),
                'link': frontmatter.get('link', ''),
                'description': body.strip()
            }
            
            episodes.append(episode)
            
        except Exception as e:
            print(f"Error processing {episode_dir}: {e}")
            continue
    
    if not episodes:
        print("No podcast episodes found to migrate")
        return 0
    
    # Generate markdown list
    markdown_lines = ["# Podcast Episodes", ""]
    
    for episode in episodes:
        # Main list item with title, link, and date in brackets
        main_item = f"- [{episode['title']}]({episode['link']})"
        if episode['date']:
            main_item += f" [[{episode['date']}]]"
        markdown_lines.append(main_item)
        
        # Add description as sub-item if available
        if episode['description']:
            markdown_lines.append(f"  - {episode['description']}")
        
        markdown_lines.append("")  # Empty line between episodes
    
    # Write to output file
    output_file = output_dir / "Podcast.md"
    output_file.write_text('\n'.join(markdown_lines), encoding='utf-8')
    
    print(f"Migrated {len(episodes)} podcast episodes to {output_file}")
    return 0


def main(input_dir: Path, output_dir: Path):
    # Validate directories
    if not input_dir.exists():
        print(f"Error: Input directory '{input_dir}' does not exist")
        return 1
    
    if not input_dir.is_dir():
        print(f"Error: '{input_dir}' is not a directory")
        return 1
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Migrate podcast episodes
    return migrate_podcast_episodes(input_dir, output_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Blog migration tool")
    parser.add_argument("input_dir", type=Path, help="Input directory containing old blog content")
    parser.add_argument("output_dir", type=Path, help="Output directory for migrated content")
    
    args = parser.parse_args()
    
    exit(main(args.input_dir, args.output_dir))
