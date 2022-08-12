# Given an integer input of a number, return the digits in sorted form

number = 782463
ascending = ''.join(sorted(str(number), reverse=True))
print(ascending)
