'''
# LAB_RECURSION_LAMBDA



## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase `I love python` , it should return : `4` 
'''
def count_vowel(word : str):
    found = 0
    if len(word) == 0:
        return found
    if word[0].lower() in "aeiuo":
        found = 1

    return found + count_vowel(word[1:])

print(count_vowel("I love python"))
'''

## 2) Given a list of numbers : `[40,35, 10, 15, 20]`

#### create a new list containing each number from the previous list mutliplied by itself.
#### print the new list.
#### Hint: use map() with a lambda funciton

'''
numbers = [40, 35, 10, 15, 20]
maping = list(map(lambda time: time*time, numbers))
print(maping)


