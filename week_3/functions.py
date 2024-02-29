# functions are a block of code running together as a unit
def print_name():
    print("my name is chris wekesa")

#calling the function
print_name()

def print_details(name,age,id_number,gender):
    print("I am {0},my age is {1},my id number is {2},my gender is {3}".format(name,age,id_number,gender))

print_details("Chris","18","123456","male")


def sum_nums(x,y):
    return x+y
z=sum_nums(10,20)
print(z)

def prod_nums(x,y):
    return x*y
print(prod_nums(9,2))

def print_odds(first_no,last_no):
    for i in range(first_no,last_no):
        if i %2:
            print(i)
print_odds(0,15)
#write a function to print all prime numbers between 1 and 99
#write a function to print all squares and cubes of numbers between 1 to 10
#write a function to calculate surface area of cylinder,cone,cube and sphere
#write a function to calculate volume of the four above


