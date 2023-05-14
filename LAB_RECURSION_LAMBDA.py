'''
1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u)
are in that phrase or word:
Note: the function should be able to count how many vowels no matter
if it is lowercase or uppercase 



Given a list of numbers : [40,35, 10, 15, 20]
create a new list containing each number
from the previous list mutliplied by itself.
'''
number= [40,35, 10, 15, 20]

number = map(lambda item:item*item, number)

print(list(number))

print("--"*14)

def count_vowel(word : str):
    count = 0
    if len(word) == 0:
        return count
    if word[0].lower() in "aeiuo":
        count = 1

    return count + count_vowel(word[1:])

print(count_vowel("I love python"))