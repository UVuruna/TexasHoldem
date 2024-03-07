import deck

Deck = deck.DeckCreating()
print(Deck)
print('------')
for i in range(20):
    print(deck.CardDrawing(Deck),end=' ')
print(len(Deck))