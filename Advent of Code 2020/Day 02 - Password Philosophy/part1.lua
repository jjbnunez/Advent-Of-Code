--[[
  Day 02 - Password Philosophy
  ============================
  
  PART 1

  A script that reads in a set of strings. These
  strings contain data about what is expected and
  what there actually is. This script determines
  whether or not each line of data conforms to
  its expected format.

  This script expects a text file containing
  two integer values separated by a hyphen,
  followed by a single expected character,
  followed by a colon, and then a string of
  lowercase letters.
--]]

-- Define our tables and our return value.
lines = {}
lower_limits = {}
upper_limits = {}
expected_chars = {}
passwords = {}
actual_chars = {}
total_valid_passwords = nil

-- Read in the file.
print("Reading in the file...")
for line in io.lines("input.txt") do
    lines[#lines+1] = line
end
print("Done!\n")

-- Break up the lines into parts.
print("Parsing the strings...")
for i = 1, #lines, 1 do
    local hyphen_start, hyphen_stop = string.find(lines[i], "-")
    local space_start, space_stop = string.find(lines[i], " ")
    local colon_start, colon_stop = string.find(lines[i], ":")
    lower_limits[i] = tonumber(string.sub(lines[i], 1, hyphen_start-1))
    upper_limits[i] = tonumber(string.sub(lines[i], hyphen_start+1, space_start-1))
    expected_chars[i] = string.sub(lines[i], space_start+1, colon_start-1)
    passwords[i] = string.sub(lines[i], colon_start+2)
end
print("Done!\n")

-- Runtime unit test to ensure integrity of values.
print("Checking rebuilt strings' integrity...")
for i = 1, #lines, 1 do
    local original = lines[i]
    local rebuilt = lower_limits[i] .. "-" ..
            upper_limits[i] .. " " ..
            expected_chars[i] .. ": " ..
            passwords[i]
    if original ~= rebuilt then
        print("ERROR: Rebuilt string did not match original.")
        print("\tOriginal: " .. original)
        print("\tRebuilt:  " .. rebuilt)
        os.exit(-1)
    end
end
print("Done!\n")

-- Collect the actual count of the expected character.
print("Collecting actual counts per line...")
for i = 1, #lines, 1 do
    actual_chars[i] = 0
    for j = 1, string.len(passwords[i]), 1 do
        if expected_chars[i] == string.sub(passwords[i], j, j) then
            actual_chars[i] = actual_chars[i] + 1
        end
    end
end
print("Done!\n")

-- Determine the number of valid passwords.
print("Determining the number of valid passwords...")
total_valid_passwords = 0;
for i = 1, #lines, 1 do
    if actual_chars[i] >= lower_limits[i] and actual_chars[i] <= upper_limits[i] then
        total_valid_passwords = total_valid_passwords + 1
    end
end
print("Done!\n")

-- Display total number of valid passwords.
print("Total valid passwords: " .. total_valid_passwords)