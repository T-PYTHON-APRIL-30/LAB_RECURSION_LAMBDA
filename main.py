#Q1
def vowels_counter(phrases: str, indx = 0) -> int:
    counter = 0
    vowels = ["a", "e", "i", "o", "u"]

    if len(phrases) == indx:
        return counter
    

    phrase = phrases[indx].lower()
    if phrase in vowels:
        counter +=1
    
    return counter + vowels_counter(phrases, indx + 1)


print(vowels_counter("I love python"))

#Q2
list_numbers = [40, 35, 10, 15, 20]
new_list = map(lambda item: item*item, list_numbers)
print(list(new_list))