# Question 16(a)
# Examination Number:

# function definition used in part (v)
def is_anagram(w1, w2):
    if sorted(w1) == sorted(w2):
        return True
    else:
        return False

word1 = input("Enter the first word: ")
#part(i)
word2 = input("Enter the second word: ")

# test whether the sorted strings are the same as each other
# if the sorted strings are the same then they must be anagrams
#part(iv)
if (sorted(word1.upper()) == sorted(word2.upper())):
#part(ii)
    print(word1, "is an anagram of", word2)
#part(iii)
else:
    print(word1, "is not an anagram of", word2)
    
#part(v)
if (is_anagram(word1.upper(), word2.upper())) is True:
    print(word1, "is an anagram of", word2)
else:
    print(word1, "is not an anagram of", word2)
    
    
#part vi
phrase=input("Please enter a phrase: ")
phrase_nospace=phrase.replace(" ", "")
print(phrase_nospace)


if (sorted(phrase_nospace.upper()) == sorted(word1.upper())):
    print(phrase, "is an anagram of", word1)
else:
    print(phrase, "is not an anagram of", word1)

if (sorted(phrase_nospace.upper()) == sorted(word2.upper())):
    print(phrase, "is an anagram of", word2)
else:
    print(phrase, "is not an anagram of", word2)
