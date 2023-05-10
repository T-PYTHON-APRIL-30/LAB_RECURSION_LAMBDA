#1_______________________________________________________________
count = 0
def vowels_count (check:str)->str:
    global count
    check = check.lower()
    leave = len(check)
    if leave == 0:
        return 0
    vowel = ("a","e","i","o","u")
    vowels_count(check[:-1])
    if check.endswith(vowel):
        count+=1
    return count
    
total = vowels_count("I love python")
print(total)

#1 in normal loop________________________________________________
def vowels_count (check:str)->str:
    check = check.lower()
    count = 0
    vowel = ("a","e","i","o","u")
    for i in check:
        if i.endswith(vowel):
            count+=1
    print(count)
vowels_count("I love python")

#2_______________________________________________________________
lst:int = [40,35, 10, 15, 20]
def lst_square (square):
    final_list = list(map(lambda void : void*void,square))
    print(final_list)

lst_square(lst)