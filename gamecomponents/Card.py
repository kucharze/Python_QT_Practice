 #A single playing card  
class Card :  #Instance variables
  #   suit: Suit of self card (String)
  #   value: Numeric or face value of self card (String)
  #   jackvalue, warvalue, svalue: value of card for given game

  def __init__ (self, aSuit, aValue):
      self.suit = aSuit
      self.value = aValue
      self.pixelOffset = 15
      self.flipped=False
      self.jackValue = 0
      self.sValue = 0
      self.warValue=0
      self.setValues(aValue)
  
    
  def setValues(self,aValue):#Used to set card values for use in certain games
    if(aValue=="k"):
      self.jackValue=10
      self.sValue=13
      self.warValue=13
    
    elif(aValue=="j"):
      self.jackValue=10
      self.sValue=11
      self.warValue=11
    
    elif(aValue=="q"):
      self.jackValue=10
      self.sValue=12
      self.warValue=12
    
    elif(aValue=="a"):
      self.jackValue=11
      self.sValue=1
      self.warValue=14

    else:
      self.jackValue=aValue
      self.sValue=aValue
      self.warValue=aValue
    
  
    
  def getSuit(self): return self.suit
  def getValue(self): return self.value; 
  def getSValue(self): return self.sValue
  def getJackValue(self): return self.jackValue
  def getWarValue(self): return self.warValue
    
  def flip(self):
    self.flipped = not self.flipped
  
   #Return a string representation of self card. 
  def toString(self):
    return self.value + self.suit
  
   #Return relative URL of self card (assumes certain folder structure).
  def getURL(self): 
    return "../Images/" + self.toString() + ".png"

   # Return relative URL of back of self (or any) card 
   # (assumes certain folder structure).
  def getBackURL(self):
    return "../Images/cardback.png"


# if (typeof module === "object") {
#  module.exports = Card;
# }