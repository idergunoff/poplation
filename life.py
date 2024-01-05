import random
import time

import pygame
import numpy as np

# Инициализация Pygame
pygame.init()

# Параметры окна и игры
width, height = 1000, 1000
rows, cols = 200, 200
cell_size = width // rows

# Цвета
white = (25, 0, 55)
black = (30, 200, 74)

# Создание окна
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game of Life")

# Создание начального состояния
grid = np.random.choice([0, 1], size=(rows, cols))

def count_neighbors(grid, x, y, rows, cols):
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            # Исключаем текущую клетку
            if i == 0 and j == 0:
                continue

            # Проверяем соседей через одну клетку
            if (0 <= x + 2 * i < rows) and (0 <= y + 2 * j < cols) and grid[x + 2 * i, y + 2 * j] == 1:
                count += 1

    return count


# Функция обновления состояния клеток
def update(grid):
    new_grid = grid.copy()
    for i in range(rows):
        for j in range(cols):
            # total = count_neighbors(grid, i, j, rows, cols)
            total = int((grid[i, (j-1)%cols] + grid[i, (j+1)%cols] +
                         grid[(i-1)%rows, j] + grid[(i+1)%rows, j] +
                         grid[(i-1)%rows, (j-1)%cols] + grid[(i-1)%rows, (j+1)%cols] +
                         grid[(i+1)%rows, (j-1)%cols] + grid[(i+1)%rows, (j+1)%cols]))

            # Логика клеточных правил "Жизни"
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1
            # if new_grid[i, j] == 0:
            #     if random.random() < 0.00001:
            #         new_grid[i, j] = 1
            # if new_grid[i, j] == 1:
            #     if random.random() < 0.00001:
            #         new_grid[i, j] = 0

    return new_grid


# Основной цикл Pygame
running = True
t = 0
while running:
    print(t)
    t += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill(white)

    # Отрисовка клеток
    for i in range(rows):
        for j in range(cols):
            color = white if grid[i, j] == 0 else black
            pygame.draw.rect(win, color, (j * cell_size, i * cell_size, cell_size, cell_size))

    # Обновление состояния клеток
    grid = update(grid)

    pygame.display.update()



pygame.quit()



