print("---------- Q1 ----------")
def vowelsCounter(word:str) -> int :
    vowels = ["a","e","i","o","u"]
    count = 0 
    for char in word:
        if char in vowels:
            count+=1
    return count
userIput = input("Enter a phrase: ").lower()
print(f"the number of the vowels : \n{vowelsCounter(userIput)}")
print("---------- Q2 ----------")
firstList = [2,35, 10, 15, 20]
secondList = map(lambda num: num*num, firstList)
print(list(secondList))