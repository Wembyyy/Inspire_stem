friends=("David","Annita","Max","Winn","Hene")
for friend in friends:
    print(friend)

enemies= friends[:]# to copy one list into another
for enemy in enemies:
    print(enemy)

fruits=("guava","mango","orange","pineapple")# to slice is to get part of the list
print(fruits[0:1])

squares=[]#means its an empty list
for x in range(0,11):
    squares.append(x**2)
print(squares)

