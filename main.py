# Код алгоритмов

# 1. Бинарный поиск (алгооритм поиска числа)

def binary_search(lst, item):
    low = 0                 # начало границы списка, в которой выполняется поиск
    high = len(lst)-1       # конец границы этого списка

    while low <= high:          # пока эта часть не сократится до одного элемента,
        mid = (low + high)      # проверяем средний элемент
        guess = lst[mid]
        if guess == item:       # значение найдено
            return mid
        if guess > item:        # много
            high = mid - 1
        else:                   # мало
            low = mid + 1
    return None                 # значение не существует


my_list = [1, 3, 5, 7, 9]           # А теперь протестируем функцию

print(binary_search(my_list, 3))        # получаем 1
print(binary_search(my_list, -1))       # получаем None




