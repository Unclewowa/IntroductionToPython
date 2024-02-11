class Employee:
    name: str
    jobTitle: str
    salary: float
    
    def __init__(self, name: str, jobTitle: str = None, salary: float = 0):
        self.name = name
        self.jobTitle = jobTitle
        self.salary = round(salary,2)
    
    def increaseSalary(self, perc:float):
        self.salary += round(self.salary*perc,2)
    
    def __str__(self):
        return self.__class__.__name__+"(\n    name: "+self.name+",\n    jobTitle: "+self.jobTitle+",\n    salary: "+str(self.salary)+",\n)"

    
class Manager(Employee):

    def increaseSalary(self, perc: float = 0, bonus: float = 0):
        self.salary += round(self.salary*perc,2)
        self.salary += round(self.salary*bonus,2)
            

if (__name__ == "__main__" ):           
    Petr = Employee("Петр","сотрудник",1000)
    print(Petr)
    Petr.increaseSalary(0.5)
    print(Petr)
    
    IvanManager = Manager("Иван","менеджер",1700)
    print(IvanManager)

    IvanManager.increaseSalary(0.335, 0.25)
    print(IvanManager)
