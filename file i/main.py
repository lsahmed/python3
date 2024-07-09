usern = input("Enter a username: ").strip()  # Strip whitespace from input username
name = input("Enter a name: ")
passwd = input("Enter a password: ")
with open("users.txt", "r") as f:
   toFind = [line.strip() for line in f.readlines()]

if usern in toFind:
  print("Username already registered")
else:
  with open("users.txt", "a") as f:
    f.write(f"{usern} : {name} : {passwd}\n")
    print("User registered successfully")
