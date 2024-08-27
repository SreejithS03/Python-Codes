def char_frequency(s):
    frequency ={}                  
    for char in s:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
    return frequency
test_string="programming"
result = char_frequency(test_string)
print("Character frequency dictionary")
print(result)