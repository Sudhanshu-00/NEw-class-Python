
class Student:
    name="John Doe"
    age=20
    gender="male"
    
    
    def _avg_(self, _avg_1):
        marks = [45, 78, 89, 90, 67, 88]
        sum = 0
        for i in marks:
            sum += i
        _avg_1 = sum / len(marks)
        print("Average marks:", _avg_1)
