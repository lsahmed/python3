usern = input("Enter a username: ")
name = input("Enter a name: ")
passwd = input("Enter a password: ")

with open("users.txt") as f:
    re = f.read()
    if(usern in re):
        print("User already registered ")
    else:
        with open("users.txt", "a") as f:
            f.write(f"\n {name} = {usern}:{passwd}")
            
