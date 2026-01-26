from helper import parseInput

def main():
    hospitals = {}
    hQueue = []
    students = {}
    n = 0

    n = parseInput("Data\Input\\testInput.txt", hospitals, hQueue, students)
    print("Hospitals: ", hospitals, "\nStudents: ", students, "\nQueue", hQueue, "\nn:", n)
    

if __name__ == "__main__":
    main()