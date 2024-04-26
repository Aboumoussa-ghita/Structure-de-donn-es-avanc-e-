# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:50:46 2024

@author: msssg
"""
class PayDescriptor : 
    def __get__(self , instance , owner): #instance : inst de employee , owner la classe 
        return instance.Pay
    
    def __set__(self , instance , sal):
        if sal<0:
            return ValueError("le salaire doit etre supp a 0 !")
        else : 
            instance.Pay=sal
            
class Compte : 
    
    def __init__(self ,code , solde ):
        self.code=code
        self.solde=solde
    
    def increaseAccount(self , montant ):
        self.solde+=montant
        
    def debit_an_account(self , montant):
        self.solde-=montant
        
class Employee : 
    
    num_of_emp=0
    bonus=0.95
    def __init__(self, first, last, age, Pay, code, solde):
        
        self.first=first
        self.last=last
        self.age=age
        self.Pay=Pay
        self.compte = Compte(code, solde)
        self.num_of_emp+=1
        
    def constEmp(cls , employeeDict) :
        return cls(first=employeeDict['first'],bonus=employeeDict['bonus'],last=employeeDict['last'],age=employeeDict['age'],Pay=employeeDict['Pay'],compte=employeeDict['compte'],num_of_emp=employeeDict['num_of_emp'])
 
    def fullname(self):
        return self.first+self.last
    
    def Apply_bonus(self):
        self.Pay+=self.bonus*self.Pay
    
    def set_bonnus(self,bonus):
        self.bonus=bonus
    
    @staticmethod 
    def IsWorkDay(day):
        if day.weekday==5 or day.weekday==6 :
            return False
        return True
    
    def __str__(self):
        return f"full name : {self.fullname()} - age : {self.age} - pay : {self.Pay}  - compte info: code: {self.compte.code} solde: {self.compte.solde}"
    
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.age}' , '{self.Pay}', '{self.compte}' , ''{self.bonus}' ,'{self.num_of_emp}')"
    
    def __call__(self,pay):  #apres avoir creer cette methode , on peut changer le salaire de cette maniere : emp.pay=emp(nouv_salaire) sans avoir a appeler a la fct
        self.Pay=pay
        
class Manager(Employee)  :

    def __init__(self,first,last,age,Pay,code,solde):
        super().__init__(first, last, age, Pay, code, solde)
        self.employees=[]
        
    def add_emp(self,empl):
        self.employees.append(empl)
        
    def remove_emp(self,empl):
        self.employees.remove(empl)

class Developer(Employee):
    bonus = 1.10
    
    def __init__(self, first, last, age, Pay, code, solde, pro_lang):
        super().__init__(first, last, age, Pay, code, solde)
        self.pro_lang = pro_lang
        
    def full_name(self):
        return super().full_name()
    
    def Apply_bonus(self):
        super().Apply_bonus()

        
# Création d'instances d'employés, de gestionnaires et de développeurs
emp1 = Employee("John", "Doe", 30, 50000, "C001", 1000)
emp2 = Developer("Jane", "Smith", 25, 60000, "C002", 1500, "Python")
emp3 = Manager("Bob", "Johnson", 40, 70000, "C003", 2000)

# Affichage des informations sur les employés
print(emp1)
print(emp2)
print(emp3)

# Modification du salaire avec la méthode __call__
emp1(55000)
print(emp1)

# Application du bonus aux employés et développeurs
emp1.Apply_bonus()
emp2.Apply_bonus()
print(emp1)
print(emp2)

# Ajout d'employés au manager
emp3.add_emp(emp1)
emp3.add_emp(emp2)

# Affichage des employés du manager
print("Employees of Manager:")
for employee in emp3.employees:
    print(employee)

# Suppression d'un employé du manager
emp3.remove_emp(emp1)

# Affichage mis à jour des employés du manager
print("Employees of Manager after removal:")
for employee in emp3.employees:
    print(employee)

    