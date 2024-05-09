import json

def registration():
    name = input("Enter name : ")
    email = input("Enter email : ")

    with open("main.json","r") as file:
        data = json.load(file)

    for i in data:
        if i["email"] == email:
            return "Email already in use"
    
    password = input("Enter Password : ")
    re_type_password = input("Enter the password again : ")

    if password == re_type_password:
        with open("main.json","r") as file:
            data = json.load(file)

        d = {
            "name" : name,
            "email" : email,
            "password" : password
        }

        data.append(d)

        with open("main.json","w") as file:
            json.dump(data,file,indent=4)
        return "Successfully registered"
    else:
        return "Password did not match"

def Login():
    email = input("Enter email : ")
    password = input("Enter password : ")

    with open("main.json","r") as file:
        data = json.load(file)

    for i in data:
        if i["email"] == email and i["password"] == password:
            with open("main.json","w") as file:
                json.dump(data,file,indent=4)
            print("Hello ",i["name"])
            break
    else:
        return "Login Failed"
    
    return "Login Successful"

def name_update():

    with open("main.json","r") as file:
        data = json.load(file)

    email = input("Enter email : ")

    for i in data:
        if i["email"] == email:
            new_name = input("Enter new name : ")
            i["name"] = new_name
            break
    else:
        return "email not found in the database"

    with open("main.json","w") as file:
        json.dump(data,file,indent=4)

    return "Name updated successfully"

while True:
    print("0.Exit")
    print("1.Registration")
    print("2.Update Name")
    print("3.Login")

    choice = int(input("Enter the choice : "))
    if choice not in [0,1,2,3]:
        print("Choice should in [0,1,2,3]")
        continue
    
    if choice == 0:
        break
    elif choice == 1:
        print(registration())
        continue
    elif choice == 3:
        print(Login())
        continue
    else:
        print(name_update())
        continue
    
