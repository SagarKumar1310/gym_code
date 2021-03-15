# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 18:54:40 2021

@author: sagar kumar
"""

class Customer:
    def __init__(self,name =' ',age =' ',gender=' ',phoneNo=' ',email=' ',bmi=' ',duration=' '):
      self.__name = name
      self.__age = age
      self.__gender = gender
      self.__phoneNo = phoneNo
      self.__email = email
      self.__bmi = bmi
      self.__duration = duration
      
    def setname(self,name):
        self.__name = name
        
    def getname(self):
        return self.__name
        
    def setage(self,age):
        self.__age = age
        
    def getage(self):
         return self.__age
        
    def setgender(self,gender):
        self.__gender = gender
        
    def getgender(self):
        return self.__gender
    
    def setphoneNo(self,phoneNo):
        self.__phoneNo = phoneNo
        
    def getphoneNo(self):
        return self.__phoneNo
        
    def setemail(self,email):
        self.__email = email
        
    def getemail(self):
        return self.__email
        
    def setbmi(self,bmi):
        self.__bmi = bmi
        
    def getbmi(self):
        return self.__bmi
        
    def setduration(self,duration):
        self.__duration = duration
        
    def getduration(self):
        return self.__duration
    
    def __str__(self):
        return self.getname()+" "+self.getphoneNo()+" "+self.getduration()+" "+self.getage()+" "+self.getgender()+" "+self.getbmi()+" "
    
        
        
        