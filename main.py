import json

def Registration():
    name = input("Enter the name : ")
    email = input("Enter Email : ")
    password = input("Enter the password : ")
    re_enter = input("Re-enter the password : ")

    if len(password) < 8:
        return "Length of the password should be more than 8"

    if password != re_enter:
        return "Password does not match"
    
    if "@" not in email or "." not in email:
        return "Please enter a valid email"

    with open("main.json",'r') as read_file:
        data = json.load(read_file)

    new_data = {
        "user_name" : name,
        "user_email" : email,
        "user_password" : password
    }

    data.append(new_data)

    with open("main.json",'w') as file:
        json.dump(data,file,indent=4)

def Login():
    pass

def Profile():
    pass

def MyPosts():
    pass

def PasswordError():
    pass

def EmailError():
    pass

def Post():
    pass

def UpdatePassword():
    pass

def UpdateEmail():
    pass

def PostsCount():
    pass

def ForgotPassword():
    pass

def EmailMessage():
    pass

if __name__ == "__main__":
    print(Registration())


