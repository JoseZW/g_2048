from point import Point
import pygame


class Site:
    def __init__(self, point: Point, width: int, color: tuple):
        self.point = point
        self.width = width
        self.color = color

    def show(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, (self.point.x, self.point.y, self.width, self.width), 0)

    def is_up(self, pos):
        if self.point.x < pos[0] < self.point.x + self.width and self.point.y > pos[1] > self.point.y - 100:
            return True
        else:
            return False

    def is_dwon(self, pos):
        if self.point.x < pos[0] < self.point.x + self.width and self.point.y +self.width< pos[1]:
            return True
        else:
            return False

    def is_left(self, pos):
        if self.point.x > pos[0] and self.point.y < pos[1] < self.point.y + self.width:
            return True
        else:
            return False

    def is_right(self, pos):
        if self.point.x + self.width < pos[0] and self.point.y < pos[1] < self.point.y + self.width:
            return True
        else:
            return False


class Square:
    color_dict = {
        "0": (216, 216, 216),
        "2": (239, 229, 219),
        "4": (236, 224, 202),
        "8": (240, 177, 131),
        "16": (241, 150, 106),
        "32": (245, 123, 95),
        "64": (233, 96, 60),
        "128": (244, 216, 107),
        "256": (236, 204, 103),
        "512": (238, 201, 87),
        "1024": (236, 197, 66),
        "2048": (238, 196, 0),
        "4096": (36, 140, 81)
    }

    def __init__(self, point: Point, width: int, value=0):
        self.point = point
        self.width = width
        self.value = value

    def show(self, surface: pygame.Surface):
        if self.value <= 4096:
            color = Square.color_dict.setdefault(str(self.value), (216, 216, 216))
        else:
            color = Square.color_dict.setdefault(str(self.value), (36, 140, 81))

        pygame.draw.rect(surface, color, (self.point.x, self.point.y, self.width, self.width), 0)
        # 显示数字
        if self.value == 0:
            value = ""
        else:
            value = str(self.value)
        if len(value) != 0:
            if len(value) <= 4:
                font_size = 20
            else:
                font_size = 20 - len(value)
            font = pygame.font.Font("./resource/font2.ttf", font_size)

            fwidth, fheight = font.size(value)

            value = font.render(value, True, (255, 255, 255), color)

            surface.blit(value,
                         (self.point.x + (self.width // 2 - fwidth // 2),
                          self.point.y + (self.width // 2 - fheight // 2)))

    def __repr__(self):
        return str(self.value)
