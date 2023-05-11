'''LAB_RECURSION_LAMBDA
1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase .

Example: given the phrase I love python , it should return : 4


2) Given a list of numbers : [40,35, 10, 15, 20]
create a new list containing each number from the previous list mutliplied by itself.
print the new list.
Hint: use map() with a lambda funciton

'''
sentence=input("please give me your sentense")
def NumOfVowels(sentence):
    senLen=len(sentence)
    for i in sentence:
        if i=="a"or i=="e" or i=="i" or i=="o" or i=="u":
            for i in senLen:
                i=+1
                vowelNum=i
                return vowelNum+NumOfVowels()
        else:
            continue

print(f"given the phrase{sentence},have{NumOfVowels}")

'''2) Given a list of numbers : [40,35, 10, 15, 20]
create a new list containing each number from the previous list mutliplied by itself.
print the new list.

Hint: use map() with a lambda funciton
'''

ListOfNum=[40,35, 10, 15, 20]
def Dupplicate(ListOfNum):
        return ListOfNum*ListOfNum
nums=map(Dupplicate,ListOfNum,ListOfNum)  
print(list(nums))

#define a lambda function

multiply_numbers = lambda ListOfNum: ListOfNum*ListOfNum
print(multiply_numbers)




   

