# A simple program to output who's paying the bill

import random

seedVariable = input("Create a seed:")
random.seed(seedVariable)

names_Input = input("Enter the names, separated by a comma: ")


# split names entered by user
names = names_Input.split(", ")

randomNumber = random.randint(0, len(names))

randomName = names[randomNumber]

print(f"{randomName} will pay the bill. ")