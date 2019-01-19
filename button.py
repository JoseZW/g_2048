import pygame

from point import Point


class Button:
    def __init__(self, point: Point, width: int, height: int, color: tuple, value: str,font_size = 20):
        self.point = point
        self.width = width
        self.height = height
        self.color = color
        self.value = value
        self.font_size = font_size

    def show(self, surface: pygame.Surface, font_name: str):
        # 画图形
        pygame.draw.rect(surface, self.color, (self.point.x, self.point.y, self.width, self.height), 0)
        # 画文字
        # font_size = max(self.width // len(self.value)//2,self.height // len(self.value)//2)
        font = pygame.font.Font(font_name, self.font_size)

        txt = font.render(self.value, True, (0, 0, 0), self.color)
        width, height = font.size(self.value)
        surface.blit(txt, (self.point.x + (self.width // 2 - width // 2),
                           self.point.y + (self.height // 2 - height // 2)))
    def is_over(self,pos):
        if self.point.x<=pos[0]<=self.point.x + self.width and self.point.y<=pos[1]<=self.point.y+self.height:
            return True
        else:
            return False

