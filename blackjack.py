##This is in the "art.py"
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""



#############################################################################



import random
import art

print(art.logo)
print("11 = ace, 10 = facecard")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(l):
    while sum(l) > 21:
        if 11 in l:
            l.remove(11)
            l.append(1)
        else:
            break
    score = sum(l)
    return score


user_cards = []
computer_cards = []
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

for k in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

print(user_cards)
# print(computer_cards)

print(calculate_score(user_cards))
# print(calculate_score(computer_cards))

play = True

while play:

    #I can put conditions to check here i think? resulting in below...idk i'm just trying to avoid nested if/else statements.
    #Looking back, I should have just set the condition of the loop as "While user_score <= 21"
    #Okay so I just tried the above but it broke some stuff... reverting back. IT WORKS DON'T MESS WITH IT ANYMORE JOSH!
  
    if user_score > 21:
        #I have no idea why in the output terminal it ouputs the score and cards before this line. I guess it finishes the loop but I still don't see how it works.
        #I was originally printing the score and card in the line below, but it ends up printing it twice for some reason...idk it works now so whatever!
        print(f"You bust! Game over!")
        play = False
        quit()

    hit = input("Would you like to hit? Y/N \n")

    if hit == "Y".lower() and user_score <= 21:
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards are {user_cards}, your score is {user_score}")

    else:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are {user_cards} your score is {user_score}")
        print(f"Dealer cards are {computer_cards}, dealer score {computer_score}")
        play = False

user_final = user_score - 21
computer_final = computer_score - 21

if computer_score > 21:
    print("Dealer Busts, you win!")
    quit()
elif user_score > 21:
    print("You bust, you lose!")
    quit()
elif user_final > computer_final and user_final <= 0:
    print("You win!")
    quit()
elif computer_final > user_final and computer_final <=0:
    print("Dealer Wins!")
    quit()
elif computer_final == user_final:
    print("It's a draw!")
else:
    print("Code Error, idk bro")

#Still just trying to figure out how things work. I was able to pretty much put this all together without a ton of clues.
#Proud of this one, even though parts are pretty much magic.
#As a side note, the logic here is pretty much for the dealer/computer to hit anytime the player hits. Which isn't necessarily the best option for the dealer. Whatever.
