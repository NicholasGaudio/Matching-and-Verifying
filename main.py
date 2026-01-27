from helper import parseInput, Entity, match, matchOuput

def main():
    hospitals = {}
    hQueue = []
    students = {}
    n = 0

    n = parseInput("Data\\Input\\testInput.txt", hospitals, hQueue, students)
    match(hQueue, students)
    matchOuput(hospitals, n, "Data\Output")
    
    
    

if __name__ == "__main__":
    main()