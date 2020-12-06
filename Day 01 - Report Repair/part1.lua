--[[
  Day 01 - Report Repair
  ======================
  
  PART 1

  A script that reads in a set of numbers,
  determines which pair sums up to 2020,
  and multiplies them together.

  This script expects a text file containing
  integer values delineated by newline characters.
--]]

lines = {}
a = nil
b = nil

print("Reading in the file...")
for line in io.lines("input.txt") do
    lines[#lines + 1] = line
end
print("Done!")
print("")

print("Finding a sum of two that matches '2020'...")
for i = 1, #lines, 1 do
    for j = 1, #lines, 1 do
        if (lines[i] + lines[j] == 2020) then
            a = lines[i]
            b = lines[j]
            break
        end
    end
end
print("Done!")
print("")

if (a ~= nil and b ~= nil) then
    print("Sum found. Multiplication yields:")
    print(a*b)
else
    print("Did not find a sum that matches '2020'!")
end