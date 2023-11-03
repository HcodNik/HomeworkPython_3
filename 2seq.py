import re

user_item = (input('Введите элементы списка через запятую: '))
delimiters = r'[,;/]'
user_item = re.split(delimiters, user_item)
unique_item = []

for item in user_item:
    if item not in unique_item:
        unique_item.append(item)
        user_item.remove(item)
print(user_item)
#print(unique_item)
#print(user_item)






