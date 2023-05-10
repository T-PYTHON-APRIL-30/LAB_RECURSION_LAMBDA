'''1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:
Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase .
Example: given the phrase I love python , it should return : 4'''


def vowels_counter (phrase:str) -> int:
    vowels = 'aouie'
    counter = 0

    if not phrase:
        return 0
    
    elif phrase[0].lower() in vowels:
        counter += 1
        return counter + vowels_counter(phrase[1:])
    
    else:
        return 0 + vowels_counter(phrase[1:])
    

    
    


sentence = "I Love Python"
print('The number of vowels letter in the sentence is: ',vowels_counter(sentence))



