groups = []
sum_of_answered_questions = 0
sum_of_yes_questions = 0

with open('day-06/input.txt', 'r') as filehandler:
    filecontents = filehandler.read().split('\n\n')
    for line in filecontents:
        groups.append(line)


def count_duplicates_from_group(group):
    return len("".join(set(group)))


def count_yes_answers_in_group(group):
    char_answers = ''
    answers = group.strip().split('\n')
    if len(answers) == 1:
        return count_duplicates_from_group(answers[0].replace('\n', ''))
    else:
        index = 0
        for answer in answers:
            for char in answer:
                if all(char in c for c in answers[:index] + answers[index + 1:]):
                    char_answers += str(char)
            index += 1
    return count_duplicates_from_group(char_answers)


for group in groups:
    sum_of_answered_questions += count_duplicates_from_group(
        group.replace('\n', ''))
    sum_of_yes_questions += count_yes_answers_in_group(group)


# Part 1
print(sum_of_answered_questions)

# Part 2
print(sum_of_yes_questions)
