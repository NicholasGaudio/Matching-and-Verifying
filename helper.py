from pathlib import Path

class Entity:

    def __init__(self, index, preferences):
        self.index = index
        self.preferences = preferences
        self.isMatched = False
        self.matchedTo = None
        

    # Potential helper methods
    def match(self, other):
        self.isMatched = True
        self.matchedTo  = other
        
        other.isMatched = True
        other.matchedTo = self

    def unmatch(self):
        self.isMatched = False
        self.matchedTo = None

# Takes input file and converts it into Entity objects that are placed into a Hospital Map and Student Map respectively
# Also adds all hospital Entities to the hQueue and stores the number of Hospitals/Students for output formatting
def parseInput(filepath, hospitals, hQueue, students):
    with open(filepath, 'r') as input:
        lines = input.readlines()

    rows = []
    for line in lines:
        rows.append(line.strip().split())
    n = int(rows[0][0])

    for i in range(1, n + 1):
        preferences = []
        for c in range(n):
            preferences.append(int(rows[i][c]))
        h = Entity(i, preferences[:])
        hospitals[h.index] = h
        hQueue.append(h)
        
    for i in range(n + 1, 2*n + 1):
        preferences = []
        for c in range(n):
            preferences.append(int(rows[i][c]))
        s = Entity(i-n, preferences[:])
        students[s.index] = s
    return n

# Takes output file and sets correct matches between Hospital and Student Entities
# Verifies correct formatting of output file
def parseOutput(filepath, hospitals, students, n):
    with open(filepath, 'r') as input:
        lines = input.readlines()

    # Verify correct number of lines
    if len(lines) != n:
        return False
    
    rows = []
    for line in lines:
        rows.append(line.strip().split())
        
    for i in range(0, n):
        
        # Verify only 2 entries per line
        if len(rows[i]) != 2:
            return False
        
        # Match
        h = hospitals[int(rows[i][0])]
        s = students[int(rows[i][1])]
        h.match(s)

    return n


# Implementation of the Gale-Shapely algorithm
# Goes through a queue of hospitals matching them to students based off of the algorithms criteria
# Any unmatched hospital is added back into the queue for later
def match(hQueue, students):
    while len(hQueue) != 0:
        curHos = hQueue[0]
        for index in curHos.preferences:
            breaker = False
            choice = students[index]
            if choice.isMatched != True:
                curHos.match(choice)
                break
            else:
                other = choice.matchedTo
                for pref in choice.preferences:
                    if pref == other.index:
                        break
                    if pref == choice.index:
                        other.unmatch()
                        hQueue.append(other)
                        curHos.match(choice)
                        breaker = True
                        break
            if breaker:
                break
        hQueue.pop(0)
    return

# This formats the output for matching using the G-S algorithm
# It will generate a new numbered file each time 
def matchOuput(hospitals, n, rootPath):
    filepath = Path("")
    i = 0
    while True:
        filepath = Path(rootPath + "\output_" + str(i) + ".txt")
        if not filepath.is_file():
            break
        else:
            i += 1

    with open(filepath, "x") as file:
        for i in range(1, 1 + n):
            file.write(str(i) + " " + str(hospitals[i].matchedTo.index) + "\n")
    return
    