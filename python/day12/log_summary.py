counts = {
  "INFO" :0,
  "ERROR" :0,
  "WARNING" :0
}

with open("app.log","r") as file:
 for line in file:
  for level in counts:
   if level in line:
    counts[level] +=1
print(counts)
