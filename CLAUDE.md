# Blog Migration Tool

## Overview

This blog project contains a Python-based migration tool in the `scripts/` directory for migrating content from an old blog to the current blog system.

## Scripts Directory
- **Location**: `/scripts/`
- **Package Manager**: UV (modern Python package manager)
- **Python Version**: >=3.13
- **Current Status**: Basic project structure with placeholder main.py

## Project Structure
```
scripts/
├── pyproject.toml    # UV project configuration
├── main.py          # Entry point (currently placeholder)
├── README.md        # Empty documentation file
└── uv.lock         # Dependency lock file
```

## Commands
- **Run migration tool**: `cd scripts && uv run main.py`
- **Install dependencies**: `cd scripts && uv sync`
- **Add dependencies**: `cd scripts && uv add <package>`

## Development Notes
- The migration tool is currently in initial setup phase
- Main entry point is `scripts/main.py`
- No external dependencies configured yet
- Ready for migration logic implementation
- **Old blog location**: `../old-blog/` (Hugo-based blog with podcast episodes)
- **Current blog content**: `content/` directory (Quartz-based blog system)

## Blog Structure Analysis

### Old Blog (Hugo-based)
- **Structure**: Hugo static site generator with content organized in directories
- **Podcast episodes**: Located in `content/podcast/` with numbered directories (0001, 0002, etc.)
- **Episode format**: Each episode has its own directory containing `index.md` and `cover.jpg`
- **Frontmatter**: YAML format with fields: `title`, `date`, `type`, `tag`, `withpost`, `description`, `link`
- **Content**: Description text follows the frontmatter delimiter (`---`)
- **Tags**: Multi-line YAML list format (e.g., `- "Cryptography"`, `- "ZK"`)
- **Links**: External links to Substack episodes
- **Total episodes**: 24 episodes (as of migration)

### Current Blog (Quartz-based)
- **Structure**: Quartz static site generator with markdown files in `content/` directory
- **Organization**: Flat structure with categorized subdirectories (Notes/, Posts/, Refs/, etc.)
- **Format**: Standard markdown files with frontmatter
- **lists**: `content/Podcast.md`, `content/Projects.md`, `content/Papers.md` (single consolidated files)
- **Migration format (lists only)**: Markdown list with `- [title](url) [[YYYY-MM-DD]]` (for some categories, just the year) and `- description` sub-items

## Development Principles
- **Silent on success**: Scripts should be silent in the happy path and only output messages on errors or warnings
