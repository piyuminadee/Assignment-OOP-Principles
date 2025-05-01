class Employee:
     def __init__(self, id, name, salary, department):
       self.id = id
       self.name = name
       self.salary = salary
       self.department = department
       
     def increase_salary(self, percentage):
           self.salary += (percentage/100)*self.salary
            
     def update_department(self, new_department):
         self.department = new_department 
     def __str__(self):
       return f"{self.id}({self.name}),{self.department}, {self.salary}" 
   
class EmployeeDatabase:
     def __init__(self):
         self.employees = []
      
     def add_employee(self, employee):
         self.employees.append(employee)
         print(f"{employee.name} added as an employee")
     
     def remove_employee(self, id):
         for employee in self.employees:
            if employee.id == id:
                self.employees.remove(employee)
         print(f"{employee.name} removed successfully")
         
     def update_employee_details(self, id, new_salary=None, new_dept=None, new_name=None):
         for employee in self.employees:
           if employee.id == id:  
             if new_salary:
                 employee.salary = new_salary
             if new_dept:
                 employee.department = new_dept
             if new_salary:
                 employee.name = new_name
             print(f"Employee id : {id} update successfully")    
           else: 
             print(f"Employee id : {id} not found")    
                 
                  
        
        
             
         
empDb = EmployeeDatabase()
ahamed = Employee("e333", "Ahamed Harin", 40000, "HR")
raheem = Employee("e334", "Faslan Raheem", 80000, "Account")

empDb.add_employee(raheem)
empDb.add_employee(ahamed)
empDb.remove_employee(raheem)
empDb.update_employee_details("e333", new_dept="Engineering")
         
            

   