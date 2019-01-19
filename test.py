class ElementError(Exception):
    def __str__(self):
        return "元素有误"


def combine(list: list, direction=True):
    square_list = list.copy()
    if len(square_list) != 4:
        raise ElementError
    if direction:
        # 先移动
        index = len(square_list) - 1
        while index >= 1:
            if square_list[index] == 0:
                t = index
                while t > 0:
                    if square_list[t - 1] != 0:
                        square_list[index] = square_list[t - 1]
                        square_list[t - 1] = 0
                        break
                    t -= 1
            index -= 1
        # 先加
        index = len(square_list) - 1

        while index >= 1:
            if square_list[index] == square_list[index - 1]:
                square_list[index] *= 2
                square_list[index - 1] = 0
            index -= 1
        # 再移动
        index = len(square_list) - 1
        while index >= 1:
            if square_list[index] == 0:
                t = index
                while t > 0:
                    if square_list[t - 1] != 0:
                        square_list[index] = square_list[t - 1]
                        square_list[t - 1] = 0
                        break
                    t -= 1
            index -= 1
    else:
        # 先移动
        index = 0
        while index < len(square_list)-1:
            if square_list[index] == 0:
                t = index
                while t < len(square_list)-1:
                    if square_list[t + 1] != 0:
                        square_list[index] = square_list[t + 1]
                        square_list[t + 1] = 0
                        break
                    t += 1
            index += 1
        # 再加
        index = 0
        while index < len(square_list)-1:
            if square_list[index] == square_list[index + 1]:
                square_list[index] *= 2
                square_list[index + 1] = 0
            index += 1

        # 再移动
        index = 0
        while index < len(square_list)-1:
            if square_list[index] == 0:
                t = index
                while t < len(square_list)-1:
                    if square_list[t + 1] != 0:
                        square_list[index] = square_list[t + 1]
                        square_list[t + 1] = 0
                        break
                    t += 1
            index += 1
    return square_list
row2cow = lambda list: [[row[i] for row in list] for i in range(len(list[0]))]

l = [[4,2,4,2],[2,4,2,8],[8,2,4,16],[4,4,8,4]]


def is_game_over(list):
    l = []
    length = len(list)
    for cow in range(length):
        for row in range(length):
            if list[cow][row]== 0:
                l.append((cow, row))

    if len(l) != 0:
        return True
    else:

        length = len(list)
        for cow in range(length - 2):
            for row in range(length - 2):
                if list[cow][row] == list[cow][row + 1] \
                        or list[cow][row] == list[cow + 1][row]:
                    return True

        for cow in range(length - 2):
            if list[cow][length - 1] == list[cow + 1][length - 1]:
                return True

        for row in range(length - 2):
            if list[length - 1][row] == list[length - 1][row + 1]:
                return True

        return False
print(is_game_over(l))

print(row2cow(l))


l = [0, 0, 2, 2]

tl = combine(l,False)
print(tl)
