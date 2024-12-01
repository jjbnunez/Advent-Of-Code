--[[
  Day 03 - Toboggan Trajectory
  ============================
  
  PART 1

  A script that reads in a set of strings which
  get interpreted as a game board. These strings
  comprise combinations of the '.' character and
  the '#' character. Each period represents an
  empty space, and each hashtag represents a
  collidable tree. We calculate a slope going
  "down the hill" to determine how many
  collisions occur.

  Note that the map wraps around horizontally by
  using modular arithmetic.
--]]


lines = {}
board = {}

-- Read in the file.
print("Reading in the file...")
for line in io.lines("input.txt") do
    lines[#lines + 1] = line
end
print("Done!\n")

-- Build the board as a matrix.
print("Building the board as a matrix...")
for i = 1, #lines do
    board[i] = {}
    for j = 1, #(lines[i]) do
        board[i][j] = string.sub(lines[i], j, j)
    end
end
print("Done!\n")

-- Test the matrix's fidelity against the
-- original lines.
print("Testing the matrix's fidelity...")
for i = 1, #lines do
    original = lines[i]
    rebuilt = ""
    for j = 1, #(board[i]) do
        rebuilt = rebuilt .. board[i][j] 
    end
    if original ~= rebuilt then
        print("ERROR: Rebuilt string did not match original.")
        print("\tOriginal: " .. original)
        print("\tRebuilt:  " .. rebuilt)
        os.exit(-1)
    end
end
print("Done!\n")

-- Count how many trees we run into.
print("Determining number of collisions...")
x = 1
y = 1
right = 1
down = 3
collisions = 0
for y = 1, #board, down do
    if board[y][x] == "#" then
        collisions = collisions + 1
    end
    x = x + right
    if x > #(board[y]) then
        x = x % #(board[y])
    end
end
print("Done!\n")

print("Total collisions: " .. collisions)