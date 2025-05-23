"""Count the Vowels in a Word"""

def count__vowels(word):
    vowel = "aeiou"
    count = 0
    for letter in word.lower():
        if letter in vowel.lower():
            count += 1
    return count 

print(count__vowels("sbd"))
