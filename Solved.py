#First question
def count_vowles(word:str):
    
    vowles = ("aeiouAEIOU")

    if not word:
        return 0

    count =(1 if word[0] in vowles else 0) + count_vowles(word[1:])
    return count


print(count_vowles(input("Enter a word or phrase to count vowles... ")))
    
#Second question
Numbers = [40,35, 10, 15, 20]

new_numbers = map(lambda n: n * n , Numbers )

print(list(new_numbers))

