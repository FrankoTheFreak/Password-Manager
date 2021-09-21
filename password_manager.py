'''---------------------------------------Start of code---------------------------------------'''

''' Creating A Password Manager '''

''' Modules '''

import string
import os

''' Functions '''

# Password to open Password Manager 
def accept():
    temp = False
    while temp == False:
        ip = input("Enter the password >> ")
        print("--------------------------------------------------------------")
        if ip == 'sagar':
            # if password is correct allow 
            temp = True
            break
        else:
            temp = False
            # if password is incorrect do not allow 
            print('Invalid password, try again !')
            print("--------------------------------------------------------------")
    return temp

# MODES OF OPERATION
def mode(app_list,pwd_list):
    # allow the user to choose a mode 
    m = input("\t *** Choose a mode *** \n (V) to view, (A) to add, (C) to clear, (Q) to quit\n >> ").upper()
    print("--------------------------------------------------------------")
    if m == 'A':
        add(app_list,pwd_list)
    elif m == 'V':
        view(app_list,pwd_list)
    elif m == 'C':
        temp = input('Are you sure you want to delete the data? (Yes or No) : ').lower()
        print("--------------------------------------------------------------")
        if temp == 'yes':
            app_list,pwd_list = clear(app_list,pwd_list)
    elif m == 'Q':
        print('\t\t*** THANK YOU ***')
        print("--------------------------------------------------------------")
        return False
    else:
        print('Invalid mode, try again !')
        print("--------------------------------------------------------------")

# ADD MODE 
def add(app_list,pwd_list):
    app = input("Application >> ")
    pwd = input("Password >> ")

# Step - 01 >>
    # update newly added apps and passwords to respective list 
    update_list(app_list,pwd_list,app,pwd)  

# Step - 02 >>
# adds new app and pwd elements to current list 
def update_list(app_list,pwd_list,app,pwd):
    app_list.append(app)
    pwd_list.append(pwd)

# VIEW MODE
def view(app_list,pwd_list):
    remove_contents()
    # check for previously stored data  
    # --> for apps 
    file = os.stat("apps.txt").st_size
    if file == 0:
        # file is empty 
        pass
    else:
        with open('apps.txt','r+') as file:
            for line in file:
                line = line.rstrip()
                if line not in app_list:
                    app_list.append(line)

    # --> for pwds 
    file = os.stat("pwds.txt").st_size
    if file == 0:
        # file is empty 
        pass
    else:
        with open('pwds.txt','r+') as file:
            for line in file:
                line = line.rstrip()
                if line not in pwd_list:
                    pwd_list.append(line)

# Step - 01 
    e_app_list,e_pwd_list = encrypter(app_list,pwd_list)

    # display encoded file to user s
    with open('encoded_file.txt','r+') as f:
        f.write('\t------------------\n')
        f.write('\t|  Encoded File  |\n')
        f.write('\t------------------\n')
        for i in range(0,len(e_app_list)):
            f.write(f'{i+1}) App -> {e_app_list[i]} | Password -> {e_pwd_list[i]}\n')
        for line in f.readlines():
            print(line.rstrip())
    print('>> Encoded File Displayed')

# Step - 02 >> 
    # ask user for master password to decrypt file
    print("--------------------------------------------------------------")
    print('*** Master Password decodes the encoded file ***')
    print("--------------------------------------------------------------") 
    master_pwd = input('Enter the master password >> ')
    print("--------------------------------------------------------------")
    if master_pwd == 'mane':
        d_app_list,d_pwd_list = decrypter(e_app_list,e_pwd_list)
        # display decoded file to user
        with open('decoded_file.txt','r+') as f:
            f.write('\t------------------\n')
            f.write('\t|  Decoded File  |\n')
            f.write('\t------------------\n')
            for i in range(0,len(d_app_list)):
                f.write(f'{i+1}) App -> {d_app_list[i]} | Password -> {d_pwd_list[i]}\n')
            for line in f.readlines():
                print(line.rstrip())
    else:
        print('Wrong password !')
    print('>> Decoded File Displayed')
    print("--------------------------------------------------------------")


# ENCRYPTER 
''' PROCESS :- Original --> Reversing --> Encoding '''
def encrypter(app_list,pwd_list):
# Step - 01 >>
    # form dict of encrypted alphabets 
    alpbts = string.ascii_lowercase
    rev_alphbts = string.ascii_lowercase[::-1]
    d1 = dict(zip(alpbts,rev_alphbts))

    # form dict of encryped numbers
    num = [str(x) for x in range(0,10)]
    rev_num = num[::-1]
    d2 = dict(zip(num,rev_num))

    # form final dict containing 'key:value' pair of 'original:encrypted' pair
    d1.update(d2)
    d = d1

