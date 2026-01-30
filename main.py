from helper import parseInput, Entity, match, matchOuput, parseOutput, verifier, generateInputs
import time

def main():
    hospitals = {}
    hQueue = []
    students = {}
    n = 0

    factorOfTwo = 10
    factorOfTwo+=1
    for i in range(1, factorOfTwo):
        generateInputs("Data\\Input", 2**i)
        start_time = time.perf_counter()

        n = parseInput("Data\\Input\\input_" + str(2**i) + ".txt", hospitals, hQueue, students)
        if n == -1:
            print("Error parsing input.")
            return
        else:
            print(f"Parsed input successfully with n={n}.")
        
        match(hQueue, students)
        matchOuput(hospitals, n, "Data\\Output")
        print("Matched Successfully to Output_" + str(i))
        end_time = time.perf_counter()
        print("Input Count: " + str(2**i) + " | Run Time: " + str({(end_time - start_time)}))

        parseOutput("Data\\Output\\output_" + str(i-1) + ".txt", hospitals, students, n)

        start_time = time.perf_counter()
        verifier(hospitals, students)
        end_time = time.perf_counter()
        print("Verifier Input Count: " + str(2**i) + " | Verifier Run Time: " + str({(end_time - start_time)}))
    
    

if __name__ == "__main__":
    main()