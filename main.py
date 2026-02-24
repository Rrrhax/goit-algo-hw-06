from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass
	

class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("The number has to be 10 digits!")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def find_phone(self, phone_number):
        return next((number for number in self.phones if number.value == phone_number), None)

        # for number in self.phones:
        #     if number.value == phone_number:
        #         return number

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if phone is None:
            raise ValueError("Phone not found")
        self.phones.remove(phone)
        
    def edit_phone(self, old_phone, new_phone):
		self.add_phone(new_phone)
        self.remove_phone(old_phone) #можно сделать с проверкой через if на ValueError но специально сделал таким образом, ибо 1- ValueError вложен уже в обе функции 2- для краткости и чистоты кода
        return
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)
    
    def __str__(self):
            contacts = "\n".join(str(r) for r in self.data.values())
            return f"All contacts:\n----------\n{contacts}\n----------"


# Створення нової адресної книги
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
     
print(book)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
book.delete("Jane")
