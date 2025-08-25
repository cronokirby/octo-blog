import argparse
import re
import yaml
import hashlib
import shutil
from pathlib import Path
from typing import Dict, List, Optional


def parse_frontmatter(content: str) -> tuple[Dict, str]:
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
    body = '\n'.join(lines[end_index:]).strip()
    
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


def sanitize_filename(title: str) -> str:
    """Convert title to a safe filename."""
    # Remove/replace problematic characters
    sanitized = re.sub(r'[^\w\s-]', '', title)
    sanitized = re.sub(r'[-\s]+', '-', sanitized)
    return sanitized.strip('-')


def detect_shortcodes(content: str) -> List[str]:
    """Detect Hugo shortcodes in content."""
    shortcode_pattern = r'{{<\s*(\w+)[^>]*>}}'
    return list(set(re.findall(shortcode_pattern, content)))


def create_alias_path(date: str, title: str, content_type: str) -> str:
    """Create the old URL path for aliases."""
    try:
        from datetime import datetime
        
        # If date is already a datetime object (from YAML parsing), use it directly
        if hasattr(date, 'year'):
            date_obj = date
        else:
            # Handle different date string formats
            date_str = str(date)
            # Replace space with T for ISO format compatibility
            date_str = date_str.replace(' ', 'T')
            # Handle Z timezone
            date_str = date_str.replace('Z', '+00:00')
            date_obj = datetime.fromisoformat(date_str)
        
        year = date_obj.year
        month = f"{date_obj.month:02d}"
        sanitized_title = sanitize_filename(title).lower()
        return f"{content_type}/{year}/{month}/{sanitized_title}"
    except Exception as e:
        # Even on error, try to extract year/month from date string
        year = "unknown"
        month = "unknown"
        if date:
            try:
                # Convert to string and try to parse just the date part (YYYY-MM-DD)
                date_str = str(date)
                date_part = date_str.split('T')[0] if 'T' in date_str else date_str.split(' ')[0]
                if len(date_part) >= 10 and date_part[4] == '-' and date_part[7] == '-':
                    year = date_part[:4]
                    month = date_part[5:7]
            except:
                pass
        
        print(f"Warning: Could not parse date '{date}' for {title}, using {year}/{month}")
        sanitized_title = sanitize_filename(title).lower()
        return f"{content_type}/{year}/{month}/{sanitized_title}"


def copy_image_with_hash(source_path: Path, images_dir: Path) -> str:
    """Copy image to images directory with SHA256-based filename."""
    if not source_path.exists():
        print(f"Warning: Image file {source_path} not found")
        return f"../Images/missing-{source_path.name}"
    
    # Read file and compute SHA256 hash
    content = source_path.read_bytes()
    hash_hex = hashlib.sha256(content).hexdigest()
    
    # Keep original extension
    extension = source_path.suffix.lower()
    if not extension:
        # Try to detect from content if no extension
        if content.startswith(b'\xff\xd8\xff'):
            extension = '.jpg'
        elif content.startswith(b'\x89PNG'):
            extension = '.png'
        else:
            extension = '.bin'
    
    # Create destination path
    dest_filename = f"{hash_hex}{extension}"
    dest_path = images_dir / dest_filename
    
    # Copy file if it doesn't already exist
    if not dest_path.exists():
        images_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, dest_path)
    
    return f"../Images/{dest_filename}"


def process_img_shortcodes(content: str, source_dir: Path, images_dir: Path) -> str:
    """Replace {{<img "filename">}} shortcodes with markdown image links."""
    def replace_img(match):
        filename = match.group(1).strip('"\'')
        
        # Look for the image file in the source directory
        source_path = source_dir / filename
        
        # Also check in a 'res' subdirectory (common pattern)
        if not source_path.exists():
            res_path = source_dir / "res" / filename
            if res_path.exists():
                source_path = res_path
        
        # Copy image and get the new path
        image_path = copy_image_with_hash(source_path, images_dir)
        
        # Return markdown image syntax
        return f"![]({image_path})"
    
    # Pattern to match {{<img "filename">}} with optional parameters
    pattern = r'{{<\s*img\s+"([^"]+)"[^>]*>}}'
    return re.sub(pattern, replace_img, content)


