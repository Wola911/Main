from collections import UserDict
import datetime


def is_date(value):
    try:
        datetime.datetime.strptime(value, '%Y-%m-%d')
        return True
    except ValueError:
        return False


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Birthday(Field):
    def __init__(self, value):
        if is_date(value):
            super().__init__(value)
        else:
            raise ValueError("Invalid birthday format")


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("Invalid phone number format")


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone):
        try:
            phone_obj = Phone(phone)
            self.phones.append(phone_obj)
        except ValueError as e:
            print(e)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p.value) != phone]

    def edit_phone(self, old_phone, new_phone):
        if old_phone not in [str(phone.value) for phone in self.phones]:
            raise ValueError("Phone number not found")

        try:
            Phone(new_phone)
        except ValueError as e:
            raise ValueError("Invalid phone number format") from e

        for phone in self.phones:
            if str(phone.value) == old_phone:
                phone.value = new_phone

    def find_phone(self, phone):
        for p in self.phones:
            if str(p.value) == phone:
                return p

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p.value) for p in self.phones)}"

    def days_to_birthday(self):
        if self.birthday:
            try:
                # Try converting the string value to datetime.date
                self.birthday.value = datetime.datetime.strptime(self.birthday.value, '%Y-%m-%d').date()
            except ValueError:
                # If conversion fails, assume birthday is unknown
                pass

            today = datetime.date.today()
            next_birthday = datetime.date(today.year, self.birthday.value.month, self.birthday.value.day)
            if today > next_birthday:
                next_birthday = datetime.date(today.year + 1, self.birthday.value.month, self.birthday.value.day)
            days_left = (next_birthday - today).days
            return days_left
        else:
            return None


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


# Приклад використання
book = AddressBook()

john_record = Record("John", "1990-01-01")
john_record.add_phone("1234567890")
john_record.add_phone("12345abcde")
book.add_record(john_record)

print(book.find("John"))

print("Days until John's birthday:", john_record.days_to_birthday())