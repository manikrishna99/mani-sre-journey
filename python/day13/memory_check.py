import subprocess


def get_memory_status(usage):
    if usage >= 90:
        return "CRITICAL"
    elif usage >= 80:
        return "WARNING"
    else:
        return "NORMAL"


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

usage = ((total - available) / total) * 100
status = get_memory_status(usage)

print(f"Memory usage: {usage:.1f}%")
print(f"Memory status: {status}")


print("\nTesting memory thresholds:")

for usage in [50, 85, 95]:
    print(usage, "% ->", get_memory_status(usage))
