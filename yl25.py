dictionary = {
"first-name": "Kevin",
"last-name": "Pihlak",
"birthyear": "2005",
"living_place": "Orissaare",
"favorite_desert": "Pancake"
}

print(päevik.get("living_place"))
print(päevik["living_place"])

päevik.update({"favorite_desert": "Ice cream" })

print(päevik.keys())

print(päevik.values())

if 'ID' in päevik :
    print("Have ID")
else:
    print("Not have ID")

print(len(päevik))

päevik.update({"length": len(päevik)})

päevik.pop("birthyear")

del dictionary