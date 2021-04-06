j = input()
if j.isdigit():
  i = 0
  j = int(j)
  while True:
    print(i)
    i += 1
    if i == j or i == 10:
      break
else:
  print('input must be digit')
