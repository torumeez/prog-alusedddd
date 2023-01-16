me = {
   "eesnimi" : "Kevin",
   "perenimi" : "Pihlak",
   "sünniaasta" : 2005,
   "elukoht" : "Orissaare",
   "lemmik magustoit" : "Pannkook"
}

#print(me.get('elukoht'))
#print(me['elukoht'])

me['lemmik magustoit'] = 'Jäätis'

for v in me.items():
    print(v)