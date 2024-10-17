def process_grades(input_file, output_file):
    try:
        grades = []

        with open(input_file, 'r') as file:
            for line in file:
                name, grade = line.split()
                grades.append(int(grade))

        average_grade = sum(grades) / len(grades)
        above_average_count = sum(1 for grade in grades if grade > average_grade)

        with open(output_file, 'w') as file:
            file.write(f"Average grade: {average_grade:.2f}\n")
            file.write(f"Students above average: {above_average_count}\n")

        print("Results written to", output_file)

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    


process_grades('grades.txt','results.txt')
