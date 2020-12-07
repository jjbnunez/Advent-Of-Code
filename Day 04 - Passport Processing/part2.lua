--[[
  Day 04 - Passport Processing
  ============================
  
  PART 2

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


dofile("mylib.lua")


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
    if hasValidKeys(passports[i]) == true then
        is_valid = true
        for j = 1, #(passports[i]) do
            key_val = passports[i][j]
            key = string.sub(key_val, 1, 3)
            if is_valid == true and key == "byr" then 
                is_valid = isValidByr(key_val)
            elseif is_valid == true and key == "iyr" then
                is_valid = isValidIyr(key_val)
            elseif is_valid == true and key == "eyr" then
                is_valid = isValidEyr(key_val)
            elseif is_valid == true and key == "hgt" then
                is_valid = isValidHgt(key_val)
            elseif is_valid == true and key == "hcl" then
                is_valid = isValidHcl(key_val)
            elseif is_valid == true and key == "ecl" then
                is_valid = isValidEcl(key_val)
            elseif is_valid == true and key == "pid" then
                is_valid = isValidPid(key_val)
            end
        end
        if is_valid == true then valid_passports = valid_passports + 1 end
    end
end

print("Total valid passports: " .. valid_passports)