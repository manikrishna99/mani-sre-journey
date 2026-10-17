server_name = "web-server-01"
cpu_usage = 65
is_healthy = True

print(server_name)
print(cpu_usage)
print(is_healthy)

print(type(server_name))
print(type(cpu_usage))
print(type(is_healthy))

cpu_before = 45
cpu_after = 90

print("CPU increase:" ,cpu_after-cpu_before)

if cpu_after >80:
   print("CRITICAL: High CPU")

elif cpu_after > 70:
   print("WARNING: High CPU usage")
else:
   print("CPU usage is normal")


services = ["nginx", "docker", "cron"]

print("Services:",services)
print("First service:",services[0])
print("Total services:",len(services))

for service in services:
   print("Checking service:",service)


for service in services:
   if service == "nginx":
     print(service,"- Check Required")
   else:
     print(service,"- Ok")

def check_cpu(cpu_usage):
   if cpu_usage >80:
     print("CRITICAL: High Cpu")
   else:
     print("CPU usage is normal")


check_cpu(90)
check_cpu(65)

def get_cpu_status(cpu_usage):
   if cpu_usage >80:
     return "CRITICAL"
   else:
     return "NORMAL"

status =get_cpu_status(90)
print("CPU status:",status)
