# program to get the records of an employee
f_name=input("enter first name")
s_name=input("enter second name")
salary=float(input("enter your salary"))
bonus=float(input("Enter your salary : "))
s_1=(salary + bonus)

print("my name is",f_name + s_name)
print("The sum of salary is",s_1)

s =salary
r =float(input("enter the rate : "))
b =float(input("enter the bonus change"))

h =(s + (s*(r/100)))
n_s =(h +(bonus+b))
print("the new salary is",n_s)
