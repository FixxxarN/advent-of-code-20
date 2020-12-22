import math

boarding_passes = []
highest_seat_id = 0

seats = []

with open("day-05/input.txt", "r") as filehandler:
    filecontents = filehandler.readlines()

    for line in filecontents:
        boarding_passes.append(line.split('\n')[0])

for boarding_pass in boarding_passes:
    current_rows_left = 0
    current_rows_right = 127
    current_column_left = 0
    current_column_right = 7

    chosen_row = 0
    chosen_column = 0

    for char in boarding_pass:
        if char == 'F':
            current_rows_right = int(math.floor(max(current_rows_left, current_rows_right) -
                                                (max(current_rows_left, current_rows_right) - min(current_rows_left, current_rows_right)) / 2))
        elif char == 'B':
            current_rows_left = int(math.ceil(max(current_rows_left, current_rows_right) -
                                              (max(current_rows_left, current_rows_right) - min(current_rows_left, current_rows_right)) / 2))
        elif char == 'L':
            current_column_right = int(math.floor(max(current_column_left, current_column_right) -
                                                  (max(current_column_left, current_column_right) - min(current_column_left, current_column_right)) / 2))
        elif char == 'R':
            current_column_left = int(math.ceil(max(current_column_left, current_column_right) -
                                                (max(current_column_left, current_column_right) - min(current_column_left, current_column_right)) / 2))

    if boarding_pass[6] == 'F':
        chosen_row = current_rows_left
    elif boarding_pass[6] == 'B':
        chosen_row = current_rows_right

    if boarding_pass[len(boarding_pass) - 1] == 'L':
        chosen_column = current_column_left
    elif boarding_pass[len(boarding_pass) - 1] == 'R':
        chosen_column = current_column_right

    seat_id = (chosen_row * 8) + chosen_column
    seats.append(seat_id)
    highest_seat_id = max(highest_seat_id, seat_id)

# Part 1
print("Highest seat: " + str(highest_seat_id))

# Part 2
seats.sort()
index = 0
for seat in seats:
    if seat != min(seats) and seat != max(seats):
        if seats[index - 1] != seat - 1:
            print("My seat: " + str(seat - 1))
    index += 1
