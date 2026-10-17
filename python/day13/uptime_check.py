import subprocess

result = subprocess.run( ["uptime"],capture_output=True,text=True)

print("System uptime:")
print(result.stdout)
