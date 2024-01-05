import random
import pygame
from config import *

def get_brown_shade(value):
    if value < 0:
        value = 0
    elif value > 10:
        value = 10

    # Используем линейную интерполяцию между белым (255, 255, 255) и темно-коричневым (101, 67, 33)
    # для получения оттенков коричневого
    brown_shade = (
        int(255 - (value / 10) * (255 - 101)),
        int(255 - (value / 10) * (255 - 67)),
        int(255 - (value / 10) * (255 - 33))
    )
    return brown_shade


def get_color_organism(health, lifetime, food, collect, attack, rest):
    red = int(((health + rest)/ 50) * 255)
    red = 255 if red > 255 else red
    green = int(((food + lifetime)/ 50) * 255)
    green = 255 if green > 255 else green
    blue = int(((attack + collect)/ 50) * 255)
    blue = 255 if blue > 255 else blue
    return (red, green, blue)


def interpolate(zero_percent, hundred_percent, desired_percent):
    # Вычисление значения искомого процента по формуле линейной интерполяции
    result = zero_percent + (desired_percent / 50) * (hundred_percent - zero_percent)
    return result


def get_organism_gen():
    total_resources = 100
    parameters = ['health', 'lifetime', 'food', 'collect', 'attack', 'rest']

    # Генерация случайных процентных значений для параметров
    percentages = {param: random.uniform(0, 1) for param in parameters}
    total_percentage = sum(percentages.values())

    # Преобразование процентных значений в реальное количество ресурсов
    resources_distribution = {param: int(round(total_resources * (percentages[param] / total_percentage), 0)) for param in
                              parameters}
    result_gen = {
        param: int(round(interpolate(param_interval[param][0], param_interval[param][1], resources_distribution[param])))
        for param in parameters
    }
    result_gen['color'] = get_color_organism(**resources_distribution)
    return result_gen


# Функция для получения спрайта по координатам x, y
def get_sprite_at_position(group, x, y):
    for sprite in group:
        if sprite.rect.collidepoint(x, y):
            return sprite
    return None


def get_new_position(x, y):
    direction = random.choice(['up', 'down', 'left', 'right'])
    x_new = x
    y_new = y
    if direction == 'up':
        y_new = y - CELL_SIZE
        y_new = 0 if y_new < 0 else y_new
    elif direction == 'down':
        y_new = y + CELL_SIZE
        y_new = CANVAS_HEIGHT - CELL_SIZE if y_new > CANVAS_HEIGHT - CELL_SIZE else y_new
    elif direction == 'left':
        x_new = x - CELL_SIZE
        x_new = 0 if x_new < 0 else x_new
    elif direction == 'right':
        x_new = x + CELL_SIZE
        x_new = CANVAS_WIDTH - CELL_SIZE if x_new > CANVAS_WIDTH - CELL_SIZE else x_new

    return x_new, y_new


def get_birth_position(direction, x, y):
    x_new = x
    y_new = y
    if direction == 'up':
        y_new = y - CELL_SIZE
        y_new = 0 if y_new < 0 else y_new
    elif direction == 'down':
        y_new = y + CELL_SIZE
        y_new = CANVAS_HEIGHT - CELL_SIZE if y_new > CANVAS_HEIGHT - CELL_SIZE else y_new
    elif direction == 'left':
        x_new = x - CELL_SIZE
        x_new = 0 if x_new < 0 else x_new
    elif direction == 'right':
        x_new = x + CELL_SIZE
        x_new = CANVAS_WIDTH - CELL_SIZE if x_new > CANVAS_WIDTH - CELL_SIZE else x_new
    return x_new, y_new


def get_populations(group):
    populations = {}
    for org in group:
        if org.color in populations.keys():
            populations[org.color] += 1
        else:
            populations[org.color] = 1
    return populations