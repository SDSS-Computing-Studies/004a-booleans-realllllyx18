#! python3

 #  Have the user enter a username 
 # If the username is not "admin" then tell them it is an "invalid user", 
 # but if it is, then ask them for a password 
 # If they get the password correct (password is 12345password) 
 # then display the message "Access granted"
 # 1 marks

username=input("Enter the username")

if username!="admin":
    print("invalid user")
else:
    password=input("Enter the password")
    if password=="12345password":
        print("Access granted")
