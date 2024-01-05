from func import *

class Energy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Вызов конструктора родительского класса
        pygame.sprite.Sprite.__init__(self)
        # Создание изображения спрайта
        self.image = pygame.Surface([CELL_SIZE, CELL_SIZE])
        self.color = (255, 255, 255)
        self.image.fill(self.color)
        # Получение прямоугольника, который ограничивает спрайт
        self.rect = self.image.get_rect()
        # Установка начальной позиции спрайта
        self.rect.x = x
        self.rect.y = y
        self.power = 0

    def update(self):
        if self.power < MAX_POWER and self.power >= 0:
            # получаем значение вероятности от 0 до 100
            chance = random.randint(0, 100)
            if chance > 75:
                self.power += 1
            # elif 75 >= chance > 50:
            #     self.power += 3
            # elif 50 >= chance > 25:
            #     self.power -= 2
            # elif 25 >= chance > 0:
            #     self.power -= 1
            # self.power = 0 if self.power < 0 else self.power
            # if chance > 50:
            #     self.power += 0
            # elif 50 >= chance > 25:
            #     self.power += 1
            # elif 25 >= chance > 10:
            #     self.power += 2
            # elif 10 >= chance > 1:
            #     self.power += 3
            # elif 1 >= chance >= 0:
            #     self.power += 10
        self.color = get_brown_shade(int(self.power/(MAX_POWER/10)))
        self.image.fill(self.color)



energies = pygame.sprite.Group()

