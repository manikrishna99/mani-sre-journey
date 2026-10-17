def get_cpu_status(cpu_usage):
  if cpu_usage >80:
    return "CRITICAL"
  elif cpu_usage >= 70:
    return "WARNING"
  else:
    return "NORMAL"

cpu_usage =50
status = get_cpu_status(cpu_usage)

print("CPU Usage:", cpu_usage, "%")
print("Status:",status)
