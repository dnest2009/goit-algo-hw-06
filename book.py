from collections import UserDict

class ValidationNumberError(Exception):
    pass


class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        self.value = value


class Phone(Field):
    def __init__(self, value):
        self.value = value
        if not self.value.isdigit() or len(self.value) != 10: #перевірка номеру
            raise ValidationNumberError (f"ValueError")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self,phone_number:str) -> Phone:   
        self.phones.append(Phone(phone_number))    # ф-ія додавання нового номеру, номер додається у форматі класу Phone
        return self.phones                         # ф-ія повертає список телефонів


    def remove_phone (self, phone_number):
        self.phones=list(filter(lambda x: x.value != phone_number, self.phones))     # видалення номеру телефону зі списку
        return self.phones
    

    def edit_phone (self, old, new):                          # ф-ія редагування номеру телефону
            flag = any(x.value == old for x in self.phones)     # пошук даного телефону у списку телефонів користувача
            if flag:
                self.add_phone(new)      #виклик ф-ії додавання нового номеру телефону
                self.remove_phone(old)       #виклик ф-ії видалення старого номеру телефону
            else:
                raise ValueError("Номеру не існує")
 

    def find_phone(self,phone_number):
        if any(x.value == phone_number for x in self.phones):   # пошук даного телефону у списку телефонів користувача
            find_phone = list(filter(lambda x: x.value == phone_number, self.phones))     # видалення номеру телефону зі списку
            return find_phone[0] # повернення даного номеру телефону
        else:
            return None # у разі відсутності номеру у списку повертаємо None 
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record_name:Record):
        self.name = record_name.name.value #і'мя у форматі класу Record
        self.data[self.name] = record_name #номери телефонів у форматі класу Record
        return self.data


    def find(self,name:str) -> Record:  #ф-ія пошуку контакту за іменем
        return self.data.get(name)
    

    def delete(self,name_delete:str):   #ф-ія видалення контакту за іменем
        self.data.pop(self.find(name_delete).name.value)
        return self.data
    

    def __str__(self): 
        u=[]
        for key in self.data:
            y = self.data[key].name.value     #значення імені
            z = self.data[key].phones         #список телефонів для цього імені
            u.append(f"{y}: {"; ".join(n.value for n in z)};")  #додаємо ім'я та номер телефону у список для відображення
        return f"book:\n{"\n".join(k for k in u)}"  #додаємо \n для кращого відображення 
        
        
book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
jane_record.add_phone("1176543211")
jane_record.remove_phone("9876543210")
jane_record.edit_phone("1176543211","1234567890")
book.add_record(jane_record)
john = book.find("John")
john1 = book.find("Jane")
john1.add_phone("1176543211")
john1.edit_phone("1176543211","0987654321")
john.edit_phone("1234567890","1112223333")
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  #Виведення: John: 5555555555
Ivan_record = Record("Ivan")
Ivan_record.add_phone("1907328922")
book.add_record(Ivan_record)
# book.delete("Ivan")
Ivan_record.edit_phone("1907328921", "0987654321")
print(book)

