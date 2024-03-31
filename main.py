from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re


with open(r"phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# шаг 1 - поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname
contacts_list_edit = []
for contacts in contacts_list:
    contacts_edit = ' '.join(contacts[:3])
    contact_lst = contacts_edit.split(' ')
    contacts[0] = contact_lst[0]
    contacts[1] = contact_lst[1]
    contacts[2] = contact_lst[2]
    contacts_list_edit.append(contacts)

# шаг 2 - привести все телефоны в формат +7(999)999-99-99 доб.9999
number_pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})'\
                    r'(\s*)(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
new_number_pattern = r'+7(\4)\8-\11-\14\15\17\18\20'

new_contact_list = []
for contact in contacts_list_edit:
    contact_string = ','.join(contact)
    number_edit = re.sub(number_pattern, new_number_pattern, contact_string)
    contact_list = number_edit.split(',')
    new_contact_list.append(contact_list)

# шаг 3 - объединить все дублирующиеся записи о человеке в одну
for i in new_contact_list:
    for j in new_contact_list:
        if i[0] == j[0] and i[1] == j[1]:
            if i[2] == '':
                i[2] = j[2]
            if i[3] == '':
                i[3] = j[3]
            if i[4] == '':
                i[4] = j[4]
            if i[5] == '':
                i[5] = j[5]
            if i[6] == '':
                i[6] = j[6]

new_contacts_list = []
for lst in new_contact_list:
    if lst not in new_contacts_list:
        new_contacts_list.append(lst)
# pprint(new_contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_contacts_list)
