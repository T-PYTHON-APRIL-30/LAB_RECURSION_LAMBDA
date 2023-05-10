
# Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) 
# are in that phrase or word:
def count_vowels(word):
 
#base case:

 if the word is empty,
 return 0 
 if len(word) ==0:
  return 0
 
 #recursive case : countthe vowels in the rest of the word and add 1 if the first letter is vowel
 rest_count = count_vowels(word[1:])
 if word[0] in "aeiouAEIOU":
   return rest_count+1
 else:
  return rest_count
 
 #to use this function, simply call it with a string argument 

 word = "Hello, World!"
 num_vowels = count_vowels(word)
 print("ther are", num_vowels, "vowels in", word)



#Given a list of numbers : [40,35, 10, 15, 20]
#create a new list containing each number from the previous list mutliplied by itself.
#print the new list.
#Hint: use map() with a lambda funciton


numbers = [40, 35, 10, 15, 20]
squared_numbers = list(map(lambda x: x*x, numbers))
print (squared_numbers)

       

