import pygame


class wall():
    def __init__(self, pos, colour, rows, winWidth):
        self.pos = pos
        self.colour = colour
        self.size = winWidth // rows - 2
        self.dis = self.size + 2
        self.rows = rows
        self.winWidth = winWidth

    def draw(self, win):
        t = (self.pos[0]*dis+1, self.pos[1]*dis+1, self.size, self.size)
        pygame.draw.rect(win, self.colour, t)


class head():
    def __init__(self, pos, colour, rows, winWidth, dir, type):
        self.pos = pos
        self.colour = colour
        self.size = winWidth // rows - 2
        self.rows = rows
        self.winWidth = winWidth
        self.dir = dir
        self.type = type

    def move(self, keys):
        self.cpos = self.pos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if keys[pygame.K_w] and self.type == 0:
            self.dir[0] = -1
        if keys[pygame.K_w] and self.type == 0:
            self.dir[0] = 1
        if keys[pygame.K_w] and self.type == 0:
            self.dir[1] = -1
        if keys[pygame.K_w] and self.type == 0:
            self.dir[1] = 1
        if keys[pygame.K_w] and self.type == 1:
            self.dir[0] = -1
        if keys[pygame.K_w] and self.type == 1:
            self.dir[0] = 1
        if keys[pygame.K_w] and self.type == 1:
            self.dir[1] = -1
        if keys[pygame.K_w] and self.type == 1:
            self.dir[1] = 1

        self.pos[0] = self.pos[0] + self.dir[0]
        self.pos[1] = self.pos[1] + self.dir[1]
        NewWall = wall(self.cpos, self.colour, self.rows, self.winWidth)
        return NewWall

    def move(self, win):
