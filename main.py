a = int(input("Ievadi preces daudzums: "))
print("Vienas preces cena ir 2.35Ls")
print(a * 2.35)

if a * 2.35 > 4.7:
  print("Pienākās atlaide 10%!")
  print(a * 2.35 / 10.0)
else: 
  if a * 2.35 < 4.7:
    print("Nav atlaides!")
