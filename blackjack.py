import random


def draw_card():
    while(len(drawn_cards) != 52):
            card = random.randint(0,52)
            if not card in drawn_cards:
                drawn_cards.append(card)
                return card

def value(card):
    val = 0
    if "King" in card:
        val = 10
    elif "Queen" in card:
        val = 10
    elif "Jack" in card:
        val = 10
    elif "Ace" in card:
        val = 11
    else:
        val = int(card.split(" ", 1)[0])
    return val

def card_sum(card_tuple):
    value_tuple = ()
    for card in card_tuple:
        value_tuple = value_tuple + (value(card),)
    if "Ace" in card_tuple and sum(value_tuple)>21:
        return sum(value_tuple)-10
    return sum(value_tuple)
        

''' if you want to create continuous game - currently deck resets on compile
def clear(card_list):
    clear(drawn_cards)
    return drawn_cards
'''


card_order = []
drawn_cards = []
user_cards = ()
house_cards = ()

for i in range(1,5):
    suit = ''
    if i == 1:
        suit = " of Clubs"
    elif i == 2:
        suit = " of Diamonds"
    elif i == 3:
        suit = " of Hearts"
    elif i ==4:
        suit = " of Spades"
        
    for j in range(1,14):
        if j == 1:
            j = "Ace"
        elif j == 11:
            j = "Jack"
        elif j == 12:
            j = "Queen"
        elif j ==13:
            j = "King"
        j = str(j) + suit
        card_order.append(j)

hit_or_stand = ""
draw_card()
print("You were dealt a", card_order[drawn_cards[0]])
user_cards = user_cards + (card_order[drawn_cards[0]],)
draw_card()
house_cards = house_cards + (card_order[drawn_cards[1]],)
draw_card()
print("You were dealt a", card_order[drawn_cards[2]])
user_cards = user_cards + (card_order[drawn_cards[2]],)
draw_card()
house_cards = house_cards + (card_order[drawn_cards[3]],)
print("The dealer has a", card_order[drawn_cards[3]], "(", value(card_order[drawn_cards[3]]),")")  
print("You have a", card_order[drawn_cards[0]], "(", value(card_order[drawn_cards[0]]), ")"
      "and a" , card_order[drawn_cards[2]], "(", value(card_order[drawn_cards[2]]), ")")

cards = 3

game = True

while(game):
    if((card_sum(user_cards) > 17 and card_sum(user_cards) < 21) and card_sum(user_cards) == card_sum(house_cards)):
        print("You have the same sum as the dealer. You are tied")
        game = False
        break
    if(card_sum(user_cards) == 21):
        while(card_sum(house_cards)<17):
            draw_card()
            cards+=1
            house_cards = house_cards + (card_order[drawn_cards[cards]],)
            print("The dealer drew a", card_order[drawn_cards[cards]], "and has a total of", card_sum(house_cards))
            if(card_sum(house_cards)>21):
                print("The dealer busted. You won")
                game = False
                break
            elif(card_sum==21):
                print("Dealer also has 21. It is a tie")
                game = False
                break
    hit_or_stand = input("Hit or stand? ")
    if hit_or_stand.lower() == "hit":
        draw_card()
        cards+=1
        user_cards = user_cards + (card_order[drawn_cards[cards]],)
        print("You were drawn a", card_order[drawn_cards[cards]], "You now have a total of" , card_sum(user_cards))
        if(card_sum(user_cards)>21):
            card_sum(user_cards)
            if(card_sum(user_cards)<21):
                continue
            print("You busted. The house wins")
            game = False
    else:
        print("The dealer has a", card_order[drawn_cards[1]], "(", value(card_order[drawn_cards[1]]), ") "
          "and a" , card_order[drawn_cards[3]], "(", value(card_order[drawn_cards[3]]), ") for a total of ", card_sum(house_cards))
        if card_sum(house_cards)>=17 and card_sum(house_cards)<=21:
            if card_sum(house_cards) > card_sum(user_cards):
                print("The dealer won.")
                game = False
            elif card_sum(house_cards) < card_sum(user_cards):
                print("You won.")
                game = False
            else:
                print("You tied")
                game = False
        if card_sum(house_cards) == 21 and card_sum(user_cards)<21:
            print("The dealer has 21. The house wins")
            game = False            
        while(card_sum(house_cards)<17):
            draw_card()
            cards+=1
            house_cards = house_cards + (card_order[drawn_cards[cards]],)
            print("The dealer drew a", card_order[drawn_cards[cards]], "for a total of", card_sum(house_cards))
            if(card_sum(house_cards)>21):
                print("The dealer busted. You won")
                game = False
            elif(card_sum(house_cards)<=21 and card_sum(house_cards)>=17):
                if(card_sum(house_cards)>card_sum(user_cards)):
                    print("The dealer won.")
                    game = False
                elif(card_sum(house_cards)<card_sum(user_cards)):
                    print("You won")
                    game = False

