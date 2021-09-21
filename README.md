
# Password Manager

Creating a password manager that can encrypt, decyrpt and store passwords securly.
### Thought Process

- Ask the user for the password that opens password manager.
- Ask the user for the mode which are view, add, clear and quit.
- In add mode take inputs from the user regarding apps and passwords that he/she want to store in system.
- This will create a encrypted file containing information of those apps and passwords.
- In view mode first display the encoded file and then ask for master password.
- Authentication through master password further displays the decoded file to the user.
- Also store info on apps and passwords added by user in the system.
- In clear mode simply clear the all the files.
- In quit mode exit the system.



  
## Code Description

All the modules and functions in this project are explained below.

  
### Modules 

`import string`

`import os`







  
### Functions

```bash
  def accept():
```

This function asks the user for password and upon successful authentication opens the password manager for the user.

```bash
  def mode(app_list,pwd_list):
```
This function asks the user to choose a mode (View, Add, Clear & Quit) and upon selection continues to exceute the set of insstructions present in the respective mode.

```bash
  def add(app_list,pwd_list):
```
This function allows the user to enter apps and their respective passwords that they want to store and also simulataneously updates the app and password list.

```bash
  def update_list(app_list,pwd_list,app,pwd):
```
This function is used toadd newly added apps and passwords to the apps and password list so that they can be displayed when needed further in the program.

```bash
  def view(app_list,pwd_list):
```
This function displays the apps and passwords stored via password manager but first displays a encoded file and upon successful authentication through the master displays the decoded file to the user.

```bash
  def encrypter(app_list,pwd_list):
```
This function takes the app and password list and further encrypts it to be displayed later in encoded file. Encoding process consists of reversing the string and then replacing each character by their mirror character from the dictionary which consists of alphabets as key and reverse alphabets as value in it.

```bash
  def decrypter(e_app_list,e_pwd_list):
```
This function takes the app and password list encrypted by the encrypter and further decrypts it to be dislayed later in decoded file. Decoding process consists of replacing each character by their mirror character from the dictionary which consists of alphabets as key and reverse alphabets as value in it and then reversing the string.

```bash
  def clear(app_list,pwd_list):
```
This function clears all the data present in endoded, decoded, apps and pwds file.

```bash
  def store_data(app_list,pwd_list):
```
This function stores the data related to apps and passwords entered by the user.

```bash
  def remove_contents():
```
This function clears all the content present in encoded and decoded file.



### Conclusion

This project was an attempt to create a password manager that can securly store data on apps and passwords by including various modes of operation along with encrypting and decrypting to make it more safer.
  