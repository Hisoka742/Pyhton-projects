N = int(input()) #кол-во участников
list = [] #пустой список

#Добавляем id и баллы в списки
for i in range(N):
    id = int(input())
    ball = int(input())
    list.append([id,ball]) #Добавление в список значений в еще 1 списке

print(list) #Для наглядности как выглядит список,
# содержащий список каждого участника (id и баллы)

#сортировка методом пузырька, можно и любые другие
flag = True
while flag: #делаем бесконечный цикл, пока все не отсортируется
    flag = False #если все сортировано, цикл прекращается
    for i in range(len(list)-1):
        # Проверяем соседние места и меняем их
        if list[i][1] > list[i+1][1]:
            list[i], list[i+1] = list[i+1], list[i]
            #можно писать по-другому, если более понятнее:
            # a = list[i]
            # list[i] = list[i+1]
            # list[i+1] = a
            flag = True

        elif list[i][1] == list[i+1][1]:  #Если совпадают баллы сравниваем id
            if list[i][0] > list[i+1][0]:
                list[i], list[i + 1] = list[i + 1], list[i]

print(list)

#если нужны только баллы то делаем след:
balls = []
for ball in list:
    balls.append(ball[1])

print(balls)