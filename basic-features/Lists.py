# Lists and splicing almost exactly same as strings for lists
shoppingList = ["Apples", "Bananans", "Cucumber", "Dill Leaves", "Eggs", "Fish"]
print(shoppingList)

print(shoppingList[0])
print(shoppingList[5])

print(shoppingList[0:4])
print(shoppingList[:3])

# You can add to list with append function
shoppingList.append("Ginger")
shoppingList.append("Nuts")
print(shoppingList)

# Replace using placeholder
shoppingList[7] = "Mangoes"
print(shoppingList)

# Delete an element in list
del shoppingList[7]
print(shoppingList)

# Length function
print(len(shoppingList))

# Add Multiply Lists
shoppingList2 = ["Aioli", "Biscuits", "Caramel"]
print(shoppingList + shoppingList2)

print(shoppingList2 * 3)

# Max n Min Functions
numList = [1, 8, 91, 3, 45]
print(max(numList))
print(min(numList))