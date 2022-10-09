
from exception import ValidateException
from book import Address_Book
from human import Human

def input_values():
    name = input("Input Name --> ")
    address = input("Input Address --> ")
    phone = input("Input phone --> ")
    try:
        p = Human(name,address,phone)
    except ValidateException as ex:
        print(ex.message)
    else:
        return p

if __name__ == "__main__":
    addressBook = Address_Book()
    for i in range(0,2):
        p = input_values()
        addressBook.add(p)
    print(addressBook)