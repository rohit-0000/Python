class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def getsalary(self):
        return self.salary

ram=employee("ram",23456778)
print(ram.name)
print(ram.salary)
print(ram.getsalary())

rohan=employee("rohan",9877)
print(rohan.name)
print(rohan.salary)
print(rohan.getsalary())