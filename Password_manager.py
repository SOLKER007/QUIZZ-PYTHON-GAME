pwd = input("What is the master password: ")

mode = input(
    "Would you like to 'add' a new password or 'view' existing ones? ").lower()
if mode == "add":
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(website + " | " + username + " | " + password + "\n")
    print("Password added!")
elif mode == "view":
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, username, password = data.split(" | ")
            print("Website:", user)
            print("Username:", username)
            print("Password:", password)
            print()
else:
    print("Invalid mode.")

if pwd != "solker123":
    print("Incorrect password! Access denied.")
    quit()
