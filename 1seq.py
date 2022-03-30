# Пользователь вводит количество элементов будущего списка
# После этого по очереди по одной вводит любые цифры
# Сохранить цифры в список
# Отсортировать список по возрастанию и вывести на экран

number_elem=int(input('Введите количество элементов списка '))
list=[]
i=1
while i<=number_elem:
    string1='Введите '
    string2= str(i)
    string3 = ' элемент: '
    new_elem=input(string1+string2+string3)
    list.append(new_elem)
    i=i+1
list.sort()
print('Вывод: ', list)
