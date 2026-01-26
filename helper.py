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

def parseInput(filepath, hospitals, hQueue, students):
    with open(filepath, 'r') as input:
        lines = input.readlines()

    rows = []
    for line in lines:
        rows.append(line.strip())
    
    n = int(rows[0])

    for i in range(1, n + 1):
        preferences = []
        for c in range(n):
            preferences.append(int(rows[i][c]))
        hospitals[i] = preferences[:]
        hQueue.append(i)
    for i in range(n + 1, 2*n + 1):
        preferences = []
        for c in range(n):
            preferences.append(int(rows[i][c]))
        students[i-n] = preferences[:]
    return n
        