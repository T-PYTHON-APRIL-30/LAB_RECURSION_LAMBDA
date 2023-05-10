'''
## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase `I love python` , it should return : `4` 

'''

def count_vowels(word, idx=0):
    if idx == len(word):
        return 0
    s_lower = word[idx].lower()
    vowels = 'aeiou'
    count = 1 if s_lower in vowels else 0

    return count + count_vowels(word, idx + 1)
print(count_vowels("I love python "))

'''
 Given a list of numbers : [40,35, 10, 15, 20]
create a new list containing each number from the previous list mutliplied by itself.
print the new list.
Hint: use map() with a lambda funciton
'''

numbers = [40, 35, 10, 15, 20]

squared_numbers = list(map(lambda numb: numb * numb, numbers))

print(squared_numbers)
