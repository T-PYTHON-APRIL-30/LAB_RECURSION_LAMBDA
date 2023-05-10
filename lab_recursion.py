# LAB_RECURSION_LAMBDA


# 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:
def print_vowels(phrase: str):
    vowels = "aeiouAEIOU"
    if phrase == "":
        return 0
    elif phrase[0] in vowels:
        return 1 + print_vowels(phrase[1:])
    else:
        return print_vowels(phrase[1:])


phrase = "I love python"
print("the number of vowels in this phrase is: ",print_vowels(phrase))

# 2) Given a list of numbers : `[40,35, 10, 15, 20]`
my_list = [40, 35, 10, 15, 20]

new_list = list(map(lambda element:  element*element, my_list))
print("the new list is: ")
print(new_list)
