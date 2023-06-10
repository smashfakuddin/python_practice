# Boolean operators

name = "Ashfak"
age = 23

if name == "Ashfak" and age == 23:
    print("Your Name is Ashfak and age are 23 also")

if name== "john" or name == "Erik":
    print("Your Name is John or Erik")
else:
    print("Not found")



# The "in" operator


name = input("Enter Your name: ")
name_list = ["Ashfak","jay"]

if name in name_list:
    print("Name Found!")
else:
    print("Not Found!")

sample code for if statement using codeblock

statement = False
another_statement = False

if statement is True:
    print("It's true")
    pass
elif another_statement is True:
    print("It's also true")
    pass
else:
    print("False")
    pass
