import square
import random
from point import Point
import json


class ElementError(Exception):
    def __str__(self):
        return "元素有误"


class GameError(Exception):
    def __str__(self):
        return "游戏结束"


def combine(list: list, direction=True):
    square_list = list.copy()
    if len(square_list) != 4:
        raise ElementError
    if direction:
        # 先移动
        index = len(square_list) - 1
        while index >= 1:
            if square_list[index].value == 0:
                t = index
                while t > 0:
                    if square_list[t - 1].value != 0:
                        square_list[index].value = square_list[t - 1].value
                        square_list[t - 1].value = 0
                        break
                    t -= 1
            index -= 1
        # 先加
        index = len(square_list) - 1

        while index >= 1:
            if square_list[index].value == square_list[index - 1].value:
                square_list[index].value *= 2
                square_list[index - 1].value = 0
            index -= 1
        # 再移动
        index = len(square_list) - 1
        while index >= 1:
            if square_list[index].value == 0:
                t = index
                while t > 0:
                    if square_list[t - 1].value != 0:
                        square_list[index].value = square_list[t - 1].value
                        square_list[t - 1].value = 0
                        break
                    t -= 1
            index -= 1
    else:
        # 先移动
        index = 0
        while index < len(square_list) - 1:
            if square_list[index].value == 0:
                t = index
                while t < len(square_list) - 1:
                    if square_list[t + 1].value != 0:
                        square_list[index].value = square_list[t + 1].value
                        square_list[t + 1].value = 0
                        break
                    t += 1
            index += 1
        # 再加
        index = 0
        while index < len(square_list) - 1:
            if square_list[index].value == square_list[index + 1].value:
                square_list[index].value *= 2
                square_list[index + 1].value = 0
            index += 1

        # 再移动
        index = 0
        while index < len(square_list) - 1:
            if square_list[index].value == 0:
                t = index
                while t < len(square_list) - 1:
                    if square_list[t + 1].value != 0:
                        square_list[index].value = square_list[t + 1].value
                        square_list[t + 1].value = 0
                        break
                    t += 1
            index += 1
    return square_list


row2cow = lambda list: [[row[i] for row in list] for i in range(len(list[0]))]


class GameSystem:
    def __init__(self, window, grade, max_grade):
        self.square_list = []
        self.window = window
        self.grade = grade
        self.max_grade = max_grade

        # 从文件中获取最高分
        try:
            with open("./resource/score.json", "r") as file:
                score = json.load(file)
        except FileNotFoundError:
            score = {"max": 0}
        self.max_grade.value = str(score["max"])

    def create(self):
        self.square_list = []
        first_cow = random.randint(0, 3)
        first_row = random.randint(0, 3)
        secend_cow = random.randint(0, 3)
        secend_row = random.randint(0, 3)

        while True:
            if first_cow == secend_cow and first_row == secend_row:
                secend_row = random.randint(0, 3)
            else:
                break

        point_x = [68, 136, 205, 273]
        potin_y = [254, 323, 393, 462]

        for i in range(4):
            t = []
            for j in range(4):
                if i == first_cow and j == first_row or i == secend_cow and j == secend_row:
                    value = random.choice([2, 4])
                    t.append(square.Square(Point(point_x[j], potin_y[i]), 59, value))
                else:
                    t.append(square.Square(Point(point_x[j], potin_y[i]), 59, 0))

            self.square_list.append(t)
        self.show()

    def show(self):
        font_name = "./resource/font2.ttf"
        sum = 0
        for i in self.square_list:
            for j in i:
                sum += j.value
                j.show(self.window)

        self.max_grade.show(self.window, font_name)
        self.grade.value = str(sum)
        self.grade.show(self.window, font_name)

        if int(self.grade.value) > int(self.max_grade.value):
            self.max_grade.value = self.grade.value
            self.max_grade.show(self.window, font_name)

    def up(self):
        l = row2cow(self.square_list)
        for index in range(len(l)):
            l[index] = combine(l[index], False)
        self.square_list = row2cow(l)

        self.rand()
        self.show()

    def down(self):

        l = row2cow(self.square_list)
        for index in range(len(l)):
            l[index] = combine(l[index])
        self.square_list = row2cow(l)

        self.rand()
        self.show()

    def left(self):
        for index in range(len(self.square_list)):
            self.square_list[index] = combine(self.square_list[index], False)

        self.rand()
        self.show()

    def right(self):
        for index in range(len(self.square_list)):
            self.square_list[index] = combine(self.square_list[index])

        self.rand()
        self.show()

    def rand(self):

        l = []
        length = len(self.square_list)
        for cow in range(length):
            for row in range(length):
                if self.square_list[cow][row].value == 0:
                    l.append((cow, row))

        if len(l) != 0:
            t = random.choice(l)
            self.square_list[t[0]][t[1]].value = random.choice([2, 4])

    def is_game_over(self):
        l = []
        length = len(self.square_list)
        for cow in range(length):
            for row in range(length):
                if self.square_list[cow][row].value == 0:
                    l.append((cow, row))

        if len(l) != 0:
            return False
        else:

            length = len(self.square_list)
            for cow in range(length - 1):
                for row in range(length - 1):
                    if self.square_list[cow][row].value == self.square_list[cow][row + 1].value \
                            or self.square_list[cow][row].value == self.square_list[cow + 1][row].value:
                        return False

            for cow in range(length - 1):
                if self.square_list[cow][length - 1].value == self.square_list[cow + 1][length - 1].value:
                    return False

            for row in range(length - 1):

                if self.square_list[length - 1][row].value == self.square_list[length - 1][row + 1].value:
                    return False

            return True

    def quit(self):
        try:
            with open("./resource/score.json", "w") as file:
                scroce = {"max": int(self.max_grade.value)}
                json.dump(scroce, file)
        except:
            pass
