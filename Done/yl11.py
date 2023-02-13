s = input("Sisesta string: ").strip()

if len(s) >= 7 and len(s) % 2 == 1:
  middle = len(s) // 2
  print(s[middle-1:middle+2])
else:
  print("Sisestatud string ei vasta tingimustele.")



