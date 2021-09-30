#Problem set 2d
#Name: Aastha Gupta
#Time Spent: 5 hours

import random
                    
 
name = input("आपका नाम क्या है? ")
 
print("नमस्ते ! ", name)
print("शुभकामनाएं....")
 
words = ['computer', 'engineer', 'science', 'hindi','python', 'mathematics', 'data', 'condition','aastha', 'water', 
        'gupta']
 

                              
word = random.choice(words)        
 
 
print("पात्रों का अनुमान लगाए")
 
guesses = ''
 
                
turns = 12              
 
 
while turns > 0:
     
                        
    failed = 0
     
                         
    for char in word:
         
                                
        if char in guesses:
            print(char)
             
        else:
            print("_")
             
                            
            failed += 1
             
 
    if failed == 0:
                            
        print("आप जीतते हैं")
         

        print("The word is: ", word)
        break
    guess = input("पात्रों का अनुमान लगाए:")
    guesses += guess
    if guess not in word: 
        turns -= 1
        print("गलत")
         
        
        print("You have", + turns, 'more guesses')
         
