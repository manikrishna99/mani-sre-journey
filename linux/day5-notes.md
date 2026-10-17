# Day 5 — Bash Automation & System Health Checks

## 1. Learning objectives

- Automate repetitive Linux tasks.
- Process multiple log files.
- Use loops, functions, variables, and conditions.
- Collect system information.
- Check disk usage and application errors.
- Build a system health-check script.

## 2. For loop

Purpose: Process multiple items or files.

```bash
for file in ../*.log
do
    echo "$file"
done
```

- `for`: starts the loop.
- `in`: specifies the items.
- `do`: starts the loop body.
- `done`: ends the loop.
- `*.log`: matches filenames ending in `.log`.

## 3. Conditions inside loops

```bash
if [ "$ERRORS" -gt 0 ]; then
    echo "UNHEALTHY"
else
    echo "HEALTHY"
fi
```

This checks each file and reports its status based on the number of errors.

## 4. Functions

Purpose: Reuse commands without repeating the same code.

```bash
check_log() {
    LOGFILE="$1"
    ERRORS=$(grep -c "ERROR" "$LOGFILE")
    echo "$LOGFILE has $ERRORS errors"
}
```

Call the function:

```bash
check_log "../app.log"
```

## 5. While loop

Purpose: Repeat commands while a condition is true.

```bash
count=1

while [ "$count" -le 5 ]
do
    echo "$count"
    count=$((count + 1))
done
```

- `-le`: less than or equal to.
- `$((...))`: arithmetic expansion.
- Always ensure the loop can eventually stop.

## 6. Service checks

```bash
systemctl is-active --quiet cron
```

Check the result:

```bash
echo $?
```

- `0`: success.
- Non-zero: failure.

## 7. System information commands

| Command | Purpose |
|---|---|
| `hostname` | Display machine name |
| `whoami` | Display current user |
| `uptime` | Show uptime and load averages |
| `df -h` | Display filesystem usage |
| `free -h` | Display memory and swap usage |

## 8. Disk monitoring

```bash
df -P /
```

Extract the usage percentage:

```bash
df -P / | awk 'NR==2 {gsub(/%/, "", $5); print $5}'
```

- `awk`: processes text and fields.
- `NR==2`: selects the second line.
- `$5`: selects the fifth field.
- `gsub`: removes the percentage symbol.

Disk threshold example:

```bash
if [ "$DISK_USAGE" -ge 80 ]; then
    echo "WARNING"
fi
```

## 9. Final project: system_health.sh

The script collects:

- Hostname
- Current user
- Uptime
- Root disk usage
- Available memory
- Application log errors
- Overall health status

It sets a status variable to indicate whether a problem was found and exits with that status.

## 10. Key lessons

- Use functions to organize reusable logic.
- Use loops to process multiple items.
- Validate files before reading them.
- Quote variables, such as `"$LOGFILE"`.
- Check exit codes.
- Collect all results before deciding the overall status.
- Test scripts with both healthy and unhealthy inputs.

## Day 5 status

Completed: Bash loops, functions, system information, disk checks, log scanning, and the system health-check project.
