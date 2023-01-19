from re import sub
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


num_pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
              r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
              r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'

num_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\20'
contacts_list_new = list()
for page in contacts_list:
    page_string = ','.join(page)  # объединение в строку
    format_page = sub(num_pattern, num_pattern_new, page_string)  # замена шаблонов в строке
    page_list = format_page.split(',')  # формируем список строк
    contacts_list_new.append(page_list)

name_pattern = r'^(\w+)(\s*)(\,?)(\w+)' \
               r'(\s*)(\,?)(\w*)(\,?)(\,?)(\,?)'
name_pattern_new = r'\1\3\10\4\6\9\7\8'
contacts_list = list()  # создаем список
for page in contacts_list_new:
    page_string = ','.join(page)  # объединение в строку
    format_page = sub(name_pattern, name_pattern_new, page_string)
    page_list = format_page.split(',')  # формируем список строк
    contacts_list.append(page_list)

