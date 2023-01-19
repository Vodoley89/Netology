import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # print(contacts_list)


dict_fio = {}
for i in contacts_list:
    fio = ' '.join(i[:3]).split()
    i[:len(fio)] = fio
    # fi_liter = re.compile(r'\W+')
    # new_list = list(filter(None, ([*fi_liter.split(i[0]), *fi_liter.split(i[1])])))
    # if len(new_list) == 3:
    #     i[0], i[1], i[2] = new_list[0], new_list[1], new_list[2]
    dict_fio[''.join(i[:2])] = i

pprint(dict_fio)


num_pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
              r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
              r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
