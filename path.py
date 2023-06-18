def travel(grid, visited, row, col, end_row, end_col, path):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return False
    if grid[row][col] == 0 or visited[row][col]:
        return False
    visited[row][col] = True
    if row == end_row and col == end_col:
        return True
    if travel(grid, visited, row+1, col, end_row, end_col, path):
        path.append('DOWN')
        return True
    if travel(grid, visited, row-1, col, end_row, end_col, path):
        path.append('UP')
        return True
    if travel(grid, visited, row, col+1, end_row, end_col, path):
        path.append('RIGHT')
        return True
    if travel(grid, visited, row, col-1, end_row, end_col, path):
        path.append('LEFT')
        return True
    return False

def find_path(grid, start_row, start_col, end_row, end_col):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    path = []
    if travel(grid, visited, start_row, start_col, end_row, end_col, path):
        path.reverse()
        return path
    else:
        return '-_-'
