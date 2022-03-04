import random
import math
from scipy.optimize import linprog


def read_file(name):
    file = open(name, "r")
    lines = []
    for line in file:
        desired_array = [int(numeric_string) for numeric_string in line.split()]
        lines.append(desired_array)
    file.close()
    return lines


def solve_linear_program(lines, clauses_count, variables_count):
    c = [0] * (variables_count + clauses_count)
    bounds = []
    for i in range(clauses_count):
        c[i + variables_count] = -1
    for i in range(variables_count + clauses_count):
        bounds.append((0, 1))
    A = []
    b = []
    index = 0
    for line in lines:
        array = [0] * (variables_count + clauses_count)
        array[variables_count + index] = 1
        negative_count = 0
        for i in range(1, len(line)):
            if line[i] > 0:
                array[line[i] - 1] = -1
            else:
                array[-line[i] - 1] = 1
                negative_count += 1
        A.append(array)
        b.append(negative_count)
        index += 1
    return linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='revised simplex')


def quantification(result, variables_count):
    list = []
    for i in range(variables_count):
        if random.random() < result[i]:
            list.append(True)
        else:
            list.append(False)
    return list


def truthness(line, list):
    for i in range(1, len(line)):
        if (line[i] > 0 and list[line[i] - 1]) or (line[i] < 0 and list[-line[i] - 1] is False):
            return True

    return False


def true_clauses_ratio(lines, list, lp_answer):
    true_clauses = 0
    for line in lines:
        if truthness(line, list):
            true_clauses += 1
    return true_clauses * 1.0 / lp_answer


lines = read_file("2.cnf")
variables_count = lines[0][0]
clauses_count = lines[0][1]
lines = lines[1:len(lines)]

result = solve_linear_program(lines, clauses_count, variables_count)
list = quantification(result['x'], variables_count)
print(true_clauses_ratio(lines, list, -result['fun']))
