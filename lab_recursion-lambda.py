
# Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) 
# are in that phrase or word:

vowels = "aeiou"

def count_vowels(pharse:str) ->int:

 if pharse == "":
   return 0 
 
 count = 0 
 if pharse[0].lower() in vowels:
    count = 1

    return 1 + count_vowels(pharse[1:])
  
    vowels_count = count_vowels ("I love python")
    print (vowels_count)
 

 



#Given a list of numbers : [40,35, 10, 15, 20]
#create a new list containing each number from the previous list mutliplied by itself.
#print the new list.
#Hint: use map() with a lambda funciton


numbers = [40, 35, 10, 15, 20]
squared_numbers = list(map(lambda x: x*x, numbers))
print (squared_numbers)

       