# Step - 02 >> 
    # list to store reverse app and password
    rev_app_list = []
    rev_pwd_list = []

    # append reverse of app and password in respective lists 
    for a in app_list:
        rev_app_list.append(a[::-1])
    for p in pwd_list:
        rev_pwd_list.append(p[::-1])

# Step - 03 >>
    # list to store encoded app and password 
    new_app_list = []
    new_pwd_list = []

    # encoding apps 
    a  = ''
    for app in rev_app_list:
        for letter in app:
            if letter in d.keys():
                letter = d.get(letter)
                a += letter
        new_app_list.append(a)
        a = ''

    # encoding pswds 
    p  = ''
    for pwds in rev_pwd_list:
        for letter in pwds:
            if letter in d.keys():
                letter = d.get(letter)
                p += letter
        new_pwd_list.append(p)
        p = ''

    # pass on the encoded app and password  list
    return (new_app_list,new_pwd_list)

# DECRYPTER 
''' PROCESS :- Encoded --> Decoding --> Reversing '''
def decrypter(e_app_list,e_pwd_list):
# Step - 01 >>
    # form dict of encrypted alphabets 
    alpbts = string.ascii_lowercase
    rev_alphbts = string.ascii_lowercase[::-1]
    d1 = dict(zip(alpbts,rev_alphbts))

    # form dict of encryped numbers
    num = [str(x) for x in range(0,10)]
    rev_num = num[::-1]
    d2 = dict(zip(num,rev_num))

    # form final dict containing 'key:value' pair of 'original:encrypted' pair
    d1.update(d2)
    d = d1

# Step - 02 >>  
    # list to store encoded app and password 
    new_app_list = []
    new_pwd_list = []

    # decoding apps 
    a  = ''
    for app in e_app_list:
        for letter in app:
            if letter in d.keys():
                letter = d.get(letter)
                a += letter
        new_app_list.append(a)
        a = ''

    # decoding pswds 
    p  = ''
    for pwds in e_pwd_list:
        for letter in pwds:
            if letter in d.keys():
                letter = d.get(letter)
                p += letter
        new_pwd_list.append(p)
        p = ''

# Step - 03 >> 
    # list to store reverse of decoded app and password
    rev_app_list = []
    rev_pwd_list = []

    # reversing decoded elements to form final lists 
    for a in new_app_list:
        rev_app_list.append(a[::-1])
    for p in new_pwd_list:
        rev_pwd_list.append(p[::-1])

    # pass on the decoded app and password  list
    return (rev_app_list,rev_pwd_list) 

# CLEAR MODE 
def clear(app_list,pwd_list):

    with open('apps.txt','r+') as f:
        f.truncate(0)
    with open('pwds.txt','r+') as f:
        f.truncate(0)
    with open('encoded_file.txt','r+') as f:
        f.truncate(0)
    with open('decoded_file.txt','r+') as f:
        f.truncate(0)
    
    app_list.clear()
    pwd_list.clear()

    return app_list,pwd_list
 
# STORE DATA
def store_data(app_list,pwd_list):

    with open('apps.txt','r+') as f:
        for i in range(0,len(app_list)):
            f.write(f'{app_list[i]}\n')

    with open('pwds.txt','r+') as f:
        for i in range(0,len(pwd_list)):
            f.write(f'{pwd_list[i]}\n')

def remove_contents():

    with open('encoded_file.txt','r+') as f:
        f.truncate(0)
    with open('decoded_file.txt','r+') as f:
        f.truncate(0)

''' Main Code '''

print("--------------------------------------------------------------")
print('\t *** Password Manager ***')
print("--------------------------------------------------------------")

# ask the user for password to open password manager
temp = accept()

# initiate app and password lists 
app_list = []
pwd_list = []

while temp == True:
    # allow the user to choose a mode 
    m = mode(app_list,pwd_list)
    if m == False:
        break

# clears the files before exiting the system
with open('encoded_file.txt','r+') as f:
            f.truncate(0)
with open('decoded_file.txt','r+') as f:
            f.truncate(0)

store_data(app_list,pwd_list)

'''---------------------------------------End of code---------------------------------------'''