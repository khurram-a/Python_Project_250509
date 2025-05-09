#---------------------------------------------------------------------------------
#------Name : Process_Data_Main.py
#------Created  : 30/04/2025 - Khurram Asif
#------Modified : 
#------Description : Python Main program file to process data from an input file,
#------carry out 2 calculations and output into a new file 
#---------------------------------------------------------------------------------


# import the user defined functions
import Calculation_Functions




# import the python built-in csv module
import csv



# initializing the students list
students = []   


try:
        # reading csv file
        with open('Students.csv', 'r') as file:
                        # creating a csv reader object
                        reader = csv.reader(file)

                        # Read the header (first row)
                        header = next(reader) 
                        
                        # extracting field names through first row
                        for row in reader:
                                
                                #data elements extracted from the row 
                                name, math, science, english = row
                                
                                #calculate the average score
                                average = Calculation_Functions.calculate_average([int(math), int(science), int(english)])
                                
                                #assign the grade
                                grade = Calculation_Functions.assign_grade(average)
                        
                                #append the data into the list
                                students.append([name, math, science, english, average, grade])

except FileNotFoundError:
 #       # Handle case when the file is not found
        print(f"Error: Students.csv not found.")

#write the data into a new file
with open('Student_Results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Math', 'Science', 'English', 'Average', 'Grade'])
        writer.writerows(students)

print('Results saved to student_results.csv')




