import random
from decorator import Decorator

Suits = ['♠','♦','♣','♥']
SuitsNames = ['Spade','Diamond','Club','Heart']
FaceCards = ['T','J','Q','K','A']

@Decorator.countExecutionMethod
def CardsStrenghtOrder():
    Cards=[]
    for i in range(2,10):
        Cards.append(str(i))
    for i in FaceCards:
        Cards.append(i)
    return Cards
CardsStrenght = CardsStrenghtOrder()

def DeckCreating(Znakovi=False):
    Karte = []
    def znakovi(card):
        if Znakovi is True:
            for i in Suits:
                Karte.append(f'{card}{i}')
        else:
            for i in SuitsNames:
                Karte.append(f'{card}-{i}')
    for i in range(2,10):
        znakovi(i)
    for i in FaceCards:
        znakovi(i)
    return Karte
        
def CardDrawing(Deck):
    karta = random.choice(Deck)
    Deck.remove(karta)
    return karta

if __name__=='__main__':
    print(CardsStrenght)
    Deck = DeckCreating(FaceCards)
    karta1 = CardDrawing(Deck)
    karta2 = CardDrawing(Deck)

    # ovde ce bacati povremenu gresku zbog 10 koji se sastoji od 2 cifre a on ce traziti 1 koga nema u listi
    print(f'karta1 {karta1} se nalazi na poziciji {CardsStrenght.index(karta1[0])} u JaciniKarata')

    print(karta1,karta2)
    print(Deck,len(Deck))
    
    '''with open('Spil.txt','w') as f:
            for i in range(len(Spil)):
                f.write(f'{Spil[i]} ') if (i+1)%4!=0 else f.write(f'{Spil[i]}\n')'''
    
