#get a sentence from the user
sentence = input("Enter a sentence to convert: ").strip().lower()

#split the words
words = sentence.split()

#loop & convert to pig latin
new_words = []

for w in words:
    if w[0] in 'aeiou':
        new_words.append(w + 'yay')
    else:
        index = 0
        for letter in w:
            if letter not in 'aeiou':
                index = index + 1
            else:
                break
        new_words.append(w[index:] + w[:index] + 'ay')



#concatenate the words

pig_latin = " ".join(new_words)


#print
print(pig_latin)