def process_ref_shortcodes(content: str) -> str:
    """Replace {{<ref>}} shortcodes with footnotes."""
    references = []
    
    def replace_ref(match):
        full_match = match.group(0)
        
        # Extract parameters from the shortcode
        # Handle both single-line and multi-line formats
        params = []
        
        # Try to extract quoted parameters
        param_pattern = r'"([^"]*)"'
        param_matches = re.findall(param_pattern, full_match)
        
        if len(param_matches) >= 3:
            ref_id = param_matches[0]
            url = param_matches[1] 
            text = param_matches[2]
            
            # Store reference for footnotes
            references.append(f"[^{ref_id}]: [{text}]({url})")
            
            # Return footnote reference
            return f"[^{ref_id}]"
        else:
            # Fallback: keep original if we can't parse
            return full_match
    
    # Pattern to match ref shortcodes (handles multi-line)
    ref_pattern = r'{{<\s*ref\s+[^>]*>}}'
    content = re.sub(ref_pattern, replace_ref, content, flags=re.DOTALL)
    
    # Add footnote definitions at the end if we found any
    if references:
        content += "\n\n" + "\n".join(references)
    
    return content


def process_note_shortcodes(content: str) -> str:
    """Replace {{<note>}}...{{</note>}} with Quartz callouts."""
    def replace_note(match):
        note_content = match.group(1).strip()
        return f"> [!note] **Note:**\n> {note_content.replace(chr(10), chr(10) + '> ')}"
    
    # Pattern to match note shortcodes with content
    note_pattern = r'{{<\s*note\s*>}}\s*(.*?)\s*{{<\s*/note\s*>}}'
    return re.sub(note_pattern, replace_note, content, flags=re.DOTALL)


def process_ref_link_shortcodes(content: str) -> str:
    """Replace {{<ref-link "X">}} shortcodes with footnote references."""
    def replace_ref_link(match):
        ref_id = match.group(1)
        return f"[^{ref_id}]"
    
    # Pattern to match ref-link shortcodes
    ref_link_pattern = r'{{<\s*ref-link\s+"([^"]+)"\s*>}}'
    return re.sub(ref_link_pattern, replace_ref_link, content)


def process_box_shortcodes(content: str) -> str:
    """Replace {{<box>}}...{{</box>}} with plain callouts."""
    def replace_box(match):
        box_content = match.group(1).strip()
        
        # Replace divider shortcodes with horizontal rules within the box
        box_content = re.sub(r'{{<\s*divider\s*>}}', '---', box_content)
        
        # Convert to callout format (prefix each line with > )
        lines = box_content.split('\n')
        callout_lines = []
        for line in lines:
            if line.strip() == '---':
                callout_lines.append('>\n> ---\n>')
            elif line.strip():
                callout_lines.append('> ' + line)
            else:
                callout_lines.append('>')
        
        return '\n'.join(callout_lines)
    
    # Pattern to match box shortcodes with content
    box_pattern = r'{{<\s*box\s*>}}\s*(.*?)\s*{{<\s*/box\s*>}}'
    return re.sub(box_pattern, replace_box, content, flags=re.DOTALL)


def process_todo_shortcodes(content: str) -> str:
    """Replace {{<todo>}}...{{</todo>}} with warning callouts."""
    def replace_todo(match):
        todo_content = match.group(1).strip()
        return f"> [!warning] **TODO:**\n> {todo_content.replace(chr(10), chr(10) + '> ')}"
    
    # Pattern to match todo shortcodes with content
    todo_pattern = r'{{<\s*todo\s*>}}\s*(.*?)\s*{{<\s*/todo\s*>}}'
    return re.sub(todo_pattern, replace_todo, content, flags=re.DOTALL)


