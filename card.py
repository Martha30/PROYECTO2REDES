class Card:
    def __init__(self, typeC = "cartas", number = 0, special_ability = None):
        self.typeC = typeC
        self.number = number
        self.special_ability = special_ability
        
    def __str__(self):
        return f"{self.get_card_text()} - {self.typeC}"
    
    def __repr__(self):
        return f"{self.get_card_text()} - {self.typeC}"
    
    def get_card_text(self):
        if self.number == 0:
            return self.special_ability
        else:
            return self.number
    
        
        
