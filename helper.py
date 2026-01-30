from pathlib import Path
import random

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

    if (len(rows) == 0 or len(rows[0]) != 1):
        return -1
    try:
        n = int(rows[0][0])
    except ValueError:
        return -1
    for i in range(1, len(rows)):
        if (len(rows[i]) != n):
            return -1
    if (len(rows) != 2*n + 1 or n <= 0):
        return -1

    for i in range(1, n + 1):
        preferences = []
        prefUnique = {}
        for c in range(n):
            try:
                preference = int(rows[i][c])
            except ValueError:
                return -1
            if (preference < 1 or preference > n):
                return -1
            if preference in prefUnique:
                return -1
            preferences.append(preference)
            prefUnique[preference] = True
        if (len(preferences) != n):
            return -1
        h = Entity(i, preferences[:])
        hospitals[h.index] = h
        hQueue.append(h)
        
    for i in range(n + 1, 2*n + 1):
        preferences = []
        prefUnique = {}
        for c in range(n):
            try:
                preference = int(rows[i][c])
            except ValueError:
                return -1       
            if (preference < 1 or preference > n):
                return -1
            if preference in prefUnique:
                return -1
            prefUnique[preference] = True
            preferences.append(preference)
        if (len(preferences) != n):
            return -1
        s = Entity(i-n, preferences[:])
        students[s.index] = s
    return n

# Takes output file and sets correct matches between Hospital and Student Entities
# Verifies correct formatting of output file
def parseOutput(filepath, hospitals, students, n):
    fileStudents = {}
    fileHospitals = {}

    with open(filepath, 'r') as input:
        lines = input.readlines()

    # Verify correct number of lines
    if len(lines) != n:
        print ("Output Error: Incorrect number of lines in output file.")
        return
    
    rows = []
    for line in lines:
        rows.append(line.strip().split())
        
    for i in range(0, n):
        
        # Verify only 2 entries per line
        if len(rows[i]) != 2:
            print ("Output Error: Incorrect number of entries in line")
            return
        
        # Match
        try:
            hospitalIndex = int(rows[i][0])
            studentIndex = int(rows[i][1])
        except ValueError:
            return False

        if hospitalIndex < 1 or hospitalIndex > n or studentIndex < 1 or studentIndex > n:
            return False
        h = hospitals[hospitalIndex]
        s = students[studentIndex]

        if h.index in fileHospitals or s.index in fileStudents:
            print("Output Error: Duplicates found.")
            return False
        
        fileHospitals[h.index] = h
        fileStudents[s.index] = s
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
                    if pref == curHos.index:
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
        filepath = Path(rootPath + "\\output_" + str(i) + ".txt")
        if not filepath.is_file():
            break
        else:
            i += 1

    with open(filepath, "x") as file:
        for i in range(1, 1 + n):
            file.write(str(i) + " " + str(hospitals[i].matchedTo.index) + "\n")
    return
    
def verifier(hospitals, students):
    for currentHos in hospitals.values():
        matchedStudent = currentHos.matchedTo
        currentHosPrefList = currentHos.preferences
        
        for potentialStudent in currentHosPrefList:
            if potentialStudent == matchedStudent.index:
                break
            else:
                potentialStudentEntity = students[potentialStudent]
                potentialStudentMatched = potentialStudentEntity.matchedTo
                potentialStudentPrefList = potentialStudentEntity.preferences
                
                for preferredHospital in potentialStudentPrefList:
                    if preferredHospital == potentialStudentMatched.index:
                        break
                    if preferredHospital == currentHos.index:
                        print("Verifier Error: Unstable Match Found between Hospital " + str(currentHos.index) + " and Student " + str(potentialStudentEntity.index))
                        return
       
    print("Verifier: Matching is stable.")

def generateInputs(rootPath, num):
    filepath = Path("")
    filepath = Path(rootPath + "\\input_" + str(num) + ".txt")

    values = []
    for i in range(1, num+1):
        values.append(i)
    
    with open(filepath, "x") as file:
        file.write(str(num) + "\n")
        for i in (range(2 * num)):
            random.shuffle(values)
            for val in values:
                file.write(str(val) + " ")
            file.write("\n")

    return