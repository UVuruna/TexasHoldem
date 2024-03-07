import deck
from decorator import Decorator

class Combinations:

    @staticmethod
    def RoyalFlushCombination_Create():
        Suits = [set() for _ in range(4)]
        for card in deck.CardsStrenght[-5:]:
            for i in range(4):
                Suits[i].add(f'{card}-{deck.SuitsNames[i]}')
        else:
            return Suits
    RoyalFlushCombination = RoyalFlushCombination_Create()



    def RoyalFlush(hand:set):
        for combination in Combinations.RoyalFlushCombination:
            if combination.issubset(hand):
                return True

    def StraightFlush():
        pass

    def Quads():
        pass

    def FullHouse():
        pass

    def Flush():
        pass

    def Straight():
        for i in range(len(deck.CardsStrenght)):
            if deck.CardsStrenght[i:i+5]:
                pass

    def Trips():
        pass

    def TwoPairs():
        pass

    def Pair():
        pass

    def HighCard():
        pass


if __name__=='__main__':
    print('CardsStrenght: ',deck.CardsStrenght)
    print('Suits: ',deck.SuitsNames)
    Deck = deck.DeckCreating()
    #print(Deck)

    Ruka = {'T-Spade','Q-Spade', 'J-Spade', 'A-Spade', 'K-Spade','6-Club', '6-Heart'}

    Combinations.RoyalFlush(Ruka)
    print(Combinations.RoyalFlush(Ruka))
    print(Ruka)