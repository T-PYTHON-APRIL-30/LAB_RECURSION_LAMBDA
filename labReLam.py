import operator
def counting_vowels_in_a_string(phrase:str) -> int:
    vowels = ['a','e','i','o','u']
    if len(phrase) == 0:
        return 0
    else:

        if phrase[0].lower() in vowels:
            return 1 + counting_vowels_in_a_string(phrase[1:])
        else:
            return 0 + counting_vowels_in_a_string(phrase[1:])


print(counting_vowels_in_a_string("I LOVE PYTHON"))




list1 = [40,35,10,15,20]
multiply_lambda = list(map(lambda x:x*2, list1))
print(multiply_lambda)