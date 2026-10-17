counts={
  "INFO" : 0, "ERROR" :0, "WARNING" :0
}

try:
  with open("app.log","r") as file:
   for line in file:
    for level in counts:
     if level in line:
      counts[level] +=1
  print("Log Analysis Summary")

  print("--------------------")

  for level, count in counts.items():
   print(f"{level}: {count}")

  if counts["ERROR"] > 0:
     print("ALERT: Errors found in application logs")
  else:
     print("Status: No errors found")

except FileNotFoundError:
  print("ERROR: Log file not found")
