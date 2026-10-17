# System Health Checker

A Python project for practicing system health monitoring and automated threshold testing.

## Current Features

- Disk usage status thresholds
- Memory usage status thresholds
- Three health states: NORMAL, WARNING, and CRITICAL
- Automated unit tests using Python's built-in `unittest` framework
- Boundary tests around warning and critical thresholds

## Thresholds

| Usage | Status |
|---|---|
| Below 80% | NORMAL |
| 80% to below 90% | WARNING |
| 90% and above | CRITICAL |

## Project Structure

```text
system-health-checker/
├── tests/
│   └── test_thresholds.py
├── __init__.py
├── thresholds.py
└── README.md
```

## Requirements

- Python 3.10 or newer
- No third-party packages required for the current threshold tests

## Run the Tests

From this project directory, run:

```bash
PYTHONPATH=. python3 -m unittest discover -s tests -v
```

## Current Limitations

This project currently contains reusable threshold logic and automated tests. Live disk, memory, and uptime checks remain in the Day 13 learning script and have not yet been integrated into this standalone project.

## Planned Improvements

- Integrate live disk, memory, and uptime checks
- Improve command failure reporting
- Add tests for error handling
- Document sample output and usage
