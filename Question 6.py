import random

class personal_info:
    def __init__ (self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone
    def set_name(self,name):
        self.__name = name
    def set_address(self,address):
        self.__address = address
    def set_age(self,age):
        self.__age = age
    def set_phone(self,phone):
        self.__phone = phone
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_phone(self):
        return self.__phone
def main():
    name = input('Enter your name ')
    address = input('Enter your address ')
    age = input('Enter your age ')
    phone = input('Enter your phone number ')
    print ('Name:', name)
    print ('Address:', address)
    print ('Age:', age)
    print ('Phone number:', phone)
main()

        
