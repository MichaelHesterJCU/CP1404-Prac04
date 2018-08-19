numbers = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0]              3
numbers[-1]             2
numbers[3]              1
numbers[:-1]            3, 1, 4, 1, 5, 9
numbers[3:4]            1
5 in numbers            true
7 in numbers            false
"3" in numbers          false
numbers + [6, 5, 3]     appends 6, 5, and 3 to the end of the list
"""
numbers[0] = "Ten"
print(numbers[0])
numbers[-1] = 1
print(numbers[-1])
print(numbers[1:-1])
print(9 in numbers)