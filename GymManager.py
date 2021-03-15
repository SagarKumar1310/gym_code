# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:45:41 2021

@author: sagar kumar
"""

class GymManager:
    regimen = {}
    customers = dict()
    def __init__(self,s_id,s_name):
        self.s_id =s_id
        self.s_name =s_name
        
    @classmethod
    def addCustomer(cls, customer):
        GymManager.customers[customer.getphoneNo()] = customer
        
ob = GymManager('s_1','hero')
