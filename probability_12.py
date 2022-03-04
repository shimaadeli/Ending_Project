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

list = []

lines = read_file("2.cnf")
variables_count = lines[0][0]
clauses_count = lines[0][1]
lines = lines[1:len(lines)]

for i in range(variables_count):
    if random.random() < 0.5:
        list.append(True)
    else:
        list.append(False)

print(true_clauses_ratio(lines, list, clauses_count))
