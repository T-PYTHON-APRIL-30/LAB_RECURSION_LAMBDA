'''LAB_RECURSION_LAMBDA
1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:
Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase .
Example: given the phrase I love python , it should return : 4
2) Given a list of numbers : [40,35, 10, 15, 20]
create a new list containing each number from the previous list mutliplied by itself.
print the new list.
Hint: use map() with a lambda funciton
'''
#Lab 1
def count_vowels(phrase:str)->int:
    
    if len(phrase) == 0 :
        return 0
    sum=0
    character:str= phrase[0]
    if character.lower() in "a,e,i,o,u":
        sum+=1
    result= sum+count_vowels(phrase[1:])
    return result

user_input = input("Please provide phrase: ")
result= count_vowels(user_input)
print(f"The count vowels: {result}")



#Lab 2
print("\n")
numbers = [40,35, 10, 15, 20]
print(f"The list: {numbers}")
new_list= map(lambda item: item*item ,numbers)
print(f"The new list: {list(new_list)}")