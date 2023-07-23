import colorama
from colorama import Fore, Back, Style
import pathlib
from pathlib import Path
import datetime

# Вывод меню для информации 
def menu():
    print('Нажми что требуется по номеру:')
    print(Fore.CYAN + '1. Посмотреть все заметки')
    print('2. Создать новую заметку')
    print('3. Редактировать заметку')
    print('4. Прочитать заметку')
    print('5. Удалить заметку')
    print('0. Выход' + Fore.RESET)

# Основная функция
def main():
  colorama.init()
  print(Fore.GREEN + 'Консольное приложение ЗАМЕТКИ:' + Fore.RESET)
  menu()
  key_input = int(input('Введите цифру: '))
  while(key_input != 0):
      if key_input == 1:
        show_notes()
      if key_input == 2:
        create_note_json()   
      # elif key_input == 3:
      #     add_contact(file_path)
      elif key_input == 4:
         read_note(int(input(Fore.YELLOW + 'Введите номер заметки: ')))
      elif key_input == 5:
          delete_note(int(input(Fore.YELLOW + 'Введите номер заметки: ')))

      menu()
      key_input = int(input("Введите цифру: "))
  print(Fore.GREEN + 'До свидания!\n')

def show_notes():
   id = 1
  #  path_file = Path('notes', f'{id}.json')
   while Path('notes', f'{id}.json').is_file():
      temp_dic = load_from_json(str(Path('notes', f'{id}.json')))
      print('{}. {}'.format(temp_dic['id'], temp_dic['title']))
      id = id + 1

# Создание новой заметки
def create_note_json():
  file_name = getId()
  file_title = input(Fore.YELLOW + 'Введите заголовок: ' + Fore.RESET)
  file_text = input(Fore.YELLOW + 'Текст заметки: ' + Fore.RESET)
  time_create = datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")
  path_file = str(Path('notes', f'{file_name}.json'))
  new_file = open(path_file, "w")
  new_file.write("{\n")
  new_file.write(f"\t\"id\": {file_name},\n")
  new_file.write(f"\t\"title\": \"{file_title}\",\n")
  new_file.write(f"\t\"text\": \"{file_text}\",\n")
  new_file.write(f"\t\"time_create\": \"{time_create}\",\n")
  new_file.write("\t\"time_change\": \"-\"\n}")
  new_file.close
  # notes[file_name] = path_file
  print(Fore.GREEN + 'Вы создали новую заметку\n' + Fore.RESET)

# Чтение заметки по его id
def read_note(id):
   path_file = str(Path('notes', f'{id}.json'))
   note_dic = load_from_json(path_file)
   print('Заголовок: ' +  Fore.RESET + '{}'.format(note_dic['title']))
   print(Fore.YELLOW + 'Создано:' + Fore.RESET + ' {}'.format(note_dic['time_create']))
   print(Fore.YELLOW + 'Изменено:' + Fore.RESET + ' {}'.format(note_dic['time_change']))
   print('{}\n'.format(note_dic['text']))

# Удаление заметки по его id
def delete_note(id):
    path_file = Path('notes', f'{id}.json')
    path_file.unlink()
    print(Fore.GREEN + 'Заметка удалена\n' + Fore.RESET)

# Вспомогательная функция для парсинга файла .json в словарь
def load_from_json(file_path):
  json_dic = {}
  with open(file_path, 'r') as note:
    for line in note:
      index = line.find(':')
      if index != -1:
        key = line[:index].strip()
        content = line[index+1:].strip()

        key = key[1:len(key)-1]
        if content.rfind('"') != -1:
          content = content[1:content.rfind('"')]
        else:
          content = content[:content.rfind(',')]

        json_dic[key] = content
  return json_dic

# Вспомогательная функция для определения id для новой заметки
def getId():
   id = 1
   while Path('notes', f'{id}.json').is_file():
      id = id + 1
   return id

# def json_to_string(file_path):
#   json = "" 
#   with open(file_path, 'r') as note:
#         for line in note:
#            json = json + line
#   return json