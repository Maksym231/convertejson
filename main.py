import json

def function():
    a = open("data.txt", "r")
    b = json.load(a)

    first_name = sorted([value for i in b for keys, value in i.items() if keys == 'first_name'])
    last_name = sorted([value for i in b for keys, value in i.items() if keys == 'last_name'])
    email = sorted([value for i in b for keys, value in i.items() if keys == 'email'])
    gender = sorted([value for i in b for keys, value in i.items() if keys == 'gender'])
    ip_address = sorted([value for i in b for keys, value in i.items() if keys == 'ip_address'])

    first_name_file = open('first_name.txt', 'w')
    first_name_file.write(str(first_name))
    first_name_file.close()

    last_name_file = open('last_name.txt', 'w')
    last_name_file.write(str(last_name))
    last_name_file.close()

    email_file = open('email.txt', 'w')
    email_file.write(str(email))
    email_file.close()

    gender_file = open('gender.txt', 'w')
    gender_file.write(str(gender))
    gender_file.close()

    ip_address_file = open('ip_address.txt', 'w')
    ip_address_file.write(str(ip_address))
    ip_address_file.close()
    

function()




   


    