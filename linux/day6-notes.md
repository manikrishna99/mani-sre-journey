# Day 6 — Linux Troubleshooting & Incident Response

## 1. Troubleshooting workflow

1. Identify the symptom.
2. Check system resources.
3. Check relevant services and processes.
4. Inspect application logs.
5. Form a hypothesis.
6. Gather more evidence.
7. Apply a fix only when justified.
8. Verify recovery.

## 2. Commands practiced

- `hostname` — identify the system hostname.
- `df -h` — inspect filesystem usage.
- `free -h` — inspect memory and swap.
- `systemctl is-active cron` — check cron service state.
- `tail -n 10 FILE` — display the last 10 lines.
- `grep -n "ERROR" FILE` — find errors with line numbers.
- `grep ... | sort | uniq -c | sort -nr` — count and rank repeated log messages.
- `sed -n '1,8p' FILE` — display selected lines.
- `systemctl list-units --type=service --all` — inspect loaded service units.
- `sudo ss -lntp` — inspect listening TCP ports and processes.
- `grep -RniE` — search files recursively.
- `find` — locate files.
- `ls -lh` — inspect file sizes.

## 3. Incident findings

- Root filesystem usage: 1%.
- Available memory: approximately 3.2 GiB.
- Cron: active.
- Main application log: 9 ERROR entries.
- Database connection failures: 4.
- Timeout errors: 2.
- Connection-refused errors: 2.
- Payment-service-unavailable errors: 1.
- No local TCP listener found on ports 3306 or 5432.
- `config.txt`, `logs/app.log`, and `logs/error.log` are empty.

## 4. Diagnosis

The main application log contains errors, especially database connection failures. Disk pressure and memory pressure are not indicated by the collected output.

The database connection issue is a hypothesis, not a confirmed root cause. The training environment lacks sufficient configuration and application evidence to determine the exact cause.

## 5. Important lessons

- An active service does not guarantee application health.
- Empty command output must be investigated rather than interpreted automatically.
- The most frequent error is not necessarily the root cause.
- Correlation does not prove causation.
- Never change a system before collecting enough evidence.
- Verify the result after applying a fix.



# Day 7 — Linux Revision and Troubleshooting

## System snapshot commands

- `hostname` — identifies the system.
- `uptime` — displays uptime and load averages.
- `df -h /` — checks root filesystem usage.
- `free -h` — checks memory and swap.
- `ps aux` — lists running processes.
- `pgrep -af NAME` — searches full command lines for matching processes.

## Service and log commands

- `systemctl status SERVICE --no-pager` — checks service state.
- `journalctl -u SERVICE -n 10 --no-pager` — displays recent service logs.
- `systemctl cat SERVICE` — displays service configuration.
- `crontab -l` — lists the current user's scheduled jobs.

## Troubleshooting principle

When a service reports "Connection refused":

1. Identify the destination host and port.
2. Check whether the destination service is listening.
3. Check whether the destination address and port are correct.
4. Investigate network access and service configuration as appropriate.
5. Verify the result after any justified fix.

Do not assume that a running application process means the application is healthy. Do not restart services or change configurations without evidence.

## Day 7 conclusion

Practiced Linux system snapshots, process inspection, service checks, log investigation, and evidence-based troubleshooting.
