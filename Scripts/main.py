from helper import parseInput, Entity, match, matchOuput, parseOutput, verifier, generateInputs
import time

def main():
    hospitals = {}
    hQueue = []
    students = {}
    n = 0

    testVerifierAlone = False

    input = "Data\\Input\\input_16.txt"

    if not testVerifierAlone:
        
        n = parseInput(input, hospitals, hQueue, students)
        
        match(hQueue, students)
        output = matchOuput(hospitals, n, "Data\\Output")

        if parseOutput(output, hospitals, students, n):
            verifier(hospitals, students)
    else:
        output = "Data\\Output\\good_output_from_input_16.txt"
        # output = "Data\\Output\\invalid_output_from_input_16.txt"
        # output = "Data\\Output\\unstable_output_from_input_16.txt"

        n = parseInput(input, hospitals, hQueue, students)
        
        match(hQueue, students)
        #matchOuput(hospitals, n, "Data\\Output")

        if parseOutput(output, hospitals, students, n):
            verifier(hospitals, students)

    
    

if __name__ == "__main__":
    main()