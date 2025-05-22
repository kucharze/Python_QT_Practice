#Deck of playing cards.
import math
# const Card = require("./Card");
class Deck:
  # Instance variable:
  #   list: Deck of cards (array of Card objects)

   # Initialize deck to represent regular 52 playing cards.
  def __init__(self):
    self.list = []
    suit = ["c", "d", "h", "s"]
    value = [
      "2",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8",
      "9",
      "10",
      "j",
      "q",
      "k",
      "a",
    ]
    for i in range(len(suit)): #(let i = 0; i < suit.length; i++):
     
      for j in range(len(value)): # (let j = 0; j < value.length; j++):
        # self.list.push(new Card(suit[i], value[j]));
        pass
      
    
  
   # Shuffle the deck.
  def shuffle(self):
    #change logic to fit js loop
    for n in range(len(self.list)): 
      # (let n = self.list.length; n >= 2; n--) :
      r = math.floor(math.random() * n)
      # Swap cards at r and n-1
      card = self.list[r]
      self.list[r] = self.list[n - 1]
      self.list[n - 1] = card
    
    

   # Remove top card from the deck and return it.
  def dealACard(self):
    return self.list.shift();
  

  def getSize(self):
    return self.list.length;


   # Determines if the deck is empty.
  def isEmpty(self):
    return self.list.length == 0;
  
   # Adds a card to the deck.
  def addACard(self,card):
    self.list.push(card);
  
  
   # Indicate whether or not top card of deck is an 8.
   # self method is intended to be used only during game
   # initialization to avoid starting the pile with an 8.
  def isTopCardAnEight(self):
    return self.list[0].getValue() == "8";
  

# if (typeof module === "object") {
#   module.exports = Deck;
# }
