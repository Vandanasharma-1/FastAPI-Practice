def insert_patients_data(name:str, age:int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('Insert into database')
    else:
        raise TypeError('Incorrect datatype')
    

insert_patients_data('Vandana', 21)
insert_patients_data('Dolly', 'twenty')