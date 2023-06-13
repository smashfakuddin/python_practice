
# function
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))


my_function_with_args("ash", "Good morning")    

# function 1
def sum_number(a,b):
    sum_n = a + b
    print(sum_n)
    return sum_n

sum_number(5, 8)    

# function Exercise

def names_list():
    return ["Ash ", "Jara" , "Shahed"]

def greeting(n):
    return "%s is a Good boy Or girl" % n

def greeting_person():
    list_name = names_list()
    for grt in list_name:
        print(greeting(grt)) 

greeting_person()



# same output with for loop 

n_list = ["Ash ", "Jara" , "Shahed"]

for n in n_list:
    print("%s is a good boy/girl" %n)