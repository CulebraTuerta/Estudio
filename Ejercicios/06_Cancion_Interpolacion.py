# String interpolation

for i in range(100):
  print(f'{99-i} bottles of beer on the wall')
  print(f"{99-i} bottles of beer")
  print("Take one down, pass it around")
  print(f'{98-i} bottles of beer on the wall')
  print("")

# OR (Mejor forma para ir de atras a adelante...)

for i in range(99, 0, -1):
  print(f'{i} bottles of beer on the wall')
  print(f'{i} bottles of beer')
  print('Take one down, pass it around')
  print(f'{i-1} bottles of beer on the wall')