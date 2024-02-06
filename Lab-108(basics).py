print("Hello world")
print("Python has three numeric types: int, float, and complex")
############## Creating a variable ##############
#To get the data type of the variable, use the type() built-in function:
#Use the str() built-in function, which converts an argument into a collection of letters called a string. 
#In this instance, you are converting the int (integer) data type into the string data type:
myValue=1
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

############## float data type ##############
print(myValue)
#To get the data type of the variable, use the type() built-in function:
print(type(myValue))
#To combine numbers and text, use the str() built-in function, which converts an argument into a collection of letters called a string. In this instance, you are converting the int (integer) data type into the string data type:
print(str(myValue) + " is of the data type " + str(type(myValue)))

############## String data type ##############
myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

############## String concatenation ##############
#The plus sign (+) is used to concatenate strings. 
#When the plus sign (+) is used with strings, it behaves differently than when you use it for numbers. 

fistring = "water"
secondstring = "fall"
thirdstring = fistring + secondstring
print(thirdstring)

############## Input strings ##############
#Input is known as information that a user enters. 
#You will use a built-in function named input() to get information from the user. 
#The input() function will pause the code until a user enters a string and presses
name = input("What is your name?")
print(name)

#Formatting output strings
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{} you like a {} {}!".format(name,color,animal))

############## Lists, Tuples, and Dictionaries ##############
myfruitlist = ["apple","banana","cherry"]
print(myfruitlist)
print(type(myfruitlist))

#Accessing a list by position
print(myfruitlist[0])
print(myfruitlist[1])
print(myfruitlist[2])

#Changing the values in a list !!!!!!!!!!!!!!
myfruitlist[2] = "lemon"
print(myfruitlist)

#Introducing the tuple data type

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

myFinalAnswerTuple[2] = "lemon" #Here we can se that we can not change pinapple to lemon because of Tuple 
print(type(myFinalAnswerTuple))

############## Dictionary data type ############### 
# Dictionary is a list with named positions (keys). 
#Imagine that your list shows people’s favorite fruit.
myFavoriteFruitDictionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo" : "pinapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

# Accessing a dictionary by name
#In this activity, you will use the name of the individuals to get their favorite fruit, instead of numbers.
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

############## Categorizing Values ##############
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print("{} is of data type {}".format(item,type(item)))


########################################################
