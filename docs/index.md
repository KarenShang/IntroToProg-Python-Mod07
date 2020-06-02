
# Pickling and Exception Handling in Python
**Dev** *Zhihua Shang*   
**Date** *6.1.2020*  

## Introduction
Python is a very popular tool at the workplace to deal with data. However, in the real world, many types of data need to be dealt with rather than some simple plain text files, so pickling is introduced in this assignment to store more complex information. Meanwhile, error is normal to encounter when users run the code. In this assignment, an exception handing approach will also be explained step by step. 
Create a folder and Open the downloaded file
Open file via PyCharm. Click create new project, name it as Assignment07, and save it under _PythonClass in C: drive (Figure 1).

 ![Figure 1](https://github.com/KarenShang/IntroToProg-Python-Mod07/blob/master/docs/1.png)
#### Figure 1: Showing the location of Assginment07.py
## Coding
This is the main and most important part of the whole process. The first step is to figure out what is the objectives of the script then edit the codes. This part shows the steps of updating the script header, pickling and unpickling codes, error handling codes, and demonstration of the results.
### Update the changelog in the header
A header is very important for both the creators and other users. It provides some basic information about this script. For example, the title, simple description, the creator, and the created date. If some codes will be updated, then the changes notification could be added each time to the header (Figure 2).

 ![Figure 2](https://github.com/KarenShang/IntroToProg-Python-Mod07/blob/master/docs/2.png) 
#### Figure 2:  Showing the updated changelog of file.
### Pickling and unpickling codes
Pickling and Unpickling is very practical in real world because it allows people to transfer data easily. In this simple example, several steps are taken to finish the whole process. The first step is to import pickle and declare some variables which includes a file and a list (Figure 3).

![Figure 3](https://github.com/KarenShang/IntroToProg-Python-Mod07/blob/master/docs/3.png)
#### Figure 3:  Showing the codes of importing pickle and variables.
  
The second step is to get users’ input and store the data in a list (Figure 4).

![Figure 4](https://github.com/KarenShang/IntroToProg-Python-Mod07/blob/master/docs/4.png)
#### Figure 4: Showing the codes of inputs

The third step is to save the data to a file. In order to make the codes more professional. It is better to define a saveData function. Inside the scope, an open() function is used in this situation, and an append mode which is “ab” can also be used. It means to append and read from a binary file. If the file exists, new data is appended to it. If the file does not exist, it is created. Meanwhile, pickle.dump() function is to save the list of data to a file (Figure 5). 

![Figure 5]()
#### Figure 5: Showing the code of saveData function.


After the data are saved, a read function is to be made. This step is to unpickle data from a pickled file. Open the file and an access mode of “rb” is used for reading the binary file, then pickle.load() is used to load the binary file to a variable. In order to read all data, a while loop is used unless it run out (Figure 6).  

![Figure 6]() 
#### Figure 6: Showing the codes of readData function. 

The last step of this part is to recall the functions that defined earlier at the main body area (Figure 7).

![Figure 7]()
#### Figure 7: Showing the codes of recalling functions at main body.

The above steps are just showed a list as an example. Pickling and unpickling can also deal with dictionaries. If you are interested in it, more examples from this website https://www.tutorialspoint.com/python-pickling. This tutorial not only shows the examples both list and dictionary but also explained the cons and prons of pickle files. This is very helpful for python beginnings to have a better understanding of pickle module.  
### Error handling 
When Python runs into an error, it stops the current program as well as raises an exception which is an error message. Most common way to trap exceptions is to use the try statement with a except clause. In order to show the approach, the users’ input part was changed to two functions from two variable. The first one is nameInput. When you want to save a contact list, name means a series of characters. However, some people may insert numbers, then try and except approach can be used. When name is a number, the exception raise and remind the users to insert characters rather than numbers (Figure 8). 

![Figure 8]() 
#### Figure 8:  Showing the try statement with an except Clause  

Try statement can also catch some specific errors. For example, in this python script, the phone number has to be integer. If the users’ put the string or float number, a ValueError will be stop the codes. If there’s other type of errors, the general Exception will catch them. Meanwhile, if the phone numbers are not 10 integers, an error also raise (Figure 9).  This script only shows some simple type of specific error. There are more types in the following website, and the explaining of basic understanding terminologies is very helpful.
(https://www.datacamp.com/community/tutorials/exception-handling-python).
![Figure 9]()
#### Figure 9:  Showing the try statement with a specific except Clause  


### Demonstrate in PyCharm
This is the result that showing in PyCharm (Figure 10). 

![Figure 10]() 
#### Figure10: Showing the result in PyCharm.
### Demonstrate in Command Window
Beside working in PyCharm, the python file can also work in a command window. The first step is to go to start, search and click CMD. The Command Prompt window shows up. Typing ‘python’ and pasting the path of the BasicMath.py file, then the information shows up (Figure 11).

![Figure 11]() 
#### Figure 11: script running from command.
### Demonstrate in Shell window

The same script could also be demonstrated in IDE shell. Go to start, search and click IDE. The shell window shows up. Find file and open from the Assignment07 which is under_PythonClass in C drive. Run it, and the same result will be shown (Figure 12).

![Figure 12]() 
#### Figure 12: script running from Shell window

## Summary
Pickling is not only used to deal with the complex information but also store them in a file with a single line of code.  Meanwhile, error handling is very user-friendly. By using these useful tools at workplace, it is very practical to manage a group of pickled objects in a single binary file, and it is timesaving to deal with the potential errors.  



