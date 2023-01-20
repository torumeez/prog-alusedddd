dictionary = {
   "first-name=": "Kevin",
   "last-name=": "Pihlak",
   "birth-year=": "2005",
   "living-place=": "Orissaare",
   "favorite-desert=": "Pancake"
}

#print(dictionary.get("living_place"))
#print(dictionary["living_place"])

dictionary.update({"favorite-desert=": "Ice cream" })

#print(dictionary.keys())

#print(dictionary.values())

for x, y in dictionary.items():
  print(x, y)

 

if 'ID' in dictionary :
    print("Have ID")
else:
    print("Not have ID")

print(len(dictionary))

dictionary.update({"length": len(dictionary)})

dictionary.pop("birth-year=")

del dictionary