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
    
  
    
  getSuit() { return self.suit; }
  getValue() { return self.value; }
  getSValue(){return self.sValue;}
  getJackValue(){return self.jackValue;}
  getWarValue(){return self.warValue;}
    
  flip(){
    self.flipped=!self.flipped;
  }
  /**
   * Return a string representation of self card.
   */
  toString() {
    return self.value + self.suit ;
  }
  /**
   * Return relative URL of self card (assumes certain folder structure).
   */
  getURL() { 
    return "../Images/" + self.toString() + ".png";
  }
  /**
   * Return relative URL of back of self (or any) card 
   * (assumes certain folder structure).
   */
  getBackURL() { 
    return "../Images/cardback.png";
  }
}

# if (typeof module === "object") {
#  module.exports = Card;
# }