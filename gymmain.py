# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:53:45 2021

@author: sagar kumar
"""

from GymManager import GymManager
from Customer import Customer

print('please select a choice from the menu')

def menu():
    print('1. create member')
    print('2. view member')
    print('3. delete member')
    print('4. update member')
    print('5. create regimen')
    print('6. view regimen')
    print('7. delete regimen')
    print('8. update regimen')
    print('0. exit')
    print('\nenter your choice')
    
menu()
    
while(True):
    option = int(input())
    if option == 1:
        name = str(input('enter member name - '))
        age = str(input('enter member age - '))
        gender = str(input('enter gender - '))
        phoneNo = str(input('enter phoneNo -'))
        email = str(input('enter member mail - '))
        bmi = str(input('enter member bmi - '))
        if bmi<'18.5':
            r={'Mon': 'Chest','Tue': 'Biceps','Wed': 'Rest','Thu': 'Back','Fri': 'Triceps','Sat': 'Rest','Sun': 'Rest'}
        elif bmi<'25':
            r={'Mon': 'Chest','Tue': 'Biceps','Wed': 'Cardio/Abs','Thu': 'Back','Fri': 'Triceps','Sat': 'Legs','Sun': 'Rest'}
        elif bmi<'30':
            r={'Mon': 'Chest','Tue': 'Biceps','Wed': 'Abs/Cardio','Thu': 'Back','Fri': 'Triceps','Sat': 'Legs','Sun': 'Cardio'}
        elif bmi>'30':
            r={'Mon': 'Chest','Tue': 'Biceps','Wed': 'Cardio','Thu': 'Back','Fri': 'Triceps','Sat': 'cardio','Sun': 'Cardio'}
        duration = str(input('enter duration in months - '))
        customer = Customer(name,age,gender,phoneNo,email,bmi,duration)
        GymManager.regimen[phoneNo]=r
        GymManager.addCustomer(customer)
        
    elif option == 2:
        check_phn = input('enter phoneNo of member: ')
        print('name\tage\tgender\tphoneNo\temail\tbmi\tduration')
        for cusId in GymManager.customers.keys():
            if cusId==check_phn:
               customer = GymManager.customers[cusId]
               name = customer.getname()
               age = customer.getname()
               gender = customer.getgender()
               phoneNo = customer.getphoneNo()
               email =  customer.getemail()
               bmi =  customer.getbmi()
               duration  =  customer.getduration()
               print(name+'\t'+age+'\t'+gender+'\t'+ phoneNo +'\t'+email+'\t'+bmi+'\t'+duration)
        print('\n')
        
    elif option == 3:
        check_phn = input('enter phoneNo you want to delete: ')
        try:
            for cusId in GymManager.Customers.keys():
                if cusId == check_phn:
                    print('member deleted')
            GymManager.customers.pop(check_phn)
        except:
            print("number doesn't exist\n")
    
    elif option == 4:
        check = input('enter phoneNo')
        exr = input('enter if you want to extend or revoke: ')
        if exr == 'extend':
           for cusId in GymManager.customers.keys():
               customer = GymManager.customers[cusId]
               if cusId == check:
                   dur = Customer.getduration()
                   s =  int(dur)+int(input('enter how many months you want to extend'))
                   res = str(s)
                   customer.setduration(res)
                   
        elif exr=='revoke':
            for cusId in GymManager.customers.keys():
               customer = GymManager .customers[cusId]
               if cusId == check:
                   customer.setduration('0')
                   print('membership revoked')
                   
    elif option == 5:
        phn = input('enter the phoneNO of member you want to regimen of ')
        for i in GymManager.regimen:
            if i == phn:
                for j in GymManager.regimen[i]:
                    GymManager.regimen[i][j]=input(j+':')
                    
    elif option == 6:
        check_phn = input('enter phoneNo of member')
        
        for i in GymManager.regimen:
            if i == check_phn:
                for key,val in GymManager.regimen[i].items():
                    print(key,':',val)
        print("\n")
        
    elif option == 7:
        check_phn = input('enter phoneNo of member')
        for i in GymManager.regimen:
            if i==check_phn:
                print('work out regimen deleted')
        GymManager.regimen.pop(check_phn)
        print('\n')
        
    elif option == 8:
        check_phn = input('enter phoneNo of member whos regimen u want to update')
        for i in GymManager.regimen:
            if i == check_phn:    
                d = input('enter the day whivh u want to update')
                for j in GymManager.regimen[i]:
                    if j == d:
                        GymManager.regimen[i][j]=input('enter the workout')
                        print('updated successfully')
                        
        print('\n')
        
    elif option == 0:
        break
    else:
        print('please enter valid number')
        
    menu()
    
def memenu():
     print("\nmember portal\n")
     print('1. my regimen')
     print('2.my profile')
     print('3.exit')
     print('\nenter your choice:')
        
memenu()
while(True):
        option = int(input())
        if option == 1:
            p = input('enter your phoneNo')
            print("__ your regimen based 0n your bmi__")
            for i in GymManager.regimen:
                if i==p:
                    for key,val in GymManager.regimen[i].items():
                        print(key,":",val)
                        
            print("\n")
            
        elif option == 2:
            p = input('enter your phoneNo')
            try:
                for cusId in GymManager.Customers.keys():
                    if cusId == p:
                        customer = GymManager.customers[cusId]
                        name = customer.getname()
                        age  = customer.getage()
                        gender = customer.getgender()
                        phoneNo = customer.getphoneNo()
                        email = customer.getemail()
                        bmi = customer.getbmi()
                        duration = customer.getduration()
                        print("your profile")
                        print("name:",name,"\nage:",age,"\ngender:",gender,"\nphone:",phoneNo,"\nemail:",email,"\nbmi:",bmi,"\nduration:",duration)
            except:
                print("no user with this phone number exist")
                
                
        elif option == 2:
            break
        else:
             exit()
                        
            
memenu()
          
            