count_vowels=0
count=0
vowels=['a','e','i','u','o']


def vowels_recursion(word:str):

    if word=="":
        return 0
    
    if word[-1].lower() in vowels:
        total_vowels=1+vowels_recursion(word[:len(word)-1])
        return total_vowels
    else:
        decrment_the_word=vowels_recursion(word[:len(word)-1])

        return decrment_the_word

print(vowels_recursion("I love python"))

#-------------------------------------------

list1=[40,35, 10, 15, 20]
new_list=list(map(lambda mutliply_list:mutliply_list*mutliply_list,list1))
print(new_list)
