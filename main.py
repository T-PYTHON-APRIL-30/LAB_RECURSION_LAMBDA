'''
1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:
Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase .
Example: given the phrase I love python , it should return : 4
'''
#How to transform this to a recursive function
def vowels_counter(phrase :str) -> int:
    lower_phrase = phrase.lower()
    count = 0
    vowels = ["a","e","i","o","u"]
    for char in range(len(lower_phrase)):
        if lower_phrase[char] in vowels:
            count += 1
    return count
    
  

phrase= input("Enter a Word/Phrase to count the vowels:")
print(vowels_counter(phrase))


'''
2) Given a list of numbers : [40,35, 10, 15, 20]
create a new list containing each number from the previous list mutliplied by itself.
print the new list.
Hint: use map() with a lambda funciton
'''
numbers_list = [40,35, 10, 15, 20]
new_numbers_list = map(lambda number : number * number , numbers_list)
print(list(new_numbers_list))