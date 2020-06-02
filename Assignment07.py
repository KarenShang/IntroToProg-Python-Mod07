# ---------------------------------------------------------------------#
# Title: Assignment07
# Description: A simple example of pickling and error handling
# ChangeLog:(who,when,what)
# Zhihua Shang, 5/28/2020, Created Script
# Zhihua Shang, 5/29/2020, update pickling and error handling codes
# Zhihua Shang, 6/1/2020, update pickling and error handling codes
# ---------------------------------------------------------------------#

import pickle
# --------Data ------------------------------------ #
# declare variables
dataFile = "contactList.dat"
contactList = []

# --------Processing ------------------------------------ #

# store the data with the pickle.dump method
def saveData(data_File,contactList):
    ''' Save list data into a file
        :param dataFile: (string) with name of file:
        :param contactList: (list) you want filled with data:
        :return: nothing
    '''

    file = open(data_File,"ab") # append a new binary file.
    pickle.dump(contactList,file) # dump the contactList data to file to store
    file.close()  # close the file
    print("Data saved!")

# read the data back with the pickle.load method
def readData(data_File):
    '''Read/unpickling data from a pickled file
        :param data_File: (string) name of file:
        :return: data that loaded from the file
    '''
    fileData=[]
    file = open(data_File, "rb") # read the binary file
    while True:  # read the all data
        try:
            fileData.append(pickle.load(file))
        except EOFError:
            break
    file.close()  # close the file
    return fileData


def nameInput():
    ''' Get users' name'''
    while True:
        try: # using try to customized how the program handles errors
            name = input("Enter your name: ") # get users' input
            if name.isnumeric(): # if name is a number, then raise exception.
                raise Exception("Do not use numbers for your name.")
            else:
                break

        except Exception as e:
            print("Enter a string of characters.")
            print(e)

    return name

def phoneInput():
    ''' Show the catching specific errors using more specific exception clauses'''
    while True:
        try: # using try to customized how the program handles errors.
            phone = int(input("Enter your phone number: ")) # get users' input which are integers.
            if len(str(phone)) !=10: # a condition of total numbers should be 10.
                raise Exception("Enter 10 numbers.")
        except ValueError:  # a specific error
            print("That was not a number. Enter numbers, please")
        except Exception as e: # a general error
            print("There was a non-specific error!")
            print(e)
        else:
            break

    return phone


# --------Presentation ------------------------------------ #
# get users'input and store inputs into a list
# name = input("Enter your name: ")
# phone = int(input("Enter your major: "))
# contactList=[name,phone]

# changed the above variables to method and call method.
contactList=(nameInput(),phoneInput())


# store the data with the pickle.dump method
saveData(dataFile,contactList)

# read the data back with the pickle.load
readData(dataFile)
for row in contactList:
    print(row,end=' ')
