function getSubstringPast4(str_input)
    
    return string.sub(str_input, 5)
end


function isDecDigit(char_input)

    dec_digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    
    for i = 1, #dec_digits do
        if char_input == dec_digits[i] then
            return true
        end
    end

    return false
end


function isHexDigit(char_input)
    
    hex_digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"}
    
    for i = 1, #hex_digits do
        if char_input == hex_digits[i] then
            return true
        end
    end

    return false
end


function hasValidKeys(passport)

    field_names  = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    field_exists = {false, false, false, false, false, false, false, false}

    if (#passport < 7) then
        return false
    end

    for i = 1, #passport do
        for j = 1, #field_names do
            if string.sub(passport[i], 1, 3) == field_names[j] then
                field_exists[j] = true
            end
        end
    end

    for i = 1, #field_exists do
        if field_exists[i] == false and i ~= 8 then
            return false
        end
    end

    return true
end


function getKeyEnum(key_val)

    key = string.sub(key_val, 1, 3)

    if key == "byr" then return 1 end
    if key == "iyr" then return 2 end
    if key == "eyr" then return 3 end
    if key == "hgt" then return 4 end
    if key == "hcl" then return 5 end
    if key == "ecl" then return 6 end
    if key == "pid" then return 7 end
    if key == "cid" then return 8 end

    return -1
end


function isValidByr(key_val)

    val = tonumber(string.sub(key_val, 5))

    if val >= 1920 and val <= 2002 then
        return true
    else
        return false
    end
end


function isValidIyr(key_val)

    val = tonumber(string.sub(key_val, 5))

    if val >= 2010 and val <= 2020 then
        return true
    else
        return false
    end
end


function isValidEyr(key_val)
    
    val = tonumber(string.sub(key_val, 5))

    if val >= 2020 and val <= 2030 then
        return true
    else
        return false
    end
end


function isValidHgt(key_val)
    
    val = string.sub(key_val, 5)
    num = tonumber(string.sub(val, 1, #val-2))
    unit = string.sub(val, #val-1)

    if unit == "cm" and num >= 150 and num <= 193 then
        return true
    elseif unit == "in" and num >= 59 and num <= 76 then
        return true
    else
        return false
    end
end


function isValidHcl(key_val)

    val = string.sub(key_val, 5)

    if string.len(val) ~= 7 then
        return false
    else
        for i = 1, string.len(val) do
            char = string.sub(val, i, i)
            if i == 1 and char ~= "#" then
                return false
            elseif i ~= 1 and isHexDigit(char) == false then
                return false
            end
        end
    end

    return true
end


function isValidEcl(key_val)

    val = string.sub(key_val, 5)
    colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    for i = 1, #colors do
        if val == colors[i] then
            return true
        end
    end

    return false
end


function isValidPid(key_val)

    val = string.sub(key_val, 5)
    digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

    if #val ~= 9 then
        return false
    else
        for i = 1, #val do
            char = string.sub(val, i, i)
            if isDecDigit(char) == false then
                return false
            end
        end
    end

    return true
end