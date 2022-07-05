#изменения ф-я суммы

#Еще один коммент

def sum(a, b):
    return a + b


print(sum(1, 4))

while True:
    try:
        enter = float(input('Введите число: '))
        print(100 / enter)
        print(200 // enter)

#Пошлю его на небо за звездочкой
#теперь все ххорошо

    except ValueError:
        print('Вы ввели не число!!!')

    except ZeroDivisionError:
        print('Делить на ноль нельзя')

    else:
        print('Пользователь молодец,с первого раза')

    finally:
        print('Вывод финали')

print('Все норм Братва')


