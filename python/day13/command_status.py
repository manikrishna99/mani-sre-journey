import subprocess

try:
    result = subprocess.run(["ls", "/folder_that_does_not_exist"])
    print("Exit code:", result.returncode)

    if result.returncode == 0:
        print("Status: SUCCESS")
    else:
        print("Status: FAILED")

except FileNotFoundError:
    print("Status: FAILED")
    print("Reason: Command not found")
