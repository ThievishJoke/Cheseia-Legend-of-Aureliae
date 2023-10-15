
# an employee record
Employee = { 
    'emp1': {
        'name': 'Lisa', 
        'age': '29',
        'Designation':'Programmer'
            }, 
         'emp2': {
             'name': 'Steve',
             'age': '25',
             'Designation':'HR'
                 }
             } 
  
# to make the updation dynamic
  
# Get input from the user for which 
# employee he needs to update
empid = input("Employee id :")
  
# which attribute / key to update
attribute = input("Attribute to be updated :")
  
# what value to update
new_value = input("New value :")
  
# updation of the dictionary
Employee[empid][attribute]= new_value
  
  
print(Employee)