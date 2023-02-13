import random

# defineerib võimalikud valikud
options = ["kivi", "paber", "käärid"]

# küsib kasutajalt, kas ta tahab mängida
play = input("Kas soovite mängida kivi-paber-käärid (jah/ei): ").lower()

# mängitakse seni, kuni kasutaja ei taha enam mängida
while play == "jah":
  # arvuti mõtleb välja valiku
  computer = random.choice(options)

  # küsib kasutajalt valiku
  player = input("Valige kivi, paber või käärid: ").lower()

  # kontrollib, kes võitis
  if player == computer:
    print("Viik!")
  elif player == "kivi" and computer == "käärid":
    print("Võitsite!")
  elif player == "paber" and computer == "kivi":
    print("Võitsite!")
  elif player == "käärid" and computer == "paber":
    print("Võitsite!")
  else:
    print("Kaotasite.")

  # küsib uuesti, kas kasutaja tahab mängida
  play = input("Kas soovite mängida uuesti (jah/ei): ").lower()

# teade, kui kasutaja ei taha enam mängida
print("Mäng lõppenud.")
