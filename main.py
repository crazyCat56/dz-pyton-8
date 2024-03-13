'''Доброго времени суток. Этот код нерабочий. Hе разобрачся как по слову вывести строку,при добовнение абонента стираются все кроме последнего, но нового добавляет). Буду еще работать
над этим справочником . Если вы это прочтете это буду рад если поможете.  '''
import json
phone_book = []
phone_book_file = "phonebook.json"

def load_phone_book(phone_book_file):

    with open(phone_book_file, "r") as f:
        return json.load(f)
       
       
def save_phone_book(phone_book, phone_book_file = "hw8/phonebook.json" ):
    with open(phone_book_file, "w", encoding="utf-8") as f:
        json.dump(phone_book, f, indent=4, ensure_ascii=False)

    print("="*len("Данные записной книги обновлены"))
    print("Данные записной книги обновлены")
    print("="*len("Данные записной книги обновлены"))



def work_with_phonebook():
	

    choice=show_menu()

    phone_book=read_txt('phonebook.txt')

    while (choice!=7):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
           print_result(find_by_lastname(phone_book))
        elif choice==3:
            namber=input('введите номер:')
            print(find_by_lastname(phone_book,last_name)) 	
        elif choice==4:
            add_contact(phone_book)
            save_phone_book(phone_book, phone_book_file)
        elif choice==5:
            save_contacts_to_txt
        elif choice==6:
            print('спасиюо что воспользовались нашим нерабочим справочником')
            break


        choice=show_menu()


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice


def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
        phone_book.append(record)

    return phone_book

def print_result(filename):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open('phonebook.txt', 'r', encoding='utf-8') as filename:
        stroki = filename.readlines()
        for str in stroki:
             record = dict(zip(fields, str.split(',')))
             print(record)

def find_by_lastname(phone_book, contacts,f):
    last_name_str=input('введите фамилию: ')
    data = []
    search_mod =(f("surname"))
    for contact in contacts:
        if last_name_str.lower() in contact[search_mod].lower():
            data.append(contact)
    if len(data) > 0: 
        return data
    return None

def add_contact(contacts):
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")
    description = input("Введите описание: ")
    new_contact = {"surname": surname, "name": name, "phone": phone, "description": description}
    contacts.append(new_contact)
    return contacts


def save_contacts_to_txt(file_name = "hw8/phone_book.txt"):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'w', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
        phone_book.append(record)

    return phone_book     
    print("файлы сохранены в формате txt")

work_with_phonebook()
