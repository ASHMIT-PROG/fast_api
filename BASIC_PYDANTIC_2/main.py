
#to avoid to write this large chunk of code we use pydantic 

def insert_patient_data(name:str,age:int):
    if type(name) == str and type (age)==int:
        if age<0:
            raise ValueError('age cant be 0')
            print (name,age)
    else:
        raise TypeError("incorrect data type")


insert_patient_data("ashmit",30)

