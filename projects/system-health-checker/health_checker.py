import subprocess

from thresholds import get_disk_status, get_memory_status


def check_uptime():
    result = subprocess.run(
        ["uptime"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def check_disk():
    result = subprocess.run(
        ["df", "-P", "/"],
        capture_output=True,
        text=True,
        check=True,
    )
    lines = result.stdout.splitlines()
    usage = int(lines[1].split()[4].replace("%", ""))
    return usage, get_disk_status(usage)


def check_memory():
    result = subprocess.run(
        ["free", "-b"],
        capture_output=True,
        text=True,
        check=True,
    )
    values = result.stdout.splitlines()[1].split()
    total = int(values[1])
    available = int(values[6])

    if total <= 0:
        raise ValueError("Total memory must be greater than zero")

    usage = round(((total - available) / total) * 100, 1)
    return usage, get_memory_status(usage)


def main():
    print("===== SYSTEM HEALTH CHECKER =====")

    checks = [
        ("UPTIME", check_uptime),
        ("DISK", check_disk),
        ("MEMORY", check_memory),
    ]

    for name, check in checks:
        print(f"\n--- {name} CHECK ---")
        try:
            result = check()
            print("Status: SUCCESS")

            if name == "UPTIME":
                print(result)
            else:
                usage, status = result
                print(f"Usage: {usage}%")
                print(f"Health: {status}")

        except (
            FileNotFoundError,
            subprocess.CalledProcessError,
            IndexError,
            ValueError,
        ) as error:
            print("Status: FAILED")
            print(f"Reason: {error}")

    print("\n===== HEALTH CHECK COMPLETE =====")


if __name__ == "__main__":
    main()
