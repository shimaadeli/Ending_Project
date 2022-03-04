import random
import math


def read_file(name):
    file = open(name, "r")
    lines = []
    for line in file:
        desired_array = [int(numeric_string) for numeric_string in line.split()]
        lines.append(desired_array)
    file.close()
    return lines


def truthness(line, list):
    for i in range(1, len(line)):
        if (line[i] > 0 and list[line[i] - 1]) or (line[i] < 0 and list[-line[i] - 1] is False):
            return True

    return False


def true_clauses_ratio(lines, list, clauses_count):
    true_clauses = 0
    for line in lines:
        if truthness(line, list):
            true_clauses += 1
    return true_clauses * 1.0 / clauses_count


def positive_to_negative(number, lines):
    for i in range(len(lines)):
        for j in range(1, len(lines[i])):
            if number == lines[i][j]:
                lines[i][j] = -number
            elif number == -lines[i][j]:
                lines[i][j] = number
    return lines


def fix_single_literals(lines, variables_count):
    positive_repetition = [0] * variables_count
    negative_repetition = [0] * variables_count
    for line in lines:
        if len(line) == 2:
            if line[1] > 0:
                positive_repetition[line[1] - 1] += 1
            else:
                negative_repetition[-line[1] - 1] += 1
    for i in range(variables_count):
        if positive_repetition[i] < negative_repetition[i]:
            lines = positive_to_negative(i + 1, lines)
    return lines


list = []

lines = read_file("2.cnf")
variables_count = lines[0][0]
clauses_count = lines[0][1]
lines = lines[1:len(lines)]
lines = fix_single_literals(lines, variables_count)

for i in range(variables_count):
    if random.random() < (math.sqrt(5) - 1) / 2:
        list.append(True)
    else:
        list.append(False)

print(true_clauses_ratio(lines, list, clauses_count))
