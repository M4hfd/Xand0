win_state = False
counter = 0
playing_field = list(range(1, 10))
win_cords = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))

while not win_state:
    if not counter %2:
        player = "O"
    else:
        player = "X"
    print("Ход игрока:", player)

    for number in range(1, 10, 3):
        print("|", playing_field[number - 1], "|", playing_field[number], "|", playing_field[number + 1], "|")

    position = input("Куда поставить " + player + "? ")
    valid = True
    if playing_field[int(position) - 1] == "X" or playing_field[int(position) - 1] == "O":
        valid = False
        while not valid:
            position = input("Клетка уже занята \nКуда поставить " + player + "? ")
            if playing_field[int(position) - 1] != "X" and playing_field[int(position) - 1] != "O":
                valid = True
    playing_field[int(position) - 1] = player
    counter += 1
    for win_coord in win_cords:
        if counter > 3 and playing_field[win_coord[0] - 1] == playing_field[win_coord[1] - 1] == playing_field[win_coord[2] - 1]:
            print('Игра окончена, победитель', player)
            win_state = True

    if counter == 9:
        print("Ничья")
        win_state = True