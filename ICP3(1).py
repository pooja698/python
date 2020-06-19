class Employee:
    empCount = 0
    sal = 0
    def __init__(self, name, family,salary, department):
       self.name = name
       self.family=family
       self.salary= salary
       self.department=department
       Employee.empCount += 1
       Employee.sal = Employee.sal + self.salary
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        print("Name : ", self.name, ", Family: ", self.family," Salary: ", self.salary, ", Department: ", self.department)
    def average(self) :
        sum = 0
        avg = Employee.sal / Employee.empCount
        print("average")
        print(avg)
class FulltimeEmployee(Employee):
  pass
emp1 = Employee("Zara", "sksjs", 200000,"IT")
emp2 = Employee("sara", "skdhdj", 300000,"ITis")
emp3 = FulltimeEmployee("sara", "skdhdj",300000,"ITis")
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp2.average()
print ("Total Employee %d" % Employee.empCount)

