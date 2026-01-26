class Entity:

    def __init__(self, index, preferences):
        self.index = index
        self.preferences = preferences
        self.isMatched = False
        self.matchedTo = None
        

    # Potential helper methods

    # def match(self, other):
    #     self.isMatched = True
    #     self.matchedTo  = other.index
        
    #     other.isMatched = True
    #     other.matchedTo = self.index

    # def unmatch(self, other):
    #     self.isMatched = False
    #     self.matchedTo = None