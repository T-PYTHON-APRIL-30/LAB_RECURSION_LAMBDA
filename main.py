def count_vowels(word):
    if len(word) == 0:
        return 0

    first_char = word[0].lower()

    if first_char in 'aeiou':
        return 1 + count_vowels(word[1:])
    else:
        return count_vowels(word[1:])

phrase = "I love python"
vowel_count = count_vowels(phrase)
print(vowel_count) 


numbers = [40, 35, 10, 15, 20]

squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)
