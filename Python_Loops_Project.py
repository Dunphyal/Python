#ask user for a sentence
original_sentence = input(" Please type a sentence: ").strip().lower()
#split sentence into words
words = original_sentence.split()
#loop through words and convert to pig latin
new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)

    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos += 1
            else:
                break
        consonants = word[:vowel_pos]
        remainder = word[vowel_pos:]
        new_word = remainder +consonants  + "ay"
        new_words.append(new_word)
        
        
    
#recombine words into a sentence
output_sentence = " ".join(new_words)

#output the sentence
print(output_sentence)
