try:
  with open("missing.log","r") as file:
   print(file.read())
except FileNotFoundError:
  print("ERROR: Log file not found")
