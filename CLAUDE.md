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

## Development Principles
- **Silent on success**: Scripts should be silent in the happy path and only output messages on errors or warnings