print("---------- Q1 ----------")
vowels = ["a","e","i","o","u"]
count = 0 
count_vol = 0 

def vowelsCounter(word:str):
    if word=="":
        return 0
    if word[-1].lower() in vowels:
        tot_vol= 1 + vowelsCounter(word[:len(word)-1])
        return tot_vol
    else:
        decrmentWord=vowelsCounter(word[:len(word)-1])
        return decrmentWord

userIput = input("Enter a phrase: ").lower()
print(f"the number of the vowels : \n{vowelsCounter(userIput)}")
print("---------- Q2 ----------")
firstList = [2,35, 10, 15, 20]
secondList = map(lambda num: num*num, firstList)
print(list(secondList))