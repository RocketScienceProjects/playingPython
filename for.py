
vowel = 0
consonant = 0
word = input("enter a word of your choice: ").strip().lower()  #example that string are iterable in python
for letter in word:
    if letter in "aeiou":
        vowel = vowel + 1
    elif letter == " ":
        print("its a blank space")
    else:
        consonant = consonant + 1

print("there are {} vowels in the word '{}'".format(vowel, word))
print("There are {} consonants in the word '{}'".format(consonant, word))
