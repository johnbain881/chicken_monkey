numbers = list(range(1, 101, 1))
# print(numbers)


def chicken_monkey(num):
  if num%5 == 0 and num%7 == 0:
    return "ChickenMonkey"
  elif num%5 == 0:
    return "Chicken"
  elif num%7 == 0:
    return "Monkey"
  else:
    return ""


for number in numbers:
  print(chicken_monkey(number))