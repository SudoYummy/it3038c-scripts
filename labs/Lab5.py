print("This program solves Problem 2")

##Defining variables
consonantsNum = 0
vowelsNum = 0
nonLetterNum = 0
consonants =["q", "w", "r", "t", "y", "p", "s", "d", "f","g", "h", "j", "k", "l", "z", "x", "c", "v", "b","n", "m"]
vowels= ["e", "u", "i", "o", "a"]

##Asking for user input
print("Please enter 1 word")
word=input()

for letter in word.lower():
    if letter in consonants:
        consonantsNum += 1
    elif letter in vowels:
        vowelsNum += 1
    else:
        nonLetterNum += 1

print("Number of vowels: " + str(vowelsNum) + "\nNumber of consonants: " + str(consonantsNum) + "\nNumber of non-letters: " + str(nonLetterNum))