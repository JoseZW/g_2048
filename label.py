import pygame
from point import Point


class Lable:
    def __init__(self, point: Point, width: int, height: int, color: tuple, title: str, value: str,title_size = 15,value_size = 20):
        self.point = point
        self.width = width
        self.height = height
        self.color = color
        self.title = title
        self.value = value
        self.title_size = title_size
        self.value_size = value_size
    def show(self, surface: pygame.Surface, font_name: str):
        # 画图形
        pygame.draw.rect(surface, self.color, (self.point.x, self.point.y, self.width, self.height), 0)

        # 写字


        title_font = pygame.font.Font(font_name, self.title_size)
        title = title_font.render(self.title, True, (0, 0, 0), self.color)

        value_font = pygame.font.Font(font_name, self.value_size)
        value = value_font.render(self.value, True, (0, 0, 0), self.color)

        twidth, theight = title_font.size(self.title)
        vwidth, vheight = value_font.size(self.value)

        surface.blit(title,
                     (self.point.x + (self.width - twidth) // 2, self.point.y + (self.height // 2 - theight // 2) // 2))

        point_value = (self.point.x + (self.width - vwidth) // 2, self.point.y + (self.height + vheight // 2) // 2)

        surface.blit(value, point_value)

class Title:
    def __init__(self, point: Point, width: int,height:int, color: tuple, value=""):
        self.point = point
        self.width = width
        self.height = height
        self.color = color
        self.value = str(value)

    def show(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, (self.point.x, self.point.y, self.width, self.height), 0)
        # 显示数字
        if len(self.value)!=0:
            # font_size = self.width // len(self.value) // 2
            font_size = 30
            font = pygame.font.Font("./resource/font2.ttf", font_size)


            fwidth, fheight = font.size(self.value)

            value = font.render(self.value, True, (255, 255, 255), self.color)

            surface.blit(value,
                         (self.point.x + (self.width // 2 - fwidth // 2), self.point.y + (self.height // 2 - fheight // 2)))
