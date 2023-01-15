n = int(input())

array = [int(x) for x in input().split()]

array.sort()

b, c = 0, 0

for number in array:
  if (number > 0):
    b += number
  else:
    c += number

print(b - c)
