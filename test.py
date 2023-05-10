def count_vowels(charachter:str) -> int :
    vowels = ["a","e","i","o","u"]
    count = 0 
    for char in charachter:
        if char in vowels:
            count+=1
    return count ,count_vowels
vowels1 = count_vowels("My Name is juohaina Iam software engineer")
print(f"umber of the vowels :" , vowels1)