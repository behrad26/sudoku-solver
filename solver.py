def check(grid, row, col, num):
	if num in grid[row]: return False
	for row_index in range(0, 9):
		if grid[row_index][col] == num: return False
	for row_index in range(0, 3):
		for col_index in range(0, 3):
			if grid[row_index + row // 3 * 3][col_index + col // 3 * 3] == num: return False
	return True

def solve(grid, row, col):
	if row == 9 - 1 and col == 9: return True
	if col == 9: row, col = row + 1, 0
	if grid[row][col] > 0: return solve(grid, row, col + 1)
	for num in range(1, 10):
		if check(grid, row, col, num):
			grid[row][col] = num
			if solve(grid, row, col + 1): return True
	grid[row][col] = 0

grid = [input() for _ in range(0, 9)]
if str(grid).count(" ") >= 72: grid = [list(map(int, grid[i].split())) for i in range(0, 9)]
else: grid = [list(map(int, grid[i].replace(" ", ""))) for i in range(0, 9)]
solve(grid, 0, 0)
print("\n")
for i in range(9): print(" ".join(list(map(str, grid[i]))))