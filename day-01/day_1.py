# List of numbers
numbers = []

# The numbers that sum up to 2020 together will be stored below
first_number = 0
second_number = 0
third_number = 0

# Reading from file
with open("day-01/input.txt", "r") as filehandler:
    filecontents = filehandler.readlines()

    for line in filecontents:
        current_place = line[:-1]
        # Adding number to the list
        numbers.append(current_place)

# Going through the list of numbers to check if some of them sum up to 2020
for fnum in numbers:
    for snum in numbers:
        for tnum in numbers:
            sum = int(fnum) + int(snum) + int(tnum)
            if sum == 2020:
                first_number = int(fnum)
                second_number = int(snum)
                third_number = int(tnum)
                break

# Printing the numbers and the multiplication of them all
print("First: " + str(first_number))
print("Second: " + str(second_number))
print("Third: " + str(third_number))
print("All: " + str((first_number * second_number * third_number)))
