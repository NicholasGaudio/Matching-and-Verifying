from helper import parseInput, Entity, match, matchOuput, parseOutput

def main():
    hospitals = {}
    hQueue = []
    students = {}
    n = 0

    n = parseInput("Data\\Input\\testInput.txt", hospitals, hQueue, students)
    
    #match(hQueue, students)
    #matchOuput(hospitals, n, "Data\Output")

    if (parseOutput("Data\\Input\\testOutput.txt", hospitals, students, n)):
        print("Output parsed successfully.")
    else:
        print("Error parsing output.")
    
    
    

if __name__ == "__main__":
    main()