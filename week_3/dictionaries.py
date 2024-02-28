laptop={"make":"hp","colour":"grey","weight":"1kg","year":"2010"}

print(laptop["make"])
print(laptop["colour"])
laptop["size"]= "120mm by 90mm"
for key,value in laptop.items():
    print(key)
    print("\n")
    print(value)
del laptop["colour"]
print(laptop)