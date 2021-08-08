# Strings and splicing
firstName = "Rushikesh"
lastName = "Teli"

print(firstName + " " + lastName)
print(firstName * 3)

sentence = "Rushikesh learning Python"
# Index starting zero
print(sentence[0])
print(sentence[0:10])

# Specify number of characters even negetive is possible
print(sentence[:5])
print(sentence[:-6])

# String Placeholder syntax
name = "Rushikesh"
print(name + " is 40 years old")

line = "%s is 40 years old"
print(line%name)
print(line%("Ram"))

# Multiple placeholders
sentence1 = "%s %s is innovative developer"
print(sentence1%(name, lastName))
print(sentence1%("Ram", "Krishna"))

# Mixed placeholders
sentence2 = "%s is %d years old"
print(sentence2%(name, 40))