from decorator import Decorator
from Combinations import Combinations
import deck


class PokerHand(Combinations):
    def __init__(self,hand) -> None:
        self.hand = hand
        self.number = []
        self.Spade = 0
        self.Diamond = 0
        self.Club = 0
        self.Heart = 0
        for card in hand:
            self.number.append(card[0])
            setattr(self,f'{card[2:]}',getattr(self,f'{card[2:]}')+1)

    def CheckingCombinations(self):
        for suit in deck.SuitsNames:
            if getattr(self,f'{suit}') >=5:
                # Flush
                pass
        
        straight = set(self.number)
        if len(straight)>=5:
            for i in range(1,10):
                if set(deck.CardsStrenght[i:i+5]).issubset(straight):
                    # Straight
                    pass
            else:
                if set(deck.CardsStrenght[:4],deck.CardsStrenght[-1]).issubset(straight):
                    # Straight
                        pass

        # IF Flush and Straight  possible ROyal and Str8Flush
           