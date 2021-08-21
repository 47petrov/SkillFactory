#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Итоговая практическая работа по Юнит 0 - игра "Крестики-нолики"

def greet():
    print("--------------------")
    print("   Сыграем в игру  ")
    print("  крестики-нолики ?")
    print("--------------------")
    print("* Ты ходишь первым *")
    print("* У тебя крестик x *")
    print("--------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
    print(" ПС:               ") 
    print(" разделитель между x и y - пробел")

greet()


# In[ ]:


# Создаем игровое поле размером 3х3:

field = [[" "] *3 for i in range (3)] 

count = 0
while True:
    count += 1
    
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")
    
    x, y = ask()
    
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    
    if check_win():
        break
    
    if count == 9:
        print(" Ничья!")
        break


# In[ ]:


# нумеруем и отображаем на экране игровое поле

def show():
    print(f"    | 0 | 1 | 2 |")
    print(f" +++++++++++++++++++")
    for i in range(3):
        row_info = " " '| '.join(field[i])
        print(f"  {i} | {row_info} | {i}")
        print(f" +++++++++++++++++++")
    print(f"    | 0 | 1 | 2 |")

show()


# In[ ]:


# Вводим крестик-нолик  и проверяем на правильность ввода данных:

def ask():
    while True:
        cords = input("         Ваш ход: ").split()
        
        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue
        
        x, y = cords
        
        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue
        
        x, y = int(x), int(y)
        
        if x not in range (3) or y not in range (3):
            print(" Координаты вне диапазона! ")
            continue
        
        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue
        
        return x, y
        
ask()


# In[ ]:


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

field = [
    [" ", "X", " "],
    [" ", "X", " "],
    [" ", "X", " "]
]

check_win()


# In[ ]:




