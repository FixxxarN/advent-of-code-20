# Part 1

valid_passwords = 0
amount_of_passwords = 0

with open("day-02/input.txt", "r") as filehandler:
    passwords_from_file = filehandler.readlines()

    for password in passwords_from_file:
        current_password = password[:-1]
        min_amount_of_chars = int(current_password.split("-")[0])
        max_amount_of_chars = int(current_password.split("-")[1].split(" ")[0])
        must_have_char = current_password.split(
            "-")[1].split(" ")[1].split(":")[0]
        actual_password = current_password.split(": ")[1]

        if actual_password.count(must_have_char) >= min_amount_of_chars and actual_password.count(must_have_char) <= max_amount_of_chars:
            valid_passwords += 1

print(valid_passwords)

# Part 2

valid_passwords = 0

with open("day-02/input.txt", "r") as filehandler:
    passwords_from_file = filehandler.readlines()

    for password in passwords_from_file:
        current_password = password[:-1]
        first_index_where_char_has_to_occur = int(
            current_password.split("-")[0])
        second_index_where_char_has_to_occur = int(
            current_password.split("-")[1].split(" ")[0])
        must_have_char = current_password.split(
            "-")[1].split(" ")[1].split(":")[0]
        actual_password = current_password.split(": ")[1]

        if actual_password.find(must_have_char, first_index_where_char_has_to_occur - 1, first_index_where_char_has_to_occur) > -1:
            if actual_password.find(must_have_char, second_index_where_char_has_to_occur - 1, second_index_where_char_has_to_occur) < 0:
                valid_passwords += 1
        elif actual_password.find(must_have_char, second_index_where_char_has_to_occur - 1, second_index_where_char_has_to_occur) > -1:
            if actual_password.find(must_have_char, first_index_where_char_has_to_occur - 1, first_index_where_char_has_to_occur) < 0:
                valid_passwords += 1

print(valid_passwords)
