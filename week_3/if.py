# learning if function

age =25
if age > 18:
    print("You may drive")


salary= 45000
if salary >30000 and salary<50000:
    salary=salary*1.1

    #if....else...
    grade=70
    if grade>=84 and grade <=90:
        print("you get a calculator")
    elif grade >=50 and grade<=83:
        print("you get a mathematical set")
    else:
        print("you get nothing")

        #if.....else
    current_sal=int(input("Input current salary"))
    if current_sal>=30000 and current_sal<=50000:
        new_sal=current_sal*1.1
    else:
        new_sal= current_sal
        print (new_sal)


    salary = 150000
    if salary>100000:
        salary= salary * 0.3 +salary
        print(salary)
    if salary > 100000 and salary < 150000:
        salary= salary * 0.15 + salary
        print(salary)
    if salary> 150000:
        salary= salary * 0.05 + salary
        print(salary)
