from copy import deepcopy

def matrix_bombing_plan(m):
    rows = len(m)
    columns = len(m[0])
    after_bombing = {}
    for row in range(rows):
        for column in range(columns):
            new_matrix = deepcopy(m)
            neighbours = filtrare_neighbours(row, column, rows - 1, columns - 1)
            for current_neighbour in neighbours:
                r, c = current_neighbour
                new_matrix[r][c] = modify_value(new_matrix[r][c], m[row][column])
            result = sum(map(sum, new_matrix))
            after_bombing.update({(row, column) : result})
    print(after_bombing)

def modify_value (element, toSubstract):
    element -= toSubstract
    if element >= 0:
        return element 
    return 0

def filtrare_neighbours(current_row, current_column, rows, columns):
    row_indexes = [current_row - 1, current_row, current_row + 1]
    row_indexes = [element for element in row_indexes if element >= 0 and element <= rows]

    column_indexes = [current_column - 1, current_column, current_column + 1]
    column_indexes = [element for element in column_indexes if element >=0 and element <= columns]

    neighbours = [(a, b) for a in row_indexes for b in column_indexes]
    neighbours.remove((current_row, current_column))

    return neighbours

matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]])