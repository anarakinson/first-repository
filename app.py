j = input()
if j.isdigit():
  j = int(j)
  for i in range(j):
    if i >= 10:
      break
    print(i)
else:
  print('input must be digit')
