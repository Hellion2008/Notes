import colorama
from colorama import Fore, Back, Style
import json

def menu():
    colorama.init()
    print(Fore.GREEN + 'Консольное приложение ЗАМЕТКИ:' + Fore.RESET)
    print('Нажми что требуется по номеру:')
    print(Fore.CYAN + '1. Посмотреть все заметки')
    print('2. Создать новую заметку')
    print('3. Редактировать заметку')
    print('4. Прочитать заметку')
    print('5. Удалить заметку')
    print('0. Выход' + Fore.RESET)

# def main():
#   print("Телефонный справочник!!!\n")
#   file_path = r'task38\\phonebook.txt'
#   menu()
#   key_input = int(input('Введите цифру: '))
#   while(key_input != 0):
#       if key_input == 1:
#           read_phonebook(file_path)
#       elif key_input == 2:
#           find_by_substring(file_path, input('Введи контакт: '))
#       elif key_input == 3:
#           add_contact(file_path)
#       elif key_input == 4:
#           change_contact(file_path, int(input('Введите id контакта: ')))
#       elif key_input == 5:
#           delete_contact(file_path, int(input('Введите id контакта: ')))

#       menu()
#       key_input = int(input("Введите цифру: "))
#   print('До свидания!')

menu()