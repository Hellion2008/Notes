import colorama
from colorama import Fore, Back, Style
import pathlib
from pathlib import Path
import json
import datetime

notes = {}
id = 1
def menu():
    print('Нажми что требуется по номеру:')
    print(Fore.CYAN + '1. Посмотреть все заметки')
    print('2. Создать новую заметку')
    print('3. Редактировать заметку')
    print('4. Прочитать заметку')
    print('5. Удалить заметку')
    print('0. Выход' + Fore.RESET)

def main():
  colorama.init()
  print(Fore.GREEN + 'Консольное приложение ЗАМЕТКИ:' + Fore.RESET)
  menu()
  key_input = int(input('Введите цифру: '))
  while(key_input != 0):
      # if key_input == 1:
        # find_by_substring(file_path, input('Введи контакт: '))
      if key_input == 2:
        create_note_json()   
      # elif key_input == 3:
      #     add_contact(file_path)
      # elif key_input == 4:
      #     change_contact(file_path, int(input('Введите id контакта: ')))
      # elif key_input == 5:
      #     delete_contact(file_path, int(input('Введите id контакта: ')))

      menu()
      key_input = int(input("Введите цифру: "))
  print(Fore.GREEN + 'До свидания!\n')

def create_note_json():
  file_name = 1
  # id = id + 1
  file_title = input('Введите заголовок: ')
  file_text = input('Текст заметки: ')
  time_create = datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")
  # new_note =("\{" 
  #            "\tid: \"{}\""
  #            "\ttitle: \"{}\""
  #            "\ttext: \"{}\""
  #            "\ttime_create: \"{}\""
  #            "\ttime_change: -"
  #            "\}".format(file_name, file_title, file_text, time_create))
  # new_note = ("\{\tid: \"{}\"\ttitle: \"{}\"\ttext: \"{}\"\ttime_create: \"{}\"\ttime_change: -\}".format(file_name, file_title, file_text, time_create))
  new_file = open(str(Path('notes', f'{file_name}.json')), "w+")
  new_file.write("{\n")
  new_file.write(f"\t\"id\": {file_name},\n")
  new_file.write(f"\t\"title\": \"{file_title}\",\n")
  new_file.write(f"\t\"text\": \"{file_text}\",\n")
  new_file.write(f"\t\"time_create\": \"{time_create}\",\n")
  new_file.write("\t\"time_change\": \"-\"\n}")
  new_file.close