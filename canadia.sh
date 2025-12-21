#!/bin/bash
# Canadia CLI wrapper script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python3 "$SCRIPT_DIR/canadia_cli.py" "$@"
