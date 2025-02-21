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
        # for i in self.phones:
        #     index_phone_number = self.phones.index(i)
        #     if phone_number == i.value:
        #         self.phones.pop(index_phone_number)
        #         print (f"{phone_number} deleted")
        x=len(self.phones)                                    # к-ть телефонів у списку до можливого видалення 
        self.phones=list(filter(lambda x: x.value != Phone(phone_number).value , self.phones))     # видалення номеру телефону зі списку
        if x > len(self.phones):
             print(f'Phone number {Phone(phone_number).value} removed') #повідомлення про видалення 
        else:
             print('number not in list')                                #повідомлення про неіснування даного номеру телефону
        return self.phones
    
    def edit_phone (self, old, new):                          # ф-ія редагування номеру телефону
            flag = any(x.value == Phone(old).value for x in self.phones)     # пошук даного телефону у списку телефонів користувача
            if flag:
                self.add_phone(new)      #виклик ф-ії додавання нового номеру телефону
                self.remove_phone(old)       #виклик ф-ії видалення старого номеру телефону
                print (f"Phone number {old} was changed to - {new}")
            else:
                print (f"Phone number {old} not in list")
        # у разі введення номерів у невірному форматі - видається помилка ValueError
    def find_phone(self,phone_number):
        if any(x.value == Phone(phone_number).value for x in self.phones):   # пошук даного телефону у списку телефонів користувача
            # finded_phone=list(filter(lambda x: x.value == Phone(phone_number).value , self.phones)) # пошук даного телефону у списку телефонів користувача
            return Phone(phone_number).value # повернення даного номеру телефону
        else:
            return None # у разі відсутності номеру у списку повертаємо None 
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record_name:Record):
        self.name = record_name.name.value #і'мя у форматі класу Record
        self.data[self.name] = [record_name] #номери телефонів у форматі класу Record
        return self.data

    def find(self,name:str) -> Record:  #ф-ія пошуку контакту за іменем
        finded_name=list(filter(lambda x: x == name , self.data ))
        contact= self.data[finded_name[0]]
        return contact[0]
    
    def delete(self,name:str):   #ф-ія видалення контакту за іменем
        finded_name=list(filter(lambda x: x == name , self.data)) 
        self.data.pop(finded_name[0])        #видаляємо контакт зі словника
        return self.data
    
    def __str__(self): 
        u=[]
        for key in self.data:
            y = self.data[key][0].name.value     #значення імені
            z = self.data[key][0].phones         #список телефонів для цього імені
            u.append(f"{y}: {"; ".join(n.value for n in z)};")  #додаємо ім'я та номер телефону у список для відображення
        return f"book:\n{"\n".join(k for k in u)}"  #додаємо \n для кращого відображення 
        
book = AddressBook()
    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
    # Додавання запису John до адресної книги
book.add_record(john_record)
    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)
    # Виведення всіх записів у книзі
    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555
    # Видалення запису Jane
print(john_record)
Ivan_record = Record("Ivan")
Ivan_record.add_phone("1907328922")
book.add_record(Ivan_record)
print(book)
