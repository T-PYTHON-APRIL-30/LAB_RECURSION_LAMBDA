'''
1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:
Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase .
Example: given the phrase I love python , it should return : 4
'''
def vowels_counter(phrase :str) -> int:
    vowels = "aeiou"

    if len(phrase) == 0:
        return 0

    if phrase[0].lower() in vowels:
        return 1 + vowels_counter(phrase[1:])
    return 0 +  vowels_counter(phrase[1:])

def vowel_count(phrase):
    pass
  

phrase= "I love python"
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