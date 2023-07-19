#list
myFruitList=[
    "apple",
    "banana",
    "cherry",
    1
]
print(str(myFruitList)+" " +str(type(myFruitList)))
myFruitList[2]="strawberry " #mutable
print(myFruitList)
#tuple
myTuple = (
    "apple",
    "banana ",
    "pineapple ",
    99
    )
print(str(myTuple)+" "+str(type(myTuple)))
#dictionary 
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(str(myFavoriteFruitDictionary)+str(type(myFavoriteFruitDictionary)))
print(myFavoriteFruitDictionary["Paulo"])