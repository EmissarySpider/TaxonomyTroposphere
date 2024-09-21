#!/bin/bash

# Directory to search in
SEARCH_DIR="/Path/to/folder"

# Find all .py files and search their contents for "user-agent" (case-insensitive)
find "$SEARCH_DIR" -type f -name "*.py" -exec grep -i "user-agent" {} +

