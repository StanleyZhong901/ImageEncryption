from PIL import Image
import numpy as np
import os

def decryptingMessage(deleteTheFile):
    flag1 = False
    flag2 = False
    xDimension = 200
    yDimension = 200
    hashInt = None

    try:
        data = np.array((Image.open('encryptedPhoto.png')))
        flag1 = True
    except FileNotFoundError:
        os.system('cls')
        print("Error: File Not Found")

    while (hashInt == None) and (flag1 == True):
            try:
                hashInt = int(input("Enter Key: "))
            except ValueError:
                os.system('cls')
                print("Error: Input Valid Key")
                hashInt = None

    if (flag1 == True) and (hashInt != data[xDimension-2][yDimension-1][2]):
         os.system('cls')
         print("Wrong Key")
    elif (flag1 == True) and (hashInt == data[xDimension-2][yDimension-1][2]):
         flag2 = True

    if (flag1 == True) and (flag2 == True):
        lengthOfString = data[xDimension-1][yDimension-1][2]

        xValue = hashInt
        yValue = 0
        zValue = 0

        outString = ""

        for i in range(lengthOfString):
            if xValue >= xDimension:
                xValue = xValue - xDimension
                yValue += 1
                if yValue >= yDimension:
                    yValue = yValue - yDimension
                    zValue += 1

            outString += chr(data[xValue][yValue][zValue] + 31)
            xValue += hashInt
        os.system('cls')
        print("Encrypted Message: " + outString)
        if deleteTheFile == True:
            os.remove('encryptedPhoto.png')
    