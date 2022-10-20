num=int(input('Sisesta Aasta:'))

div=400
div2=3
div3=100

if num%div == 0 or num%div2 == 0 and num%div3 != 0:

    print("on liigaasta")
else:
    print("ei ole liigaasta")