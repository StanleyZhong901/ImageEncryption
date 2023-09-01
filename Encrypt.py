from PIL import Image
import numpy as np
import random
import os

def encryptingMessage():
    hashInt = None
    while (hashInt == None):
        try:
            hashInt = int(input("Enter Number (1 - 161): "))
            if (hashInt < 1) or (hashInt > 161):
                raise ValueError
        except ValueError:
            os.system('cls')
            print("Error: Enter Valid Integer")
            hashInt = None
        
    inString = input("Enter Message to Ecrypt: ")

    xDimension = 200
    yDimension = 200

    data = np.zeros((xDimension, yDimension, 3), dtype=np.uint8)

    xValue = hashInt
    yValue = 0
    zValue = 0

    flag = True

    encryption = hashInt

    for i in range(len(inString)):
        if (ord(inString[i]) > 126) or (ord(inString[i]) < 32):
            continue
        
        else:
            if xValue >= xDimension:
                xValue = xValue - xDimension
                yValue += 1
                if yValue >= yDimension:
                    yValue = yValue - yDimension
                    zValue += 1
                    if zValue == 3:
                        print("Error: Image cannot Encrypt anymore Data")
                        flag = False
                        break

            data[xValue][yValue][zValue] = (ord(inString[i]) - 31)
            xValue += encryption
    
    xValue = 0
    yValue = 0
    zValue = 0

    if flag == True:
        while zValue != 2:
            if xValue >= xDimension:
                xValue = xDimension - xValue
                yValue += 1
                if yValue >= yDimension:
                    yValue = yDimension - yValue
                    zValue += 1
            if data[xValue][yValue][zValue] == 0:
                data[xValue][yValue][zValue] = random.randint(0, 126)
            xValue += 1

    data[xDimension-1][yDimension-1][2] = len(inString)
    data[xDimension-2][yDimension-1][2] = hashInt
    image2 = Image.fromarray(data, "RGB")

    os.system('cls')
    image2.save('encryptedPhoto.png')
    print("Message Encrypted")

