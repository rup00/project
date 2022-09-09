import random
print("welcome to word puzzle game")
name = input("What is your name ")
user=0
count=0
print("Good Luck ! ", name)
print("rule of game are :\n")
print("you score +1 for each correct answer and  -1 for each wrong answer")
print("\n")
print ("All the Best:",name)
#to choose randomly word from the list
def choose():
    words = ['MySirG','Father','clock','yummy','complete']
    pick = random.choice(words)
    return pick


#to arange words in ulta pulta 
def ulta(word):
    random_word = random.sample(word, len(word))
    jumbled = ''.join(random_word)
    return jumbled
 
while True:
    
    
        picked_word = choose()
 
        # jumble() function calling
        ulta_p = ulta(picked_word)
        print("Arrange the letters to form a valid word:", ulta_p)
        print("\n")
        ans=input("enter your answer:")
        if(ans==picked_word):
                      user+=1
                      print("right answer \n score=+1")
                      count+=1
        else:
            user-=1;
            print("wrong answer \n score=-1")
            count+=1
        if(count>4):
            break
            
        
print("total score is:",user)
if user>3:
    print("Well Played genius")
else:
    print("ohhh try next better ")

          
        
 
