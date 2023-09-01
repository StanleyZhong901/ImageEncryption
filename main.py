import Encrypt
import Decrypt
import os

os.system('cls')
print('''
1. Encrypt Message
2. Decrypt Message
3. Decrypt Message and Delete Image
4. Exit
''')

userInput = input("Enter Command:")

while userInput != '4':
    if userInput =='1':
        os.system('cls')
        Encrypt.encryptingMessage()
    elif userInput =='2':
        os.system('cls')
        Decrypt.decryptingMessage(False)
    elif userInput =='3':
        os.system('cls')
        Decrypt.decryptingMessage(True)
    elif userInput == '4':
        os.system('cls')
    else:
        os.system('cls')
        print("Error: Enter Value Input")
    print('''
1. Encrypt Message
2. Decrypt Message
3. Decrypt Message and Delete Image
4. Exit
''')
    userInput = input("Enter Command:")

os.system('cls')
print("Exiting Program")