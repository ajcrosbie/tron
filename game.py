import objects
import pygame


def redrawWindow(win, player1, player2, walls, rows, width, Tplayer2=True):
    win.fill((0, 0, 0))
    drawGrid(width, rows, win)
    player1.draw(win)
    if Tplayer2:
        player2.draw(win)
    for i in walls:
        i.draw(win)
    pygame.display.update()


def drawGrid(w, rows, surface):
    SBT = w // rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + SBT
        y = y + SBT

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

    pass


def main():
    width = 720
    rows = 40
    win = pygame.display.set_mode((width, width))
    walls = []
    for i in range(rows):
        walls.append(objects.wall((-1, i), (255, 255, 255), rows, width))
        walls.append(objects.wall((rows, i), (255, 255, 255), rows, width))
        walls.append(objects.wall((i, -1), (255, 255, 255), rows, width))
        walls.append(objects.wall((i, rows), (255, 255, 255), rows, width))
    nPls = int(input("number of player 1 or 2"))
    if nPls == 2:
        player1 = objects.head((18, 18), (255, 0, 0), rows, width, (1, 0), 0)
        player2 = objects.head((21, 21), (0, 255, 255),
                               rows, width, (-1, 0), 1)
        Tplayer2 = True
    else:
        player1 = objects.head((18, 18), (255, 0, 0), rows, width, (1, 0), 0)
        player2 = "not found"
        Tplayer2 = False

    clock = pygame.time.Clock()
    while True:
        if Tplayer2:
            pygame.time.delay(60)
            clock.tick(20)
        else:
            pygame.time.delay(30)
            clock.tick(40)
        keys = pygame.key.get_pressed()
        if player1.life:
            walls.append(player1.move(keys))
        if Tplayer2:
            if player2.life:
                walls.append(player2.move(keys))
        player1.collision(walls)
        if Tplayer2:
            player2.collision(walls)
        if Tplayer2:
            if not player1.life and not player2.life:
                player1.reset()
                player2.reset()
                walls = []
                for i in range(rows):
                    walls.append(objects.wall(
                        (-1, i), (255, 255, 255), rows, width))
                    walls.append(objects.wall(
                        (rows, i), (255, 255, 255), rows, width))
                    walls.append(objects.wall(
                        (i, -1), (255, 255, 255), rows, width))
                    walls.append(objects.wall(
                        (i, rows), (255, 255, 255), rows, width))
        else:
            if not player1.life:
                player1.reset()
                # player2.reset()
                walls = []
                for i in range(rows):
                    walls.append(objects.wall(
                        (-1, i), (255, 255, 255), rows, width))
                    walls.append(objects.wall(
                        (rows, i), (255, 255, 255), rows, width))
                    walls.append(objects.wall(
                        (i, -1), (255, 255, 255), rows, width))
                    walls.append(objects.wall(
                        (i, rows), (255, 255, 255), rows, width))
        if Tplayer2:
            redrawWindow(win, player1, player2, walls, rows, width)
        else:
            redrawWindow(win, player1, player2, walls, rows, width, Tplayer2)


if __name__ == '__main__':
    main()
