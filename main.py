import pygame
import button
import label
import square
from point import Point
import gameSystem


def main():
    # 初始化窗口
    pygame.init()

    window = pygame.display.set_mode((400, 600))
    window.fill((242, 242, 242))
    font_name = "./resource/font2.ttf"

    # button.Button(Point(39,31),122,122,(178,166,41),"2048").show(window,font_name) # 2048
    label.Title(Point(39, 31), 122, 122, (178, 166, 41), "2048").show(window)  # 2048

    grade = label.Lable(Point(182, 32), 79, 60, (198, 194, 193), "得分", "0")
    # grade.show(window, font_name)  # 得分
    max_grade = label.Lable(Point(283, 32), 79, 60, (198, 194, 193), "最高分", "0")
    # max_grade.show(window, font_name)  # 最高分
    quit = button.Button(Point(182, 113), 79, 32, (250, 163, 47), "退出")
    quit.show(window, font_name)  # 退出
    new_game = button.Button(Point(283, 113), 79, 32, (250, 163, 47), "新游戏")
    new_game.show(window, font_name)  # 新游戏

    site = square.Site(Point(56, 244), 290, (248, 248, 241))
    site.show(window)  # 背景

    game_system = gameSystem.GameSystem(window, grade, max_grade)
    game_system.create()
    game_over = label.Title(Point(100, 285), 200, 100, (178, 166, 41), "GAME OVER")  # gameover
    pygame.display.flip()

    flog = True
    while flog:
        for event in pygame.event.get():
            if event.type == pygame.QUIT \
                    or (event.type == pygame.MOUSEBUTTONDOWN and quit.is_over(event.pos)):  # 退出
                game_system.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN and new_game.is_over(event.pos):  # 新游戏
                site.show(window)  # 背景
                game_system.create()
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and site.is_up(event.pos) \
                    or event.type == pygame.KEYDOWN and event.key == 273:  # 检测上
                if game_system.is_game_over():
                    game_over.show(window)  # gameover
                else:
                    game_system.up()
                pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONDOWN and site.is_dwon(event.pos) \
                    or event.type == pygame.KEYDOWN and event.key == 274:  # 检测下
                if game_system.is_game_over():
                    game_over.show(window)  # gameover
                else:
                    game_system.down()
                pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONDOWN and site.is_left(event.pos) \
                    or event.type == pygame.KEYDOWN and event.key == 276:  # 检测左
                if game_system.is_game_over():
                    game_over.show(window)  # gameover
                else:
                    game_system.left()
                pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONDOWN and site.is_right(event.pos) \
                    or event.type == pygame.KEYDOWN and event.key == 275:  # 检测右
                if game_system.is_game_over():
                    game_over.show(window)  # gameover
                else:
                    game_system.right()
                pygame.display.flip()


if __name__ == '__main__':
    main()
