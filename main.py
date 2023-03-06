def bubble(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def BinarySearch(numbers, NumberUser, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if numbers[middle] == NumberUser:
        return middle
    elif NumberUser < numbers[middle]:
        return BinarySearch(numbers, NumberUser, left, middle - 1)
    else:
        return BinarySearch(numbers, NumberUser, middle + 1, right)

what = True
while what:
    try:
        NumbersList = input("Введите последовательность чисел через пробел: ").split()
        NumbersListMod = [int(x) for x in NumbersList]
        NumbersListMod = bubble(NumbersListMod)
        print('Сортировка чисел:', NumbersListMod)

        NumberUser = input("Введите число для установки позиции элемента: ")
        NumberUser = int(NumberUser)
        what = False
    except ValueError:
            print(f'Ошибка {ValueError}')
            print('Введены некорректные данные. Необходимо указывать только натуральные числа.')

if NumberUser not in NumbersListMod:
     print(f'Число {NumberUser} не найдено в числах последовательности. {NumbersListMod}')

index = BinarySearch(NumbersListMod, NumberUser, 0, len(NumbersListMod))

print("Номер позиции элемента: ", (index + 1))
if index == int(len(NumbersListMod)-1):
    print(f'число {NumberUser} последнее значение в списке, предыдущее число {NumbersListMod[index-1]}')
elif index == 0:
    print(f'число {NumberUser} первое значение в списке, следующее {NumbersListMod[index + 1]}')
else:
    print(f'предыдущее число {NumbersListMod[index-1]}, следующее {NumbersListMod[index + 1]}')

