# MonitorBrightness

A Python CLI tool to control monitor brightness on Ubuntu.

## Installation

```bash
pipx install .
```

Or for development:

```bash
pip install -e .
```

## Usage

```bash
# Set brightness (0–100)
mbright set-brightness 75

# Set brightness on a specific monitor
mbright set-brightness 75 --display "Monitor Name"

# Show current brightness
mbright stats

# Show brightness for a specific monitor
mbright stats --display "Monitor Name"
```

## Requirements

- Python >= 3.12
- Ubuntu (uses `screen-brightness-control`)
