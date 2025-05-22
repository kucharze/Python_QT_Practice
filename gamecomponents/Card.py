 #A single playing card  
class Card :  #Instance variables
  #   suit: Suit of this card (String)
  #   value: Numeric or face value of this card (String)
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
      this.jackValue=10;
      this.sValue=13;
      this.warValue=13;
    }
    else if(aValue=="j"){
      this.jackValue=10;
      this.sValue=11;
      this.warValue=11;
    }
    else if(aValue=="q"){
      this.jackValue=10;
      this.sValue=12;
      this.warValue=12;
    }
    else if(aValue=="a"){
      this.jackValue=11;
      this.sValue=1;
      this.warValue=14;
    }
    else{
      this.jackValue=aValue;
      this.sValue=aValue;
      this.warValue=aValue;
    }
  }
    
  getSuit() { return this.suit; }
  getValue() { return this.value; }
  getSValue(){return this.sValue;}
  getJackValue(){return this.jackValue;}
  getWarValue(){return this.warValue;}
    
  flip(){
    this.flipped=!this.flipped;
  }
  /**
   * Return a string representation of this card.
   */
  toString() {
    return this.value + this.suit ;
  }
  /**
   * Return relative URL of this card (assumes certain folder structure).
   */
  getURL() { 
    return "../Images/" + this.toString() + ".png";
  }
  /**
   * Return relative URL of back of this (or any) card 
   * (assumes certain folder structure).
   */
  getBackURL() { 
    return "../Images/cardback.png";
  }
}

if (typeof module === "object") {
 module.exports = Card;
}