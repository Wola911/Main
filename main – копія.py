from collections import UserDict


class Field():
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(self.validate_phone(value))

    @classmethod
    def validate_phone(cls, value):
        m_value = str(value)

        if len(m_value) == 10 and m_value.isdigit():
            return m_value
        else:
            raise ValueError("Invalid phone number format")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            phone_obj = Phone(phone)
            self.phones.append(phone_obj)
        except ValueError as e:
            print(e)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        if old_phone not in [phone.value for phone in self.phones]:
            raise ValueError("Phone number not found")

        try:
            Phone.validate_phone(new_phone)
        except ValueError as e:
            raise ValueError("Invalid phone number format") from e

        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        keys_to_delete = [key for key in self.data if key == name]
        for key in keys_to_delete:
            del self.data[key]


book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("12345abcde")
book.add_record(john_record)

print(book.find("John"))