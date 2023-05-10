def count_vowels(vowels:str) -> int:
    vowels = ["a","e","i","o","u"]
    count = 0
    vowels1 = count_vowels("My Name is juohaina Iam software engineer")
    for c in vowels:
        if c in vowels1:
         count+=1
    print(vowels1)
    return count_vowels