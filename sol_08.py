# Advent of Code 2023
# Day 8

import numpy
import lib


sample_data_file = "input/sample/sample_08.txt"
full_data_file = "input/full/input_08.txt"

lines = lib.read_input(full_data_file)

# convert line strings into arrays before passing to numpy constructor
M = numpy.array([list(line) for line in lines])
N = numpy.zeros(M.shape)

for i, row in enumerate(M):
    # set row ends to 1
    N[i, 0] = N[i, len(row) - 1] = 1
    
    # scan right
    row_max = int(row[0])
    for j in range(1, len(row)):
        cell_val = int(row[j])
        if cell_val > row_max:
            row_max = cell_val
            N[i, j] = 1
            if cell_val == 9:
                break

    # scan left
    prev_row_max = row_max
    row_max = int(row[len(row) - 1])
    for j in range(len(row) - 2, 0, -1):
        cell_val = int(row[j])
        if cell_val > row_max:
            row_max = cell_val
            N[i, j] = 1
            if cell_val == 9 or cell_val == prev_row_max:
                break

N = N.T
M = M.T
for i, row in enumerate(M):
    # set row ends to 1
    N[i, 0] = N[i, len(row) - 1] = 1
    
    # scan right
    row_max = int(row[0])
    for j in range(1, len(row)):
        cell_val = int(row[j])
        if cell_val > row_max:
            row_max = cell_val
            N[i, j] = 1
            if cell_val == 9:
                break

    # scan left
    prev_row_max = row_max
    row_max = int(row[len(row) - 1])
    for j in range(len(row) - 2, 0, -1):
        cell_val = int(row[j])
        if cell_val > row_max:
            row_max = cell_val
            N[i, j] = 1
            if cell_val == 9 or cell_val == prev_row_max:
                break

print(N.sum())