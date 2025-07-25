
class Student:  # Define a class named Student
    name="John Doe"  # Class variable for student's name
    age=20  # Class variable for student's age
    gender="male"  # Class variable for student's gender
    
    
    def _avg_(self):  # Define a method to calculate average marks
        marks = [45, 78, 89, 90, 67, 88]  # List of marks
        sum = 0  # Initialize sum to 0
        for i in marks:  # Iterate over each mark in the list
            sum += i  # Add each mark to sum
        _avg_1 = sum / len(marks)  # Calculate average by dividing sum by number of marks
        print("Average marks:", _avg_1)  # Print the average marks

    @classmethod
    def display_info(cls):
        print("Name:", cls.name)
        print("Age:", cls.age)
        print("gender:",cls.gender)


s1= Student()  # Create an instance of Student class
s1._avg_()  # Call the _avg_ method for the instance
s1.display_info()  # Call the display_info method to show student information
