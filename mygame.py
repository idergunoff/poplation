import pygame

from func import *
from energy import Energy, energies
from organism import Organism, world
from text import show_era, show_gen, show_legend




# Инициализация pygame
pygame.init()
# Создание окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Установка заголовка окна
pygame.display.set_caption("Organisms")

for x in range(0, CANVAS_WIDTH, CELL_SIZE):
    for y in range(0, CANVAS_HEIGHT, CELL_SIZE):
        energy = Energy(x, y)
        energies.add(energy)

for _ in range(25):
    x_spawn = random.randint(0, CANVAS_WIDTH/CELL_SIZE - 1)
    y_spawn = random.randint(0, CANVAS_HEIGHT/CELL_SIZE - 1)
    organism_gen = get_organism_gen()
    print(organism_gen)
    new_organism = Organism(x_spawn*CELL_SIZE, y_spawn*CELL_SIZE, **organism_gen)
    world.add(new_organism)

# Создание переменной для контроля цикла
done = False
paused = False
show_energy = True
# Создание объекта для управления частотой обновления экрана
clock = pygame.time.Clock()

n = 0
# Основной цикл программы
while not done:
    # Обработка событий
    for event in pygame.event.get():
        # Если пользователь нажал на кнопку закрытия окна
        if event.type == pygame.QUIT:
            # Выход из цикла
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                show_energy = not show_energy



    if not paused:
        n += 1
        # Обновление логики игры
        energies.update()
        world.update()
        # Очистка экрана
        window.fill((255, 255, 255))
        # Копирование поверхности с сеткой на экран
        # window.blit(grid, (0, 0))
        # Рисование спрайтов на экране
        if show_energy:
            energies.draw(window)
        world.draw(window)

        show_era(n, window)
        show_legend(window, get_populations(world))
        # Обновление содержимого окна
        pygame.display.flip()
        # print(get_organism_gen())
        # Установка частоты обновления экрана в 10 кадров в секунду
        # clock.tick(5)
    else:
        window.fill((255, 255, 255))
        if show_energy:
            energies.draw(window)
        world.draw(window)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        show_gen(mouse_x, mouse_y, window)
        show_legend(window, get_populations(world))
        pygame.display.flip()

# Завершение работы pygame
pygame.quit()
