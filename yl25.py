dictionary = {
"first-name": "Kevin",
"last-name": "Pihlak",
"birthyear": "2005",
"living_place": "Orissaare",
"favorite_desert": "Pancake"
}

#print(dictionary.get("living_place"))
#print(dictionary["living_place"])

dictionary.update({"favorite_desert": "Ice cream" })

print(dictionary.keys())

print(dictionary.values())

if 'ID' in dictionary :
    print("Have ID")
else:
    print("Not have ID")

print(len(dictionary))

dictionary.update({"length": len(dictionary)})

dictionary.pop("birthyear")

del dictionary