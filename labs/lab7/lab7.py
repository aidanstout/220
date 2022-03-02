"""
Aidan Stout
lab7.py
Problem: create program that pulls grades from a file, finds the average,
    then prints them in a new file
I certify that this is entirely my work
"""


def weighted_average(in_file_name, out_file_name):
    with open(in_file_name, "r") as grade_values:
        with open(out_file_name, "w") as grade_averages:
            lines = grade_values.readlines()
            class_average = 0
            counter = 0
            for line_var in lines:
                diff_lists = line_var.split(':')
                names = diff_lists[0]
                numbers = diff_lists[1]
                number_list = numbers.split()
                weight_sum = 0
                average = 0
                for n in range(0, len(number_list), 2):
                    weight_sum = weight_sum + eval(number_list[n])
                    average = average + (eval(number_list[n]) * eval(number_list[n+1]))
                grade_averages.write(names + "'s average: ")
                if weight_sum > 100:
                    grade_averages.write("Error: The weights are more than 100")
                    grade_averages.write("\n")
                elif weight_sum < 100:
                    grade_averages.write("Error: The weights are less than 100")
                    grade_averages.write("\n")
                else:
                    average = average / 100
                    grade_averages.write(str(round(average, 1)))
                    grade_averages.write("\n")
                    counter = counter + 1
                    class_average = class_average + average
            class_average = class_average / counter
            grade_averages.write("Class average: ")
            grade_averages.write(str(round(class_average, 1)))
            grade_averages.write("\n")
