#list
myFruitList=[
    "apple",
    "banana",
    "cherry",
    1,
    2.4
]
# for items in myFruitList:
#     print(items)
# for items in range(len(myFruitList)):
#     print(myFruitList[items])
#print(str(myFruitList)+" " +str(type(myFruitList)))
myFruitList[2]="strawberry " #mutable
# print(myFruitList)
#tuple
myTuple = (
    "apple",
    "banana ",
    "pineapple ",
    99
    )
# print(str(myTuple)+" "+str(type(myTuple)))
# for items in range(len(myTuple)):
#     print(myTuple[items])
#dictionary 
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
for item in myFavoriteFruitDictionary:
    print(item)
print(str(myFavoriteFruitDictionary)+str(type(myFavoriteFruitDictionary)))
print(myFavoriteFruitDictionary["Paulo"])