def process_raw_shortcodes(content: str) -> str:
    """Replace {{<raw>}}...{{</raw>}} by keeping inner content."""
    def replace_raw(match):
        raw_content = match.group(1).strip()
        return raw_content
    
    # Pattern to match raw shortcodes with content
    raw_pattern = r'{{<\s*raw\s*>}}\s*(.*?)\s*{{<\s*/raw\s*>}}'
    return re.sub(raw_pattern, replace_raw, content, flags=re.DOTALL)


def fix_escaped_math_backslashes(content: str) -> str:
    """Fix double backslashes that were escaped for markdown parsing in math contexts."""
    
    def fix_math_block(match):
        """Fix backslashes within a math block."""
        math_content = match.group(1)
        # Replace \\ with \ in mathematical contexts
        # Common escaped characters in math
        fixes = [
            (r'\\{', r'\{'),
            (r'\\}', r'\}'),
            (r'\\_', r'\_'),
            (r'\\|', r'\|'),
            (r'\\&', r'\&'),
            (r'\\$', r'\$'),
            (r'\\#', r'\#'),
            (r'\\%', r'\%'),
            (r'\\^', r'\^'),
            (r'\\~', r'\~'),
        ]
        
        for escaped, unescaped in fixes:
            math_content = math_content.replace(escaped, unescaped)
        
        return f"$${math_content}$$"
    
    def fix_inline_math(match):
        """Fix backslashes within inline math."""
        math_content = match.group(1)
        # Apply same fixes as block math
        fixes = [
            (r'\\{', r'\{'),
            (r'\\}', r'\}'),
            (r'\\_', r'\_'),
            (r'\\|', r'\|'),
            (r'\\&', r'\&'),
            (r'\\$', r'\$'),
            (r'\\#', r'\#'),
            (r'\\%', r'\%'),
            (r'\\^', r'\^'),
            (r'\\~', r'\~'),
        ]
        
        for escaped, unescaped in fixes:
            math_content = math_content.replace(escaped, unescaped)
        
        return f"${math_content}$"
    
    # Fix in display math blocks ($$...$$)
    content = re.sub(r'\$\$(.+?)\$\$', fix_math_block, content, flags=re.DOTALL)
    
    # Fix in inline math ($...$) - be careful not to match $$ blocks
    content = re.sub(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', fix_inline_math, content, flags=re.DOTALL)
    
    return content


def process_shortcodes(content: str, source_dir: Path, images_dir: Path) -> str:
    """Process all known shortcodes in content."""
    # Handle img shortcodes
    content = process_img_shortcodes(content, source_dir, images_dir)
    
    # Handle ref shortcodes  
    content = process_ref_shortcodes(content)
    
    # Handle ref-link shortcodes
    content = process_ref_link_shortcodes(content)
    
    # Handle note shortcodes
    content = process_note_shortcodes(content)
    
    # Handle todo shortcodes
    content = process_todo_shortcodes(content)
    
    # Handle raw shortcodes
    content = process_raw_shortcodes(content)
    
    # Handle box shortcodes (must be after divider processing)
    content = process_box_shortcodes(content)
    
    # Fix escaped backslashes in math
    content = fix_escaped_math_backslashes(content)
    
    return content


def migrate_papers(old_blog_dir: Path, output_dir: Path) -> int:
    """Migrate papers from old blog to new format."""
    papers_dir = old_blog_dir / "content" / "papers"
    
    if not papers_dir.exists():
        print(f"Error: Papers directory '{papers_dir}' does not exist")
        return 1
    
    papers = []
    
    # Find all paper directories (year/paper-name structure)
    for year_dir in papers_dir.iterdir():
        if not year_dir.is_dir():
            continue
            
        for paper_dir in year_dir.iterdir():
            if not paper_dir.is_dir():
                continue
                
            index_file = paper_dir / "index.md"
            if not index_file.exists():
                print(f"Warning: No index.md found in {paper_dir}")
                continue
            
            try:
                content = index_file.read_text(encoding='utf-8')
                frontmatter, body = parse_frontmatter(content)
                
                paper = {
                    'title': frontmatter.get('title', 'Untitled'),
                    'date': frontmatter.get('date', ''),
                    'authors': frontmatter.get('author', []),
                    'link': frontmatter.get('link', ''),
                    'description': body.strip()
                }
                
                papers.append(paper)
                
            except Exception as e:
                print(f"Error processing {paper_dir}: {e}")
                continue
    
    if not papers:
        print("No papers found to migrate")
        return 0
    
    # Sort by date (newest first)
    papers.sort(key=lambda x: x['date'], reverse=True)
    
    # Generate markdown list
    markdown_lines = ["# Papers", ""]
    
    for paper in papers:
        # Main list item with title, link, and date in brackets
        main_item = f"- [{paper['title']}]({paper['link']})"
        if paper['date']:
            main_item += f" [[{paper['date']}]]"
        markdown_lines.append(main_item)
        
        # Add description as sub-item if available
        if paper['description']:
            markdown_lines.append(f"  - {paper['description']}")
        
        markdown_lines.append("")  # Empty line between papers
    
    # Write to output file
    output_file = output_dir / "Papers.md"
    output_file.write_text('\n'.join(markdown_lines), encoding='utf-8')
    
    print(f"Migrated {len(papers)} papers to {output_file}")
    return 0


def migrate_projects(old_blog_dir: Path, output_dir: Path) -> int:
    """Migrate projects from old blog to new format."""
    projects_dir = old_blog_dir / "content" / "projects"
    
    if not projects_dir.exists():
        print(f"Error: Projects directory '{projects_dir}' does not exist")
        return 1
    
    projects = []
    
    # Find all project directories (year/project-name structure)
    for year_dir in projects_dir.iterdir():
        if not year_dir.is_dir():
            continue
            
        for project_dir in year_dir.iterdir():
            if not project_dir.is_dir():
                continue
                
            index_file = project_dir / "index.md"
            if not index_file.exists():
                print(f"Warning: No index.md found in {project_dir}")
                continue
            
            try:
                content = index_file.read_text(encoding='utf-8')
                frontmatter, body = parse_frontmatter(content)
                
                project = {
                    'title': frontmatter.get('title', 'Untitled'),
                    'date': frontmatter.get('date', ''),
                    'tech': frontmatter.get('tech', []),
                    'link': frontmatter.get('link', ''),
                    'description': body.strip()
                }
                
                projects.append(project)
                
            except Exception as e:
                print(f"Error processing {project_dir}: {e}")
                continue
    
    if not projects:
        print("No projects found to migrate")
        return 0
    
    # Sort by date (newest first)
    projects.sort(key=lambda x: x['date'], reverse=True)
    
    # Generate markdown list
    markdown_lines = ["# Projects", ""]
    
    for project in projects:
        # Main list item with title, link, and year only (extract from date)
        main_item = f"- [{project['title']}]({project['link']})"
        if project['date']:
            year = project['date'][:4]  # Extract year from YYYY-MM-DD
            main_item += f" [[{year}]]"
        markdown_lines.append(main_item)
        
        # Add description as sub-item if available
        if project['description']:
            markdown_lines.append(f"  - {project['description']}")
        
        markdown_lines.append("")  # Empty line between projects
    
    # Write to output file
    output_file = output_dir / "Projects.md"
    output_file.write_text('\n'.join(markdown_lines), encoding='utf-8')
    
    print(f"Migrated {len(projects)} projects to {output_file}")
    return 0


def migrate_posts(old_blog_dir: Path, output_dir: Path) -> int:
    """Migrate blog posts from old blog to new format."""
    posts_dir = old_blog_dir / "content" / "posts"
    
    if not posts_dir.exists():
        print(f"Error: Posts directory '{posts_dir}' does not exist")
        return 1
    
    output_posts_dir = output_dir / "Posts"
    output_posts_dir.mkdir(exist_ok=True)
    
    images_dir = output_dir / "Images"
    
    posts_count = 0
    unknown_shortcodes = set()
    
    # Walk through all year/month directories
    for year_dir in sorted(posts_dir.iterdir()):
        if not year_dir.is_dir():
            continue
            
        for month_dir in sorted(year_dir.iterdir()):
            if not month_dir.is_dir():
                continue
                
            for post_dir in sorted(month_dir.iterdir()):
                if not post_dir.is_dir():
                    continue
                    
                index_file = post_dir / "index.md"
                if not index_file.exists():
                    # Check for .md files directly in the directory
                    md_files = list(post_dir.glob("*.md"))
                    if md_files:
                        index_file = md_files[0]
                    else:
                        print(f"Warning: No markdown file found in {post_dir}")
                        continue
                
                try:
                    content = index_file.read_text(encoding='utf-8')
                    frontmatter, body = parse_frontmatter(content)
                    
                    title = frontmatter.get('title', 'Untitled')
                    date = frontmatter.get('date', '')
                    
                    # Process shortcodes in the body
                    processed_body = process_shortcodes(body, post_dir, images_dir)
                    
                    # Check for remaining unknown shortcodes
                    remaining_shortcodes = detect_shortcodes(processed_body)
                    if remaining_shortcodes:
                        unknown_shortcodes.update(remaining_shortcodes)
                        print(f"UNKNOWN SHORTCODES in {post_dir.name}: {', '.join(remaining_shortcodes)}")
                        print("Please tell me how to handle these shortcodes before continuing.")
                        return 1
                    
                    # Create output filename
                    safe_title = sanitize_filename(title)
                    output_file = output_posts_dir / f"{safe_title}.md"
                    
                    # Create alias for old URL structure
                    alias_path = create_alias_path(date, title, "posts")
                    
                    # Build new frontmatter
                    new_frontmatter = {
                        'title': title,
                        'date': date,
                        'aliases': [alias_path]
                    }
                    
                    # Copy over relevant fields
                    for field in ['tags', 'draft', 'katex']:
                        if field in frontmatter:
                            new_frontmatter[field] = frontmatter[field]
                    
                    # Write new markdown file
                    lines = ['---']
                    for key, value in new_frontmatter.items():
                        if isinstance(value, list):
                            lines.append(f'{key}:')
                            for item in value:
                                lines.append(f'  - "{item}"')
                        else:
                            lines.append(f'{key}: "{value}"')
                    lines.append('---')
                    lines.append('')
                    lines.append(processed_body)
                    
                    output_file.write_text('\n'.join(lines), encoding='utf-8')
                    posts_count += 1
                    
                except Exception as e:
                    print(f"Error processing {post_dir}: {e}")
                    continue
    
    print(f"Migrated {posts_count} posts to {output_posts_dir}")
    return 0


def migrate_notes(old_blog_dir: Path, output_dir: Path) -> int:
    """Migrate notes from old blog to new format."""
    notes_dir = old_blog_dir / "content" / "notes"
    
    if not notes_dir.exists():
        print(f"Error: Notes directory '{notes_dir}' does not exist")
        return 1
    
    output_notes_dir = output_dir / "Notes"
    output_notes_dir.mkdir(exist_ok=True)
    
    images_dir = output_dir / "Images"
    
    notes_count = 0
    unknown_shortcodes = set()
    
    # Walk through all year/month directories
    for year_dir in sorted(notes_dir.iterdir()):
        if not year_dir.is_dir():
            continue
            
        for month_dir in sorted(year_dir.iterdir()):
            if not month_dir.is_dir():
                continue
                
            for note_item in sorted(month_dir.iterdir()):
                # Notes can be either directories with index.md or direct .md files
                if note_item.is_dir():
                    index_file = note_item / "index.md"
                    if not index_file.exists():
                        print(f"Warning: No index.md found in {note_item}")
                        continue
                    note_name = note_item.name
                    source_dir = note_item
                elif note_item.suffix == '.md':
                    index_file = note_item
                    note_name = note_item.stem
                    source_dir = note_item.parent
                else:
                    continue
                
                try:
                    content = index_file.read_text(encoding='utf-8')
                    frontmatter, body = parse_frontmatter(content)
                    
                    title = frontmatter.get('title', note_name.replace('-', ' ').title())
                    date = frontmatter.get('date', '')
                    
                    # Process shortcodes in the body
                    processed_body = process_shortcodes(body, source_dir, images_dir)
                    
                    # Check for remaining unknown shortcodes
                    remaining_shortcodes = detect_shortcodes(processed_body)
                    if remaining_shortcodes:
                        unknown_shortcodes.update(remaining_shortcodes)
                        print(f"UNKNOWN SHORTCODES in {note_name}: {', '.join(remaining_shortcodes)}")
                        print("Please tell me how to handle these shortcodes before continuing.")
                        return 1
                    
                    # Create output filename
                    safe_title = sanitize_filename(title)
                    output_file = output_notes_dir / f"{safe_title}.md"
                    
                    # Create alias for old URL structure
                    alias_path = create_alias_path(date, note_name, "notes")
                    
                    # Build new frontmatter
                    new_frontmatter = {
                        'title': title,
                        'date': date,
                        'aliases': [alias_path]
                    }
                    
                    # Copy over relevant fields
                    for field in ['tags', 'note-tags', 'draft', 'katex', 'type']:
                        if field in frontmatter:
                            new_frontmatter[field] = frontmatter[field]
                    
                    # Write new markdown file
                    lines = ['---']
                    for key, value in new_frontmatter.items():
                        if isinstance(value, list):
                            lines.append(f'{key}:')
                            for item in value:
                                lines.append(f'  - "{item}"')
                        else:
                            lines.append(f'{key}: "{value}"')
                    lines.append('---')
                    lines.append('')
                    lines.append(processed_body)
                    
                    output_file.write_text('\n'.join(lines), encoding='utf-8')
                    notes_count += 1
                    
                except Exception as e:
                    print(f"Error processing {note_item}: {e}")
                    continue
    
    print(f"Migrated {notes_count} notes to {output_notes_dir}")
    return 0


def migrate_podcast_episodes(old_blog_dir: Path, output_dir: Path) -> int:
    """Migrate podcast episodes from old blog to new format."""
    podcast_dir = old_blog_dir / "content" / "podcast"
    
    if not podcast_dir.exists():
        print(f"Error: Podcast directory '{podcast_dir}' does not exist")
        return 1
    
    episodes = []
    
    # Find all episode directories (numbered folders)
    for episode_dir in sorted(podcast_dir.iterdir(), reverse=True):
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
    
    # Migrate all content types
    exit_code = 0
    
    # Migrate posts
    if migrate_posts(input_dir, output_dir) != 0:
        exit_code = 1
    
    # Migrate notes
    if migrate_notes(input_dir, output_dir) != 0:
        exit_code = 1
    
    # # Migrate papers
    # if migrate_papers(input_dir, output_dir) != 0:
    #     exit_code = 1
    
    # # Migrate projects  
    # if migrate_projects(input_dir, output_dir) != 0:
    #     exit_code = 1
    
    # # Migrate podcast episodes
    # if migrate_podcast_episodes(input_dir, output_dir) != 0:
    #     exit_code = 1
    
    return exit_code


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Blog migration tool")
    parser.add_argument("input_dir", type=Path, help="Input directory containing old blog content")
    parser.add_argument("output_dir", type=Path, help="Output directory for migrated content")
    
    args = parser.parse_args()
    
    exit(main(args.input_dir, args.output_dir))
