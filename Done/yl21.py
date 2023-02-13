import random

#mõtleb välja arvu
number = random.randint(0, 100)

# pakkumine
guess = int(input("Pakkuge arvu 0 ja 100 vahel: "))

# kontrollime pakkumist, kuni see on õige
while guess != number:
  if guess < number:
    print("Arv on suurem.")
  else:
    print("Arv on väiksem.")
  guess = int(input("Pakkuge uuesti: "))

# väljastame teate, kui pakkumine on õige
print("Õige! Arvuti mõtles välja arvu", number)
