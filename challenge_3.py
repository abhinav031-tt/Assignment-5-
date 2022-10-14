


class student:
    def __init__(self,name,rollno) :
     self._name = name
     self._rollno = rollno
    

    def  set_name(self,name):
        self._name = name

    def get_name(self,name):
        return self._name

    def setRollNumber(self):
         set._rollno = self.rollno

    def get_rollNumber(self):
        return self._rollno 

student_obj = student (input("Enter a name : -"), input("Enter a rollno: - "))

student_obj.set_name(input("Enter a name : -"))
print(student_obj.get_name())
student_obj.set_rollno(input("Enter a rollno : -"))
print(student_obj.get_rollno())
