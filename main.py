from helper import parseInput, Entity

def main():
    hospitals = {}
    hQueue = []
    students = {}
    n = 0

    n = parseInput("Matching-and-Verifying\\Data\\Input\\testInput.txt", hospitals, hQueue, students)

    print(n)
    
    
    
    

if __name__ == "__main__":
    main()