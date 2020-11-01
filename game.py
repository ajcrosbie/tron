import objects
import pygame


def redrawWindow(win, player1, player2, walls, rows, width):
    win.fill((0, 0, 0))
    drawGrid(width, rows, win)
    player1.draw(win)
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
    player1 = objects.head((18, 18), (255, 0, 0), rows, width, (1, 0), 0)
    player2 = objects.head((21, 21), (0, 255, 255), rows, width, (-1, 0), 1)
    clock = pygame.time.Clock()
    while True:
        pygame.time.delay(60)
        clock.tick(20)
        keys = pygame.key.get_pressed()
        if player1.life:
            walls.append(player1.move(keys))
        if player2.life:
            walls.append(player2.move(keys))

        player1.collision(walls)
        player2.collision(walls)

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

        redrawWindow(win, player1, player2, walls, rows, width)


if __name__ == '__main__':
    main()
