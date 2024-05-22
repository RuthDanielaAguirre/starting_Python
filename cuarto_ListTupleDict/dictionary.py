#A dictionary is a list with named positions(keys) and values. In order to define it you use {} instead of [].

myFavoriteFruitDictionary = {
    "manzana" : "apple",
    "platano" : "banana",
    "piña" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))


#It can also be accessed by position by using the key instead of the position.

print(myFavoriteFruitDictionary["manzana"])

#It can also be changed.

myFavoriteFruitDictionary["manzana"] = "poma" 

print(myFavoriteFruitDictionary)