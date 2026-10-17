
import subprocess


# Disk usage thresholds
def get_disk_status(usage):
    if usage >= 90:
        return "CRITICAL"
    elif usage >= 80:
        return "WARNING"
    else:
        return "NORMAL"


# Memory usage thresholds
def get_memory_status(usage):
    if usage >= 90:
        return "CRITICAL"
    elif usage >= 80:
        return "WARNING"
    else:
        return "NORMAL"


# Check system uptime
def check_uptime():
    try:
        result = subprocess.run(
            ["uptime"],
            capture_output=True,
            text=True,
            check=True
        )

        print("\n--- UPTIME CHECK ---")
        print("Status: SUCCESS")
        print(result.stdout.strip())

    except (FileNotFoundError, subprocess.CalledProcessError):
        print("UPTIME CHECK: FAILED")


# Check disk usage
def check_disk():
    try:
        result = subprocess.run(
            ["df", "-P", "/"],
            capture_output=True,
            text=True,
            check=True
        )

        lines = result.stdout.splitlines()
        disk_values = lines[1].split()
        usage = int(disk_values[4].replace("%", ""))

        status = get_disk_status(usage)

        print("\n--- DISK CHECK ---")
        print("Command Status: SUCCESS")
        print(f"Disk Usage: {usage}%")
        print(f"Disk Status: {status}")

        if status == "WARNING":
            print("WARNING: Disk usage is high!")
        elif status == "CRITICAL":
            print("CRITICAL: Disk usage is very high!")

    except (FileNotFoundError, subprocess.CalledProcessError,
            IndexError, ValueError):
        print("DISK CHECK: FAILED")


# Check memory usage
def check_memory():
    try:
        result = subprocess.run(
            ["free", "-b"],
            capture_output=True,
            text=True,
            check=True
        )

        lines = result.stdout.splitlines()
        memory_values = lines[1].split()

        total = int(memory_values[1])
        available = int(memory_values[6])

        if total <= 0:
            raise ValueError("Invalid total memory")

        usage = ((total - available) / total) * 100
        status = get_memory_status(usage)

        print("\n--- MEMORY CHECK ---")
        print("Command Status: SUCCESS")
        print(f"Memory Usage: {usage:.1f}%")
        print(f"Memory Status: {status}")

        if status == "WARNING":
            print("WARNING: Memory usage is high!")
        elif status == "CRITICAL":
            print("CRITICAL: Memory usage is very high!")

    except (FileNotFoundError, subprocess.CalledProcessError,
            IndexError, ValueError):
        print("MEMORY CHECK: FAILED")


# Run all health checks
def main():
    print("===== SYSTEM HEALTH CHECKER =====")

    check_uptime()
    check_disk()
    check_memory()
    test_thresholds()

    print("\n===== HEALTH CHECK COMPLETE =====")

def test_thresholds():
    print("\n===== THRESHOLD TESTS =====")

    test_values = [50, 80, 95]

    for usage in test_values:
        print(f"Disk {usage}% -> {get_disk_status(usage)}")
        print(f"Memory {usage}% -> {get_memory_status(usage)}")


if __name__ == "__main__":
    main()
