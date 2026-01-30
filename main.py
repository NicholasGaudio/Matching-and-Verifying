from helper import parseInput, Entity, match, matchOuput, parseOutput, verifier

def main():
    hospitals = {}
    hQueue = []
    students = {}
    n = 0

    n = parseInput("Data\\Input\\testInput.txt", hospitals, hQueue, students)
    if n == 0:
        print("Error parsicng input.")
        return
    
    match(hQueue, students)
    matchOuput(hospitals, n, "Data\\Output")

    if (parseOutput("Data\\Output\\output_0.txt", hospitals, students, n)):
        print("Output parsed successfully.")
    else:
        print("Error parsing output.")

    if (verifier(hospitals, students)):
        print("Output verified successfully.")
    else:
        print("Error verifying output.")
    
    

if __name__ == "__main__":
    main()