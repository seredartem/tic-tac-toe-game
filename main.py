import os
import random
import time
from datetime import datetime

# Графическая часть меню
stop_app = False
history = []
while stop_app == False:
    print ("1 - Start game")
    print ("2 - Check history")
    print ("3 - Exit")

    to_do = int(input('Enter number: '))
    if to_do == 1:
        name = input("Enter your name: ")
        
        field = [
            '*','*','*',
            '*','*','*',
            '*','*','*',
        ]

        # Алгоритм игры
        
        step_counter = 0
        stop = False
        while stop == False:
            # Очищаем консоль
            os.system("cls")

            # Алгоритм отрисовки поля
            print(" =============")
            index = 0
            for star in field:
                index += 1 
                if index % 3 == 0:
                    print(' | ',star, ' | ', sep='')
                else:
                    print(' | ', star, sep='', end='')
            print(" =============")
          
            # Проверка на победу 
            
            if field[0] == field[1] and field[1] == field[2] and field[0] != '*':
                stop = True
                step_counter += 1
            elif field[3] == field[4] and field[4] == field[5] and field[3] != '*':
                stop = True
                step_counter += 1
            elif field[6] == field[7] and field[7] == field[8] and field[6] != '*':
                stop = True
                step_counter += 1
            elif field[0] == field[4] and field[4] == field[8] and field[0] != '*':
                stop = True
                step_counter += 1
            elif field[2] == field[4] and field[4] == field[6] and field[2] != '*':
                stop = True
                step_counter += 1
            elif field[0] == field[3] and field[3] == field[6] and field[0] != '*':
                stop = True
                step_counter += 1
            elif field[1] == field[4] and field[4] == field[7] and field[1] != '*':
                stop = True
                step_counter += 1
            elif field[2] == field[5] and field[5] == field[8] and field[2] != '*':
                stop = True
                step_counter += 1
            elif not '*' in field:
                stop = True
                step_counter = -1


            if stop == True:
                if step_counter % 2 == 0:
                    print("Won ", name)
                    history.append([str(datetime.now()),name,"Бот.",name])
                elif step_counter == -1:
                    print("Draw")
                    history.append([str(datetime.now()),name,"Бот.", "Ничья"])
                else:
                    print("Won Bot")
                    history.append([str(datetime.now()),name,"Бот.","bot"])
                continue
            
            
            # Обработка хода игрока
            if step_counter % 2 == 0:
                print("Turn", name)
                coord = int(input("Enter coordinate: ")) - 1
                if coord > 8 or coord < 0:
                    continue
                if field[coord] == "X" or field[coord] == "O":
                    continue
                field[coord] = "X"
            # Обработка хода бота
            else:
                bot_coord = random.randint(0,8)
                if field[bot_coord] == "X" or field[bot_coord] == "O":
                    continue
                print("Turn 'Bot' ")
                time.sleep(1)
                field[bot_coord] = "O"
            step_counter += 1
    elif to_do == 2:
        num = 1
        print("History game")
        history_name = input("Enter name: ")
        for data in history:
            if data[1] == history_name:
                print(num,')', data[0], data[1],"VS", data[2],"won: ", data[3])
                num += 1 
    elif to_do == 3:
        print("Exit")
        stop_app = True

