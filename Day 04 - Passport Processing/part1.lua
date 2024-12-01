--[[
  Day 04 - Passport Processing
  ============================
  
  PART 1

  A script that reads in a set of strings which
  represent a passport entry. The script then
  determines the validity of the passport
  entries.

  This script expects a set of strings. Many
  passport fields can exist one one line, and
  many lines can comprise one passport unsorted.
  Passport unsorteds are delineated by a blank
  line.
--]]


-- Read the file in.
print("Reading in the file...")
lines = {}
for line in io.lines("input.txt") do
    lines[#lines + 1] = line
end
print("Done!\n")

-- Concatenate passport fields to one line.
print("Concatenating passport fields per object...")
unsorteds = {}
unsorted = ""
for i = 1, #lines+1 do
    if i == #lines+1 then
        unsorteds[#unsorteds + 1] = unsorted
        unsorted = ""
    elseif lines[i] ~= "" then
        unsorted = unsorted .. lines[i] .. ","
    else
        unsorteds[#unsorteds + 1] = unsorted
        unsorted = ""
    end
end
print("Done!\n")

print("Unsorteds count: " .. #unsorteds)

-- Tokenize passport fields.
print("Tokenizing passport fields...")
passports = {}
for i = 1, #unsorteds do
    k = 1
    passports[i] = {}
    for j = 1, #(unsorteds[i]) do
        if string.sub(unsorteds[i], j, j) == " " or string.sub(unsorteds[i], j, j) == "," then
            passports[i][#(passports[i]) + 1] = string.sub(unsorteds[i], k, j - 1)
            k = j + 1
        end
    end
end
print("Done!\n")

-- Sort passport field strings.
print("Sorting passport fields...")
for i = 1, #passports do
    for j = 1, #(passports[i]) do
        for k = j, #(passports[i]) do
            if passports[i][k] < passports[i][j] then
                local min = passports[i][k]
                local high = passports[i][j]
                passports[i][j] = min
                passports[i][k] = high
            end
        end
    end
end
print("Done!\n")

-- Determine which passports are valid.
print("Determining number of valid passports...")
valid_passports = 0
for i = 1, #passports do
    if #(passports[i]) == 7 then
        local contains_cid = false
        for j = 1, #(passports[i]) do
            if string.sub(passports[i][j], 1, 3) == "cid" then
                contains_cid = true
            end
        end
        if contains_cid == false then
            valid_passports = valid_passports + 1
        end
    elseif #(passports[i]) == 8 then
        valid_passports = valid_passports + 1
    end
end
print("Done!\n")

print("Total valid passports: " .. valid_passports)