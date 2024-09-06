username = input("Enter your username: ")
password = input("Enter your password: ")
print()
if username == "admin" and password == "admin":
  print("Welcome admin")
elif username == "user" and password == "user":
  print("Welcome user")
elif username == "guest" and password == "guest":
  print("Welcome guest")
else:
  print("Wrong username or password")