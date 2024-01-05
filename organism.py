from func import *
from energy import energies


# создаем класс Организм
class Organism(pygame.sprite.Sprite):
    def __init__(self, x, y, health, lifetime, food, collect, attack, rest, color):
        # Вызов конструктора родительского класса
        pygame.sprite.Sprite.__init__(self)
        # Создание изображения спрайта
        self.image = pygame.Surface([CELL_SIZE, CELL_SIZE])
        self.color = color
        self.image.fill(self.color)
        # Получение прямоугольника, который ограничивает спрайт
        self.rect = self.image.get_rect()
        # Установка начальной позиции спрайта
        self.rect.x = x
        self.rect.y = y
        # ген организма
        self.health = health
        self.lifetime = lifetime
        self.food = food
        self.collect = collect
        self.attack = attack
        self.rest = rest

        self.current_health = health
        self.current_lifetime = lifetime
        self.current_rest = rest

    def death(self):
        energy_block = get_sprite_at_position(energies, self.rect.x, self.rect.y)
        energy_block.power += random.randint(0, self.health)
        energy_block.power = MAX_POWER if energy_block.power > MAX_POWER else energy_block.power
        energy_block.color = get_brown_shade(int(energy_block.power/(MAX_POWER/10)))
        energy_block.image.fill(self.color)
        self.kill()

    def move(self):
        x_new, y_new = get_new_position(self.rect.x, self.rect.y)
        enemy_organism = get_sprite_at_position(world, x_new, y_new)
        if enemy_organism:
            self.fight(enemy_organism)
        else:
            self.rect.x = x_new
            self.rect.y = y_new
            self.current_rest = self.rest

    def fight(self, enemy_organism):
        if self.attack + self.current_health > enemy_organism.attack + enemy_organism.current_health:
            enemy_organism.death()
            self.rect.x = enemy_organism.rect.x
            self.rect.y = enemy_organism.rect.y
            # self.current_health += enemy_organism.health
        else:
            self.death()


    def birth(self):
        list_dir = ['up', 'down', 'left', 'right']
        while list_dir:
            dir = random.choice(list_dir)
            x_birth, y_birth = get_birth_position(dir, self.rect.x, self.rect.y)
            if not get_sprite_at_position(world, x_birth, y_birth):
                rnd_val = random.randint(0, 1000)
                if rnd_val < 2:
                    list_gen = ['health', 'lifetime', 'food', 'collect', 'attack', 'rest']
                    mutate_gen1 = random.choice(list_gen)
                    list_gen.remove(mutate_gen1)
                    mutate_gen2 = random.choice(list_gen)
                    mutate_val = random.randint(1, 3)
                    self.__dict__[mutate_gen1] += mutate_val
                    self.__dict__[mutate_gen2] -= mutate_val
                    self.__dict__[mutate_gen2] = 1 if self.__dict__[mutate_gen2] < 1 else self.__dict__[mutate_gen2]
                    self.color = get_color_organism(self.health, self.lifetime, self.food, self.collect, self.attack, self.rest)
                new_organism = Organism(x_birth, y_birth, self.health, self.lifetime, self.food, self.collect, self.attack, self.rest, self.color)
                world.add(new_organism)
                self.current_health = self.health
                break
            else:
                list_dir.remove(dir)
        if list_dir == []:
            self.current_health = self.health


    def update(self):
        if self.current_lifetime <= 0:
            self.death()
            return
        if self.current_rest != 0:
            self.current_rest -= 1
        energy_block = get_sprite_at_position(energies, self.rect.x, self.rect.y)
        if energy_block is None:
            return
        if energy_block.power > self.collect:
            energy_block.power -= self.collect
            self.current_health += self.collect
        else:
            self.current_health += energy_block.power
            energy_block.power = 0
            if self.current_rest == 0:
                self.move()

        if self.current_health >= self.health * 2:
            self.birth()

        if self.current_health <= 0:
            self.death()

        self.current_lifetime -= 1

        if random.choice([True, False]) or energy_block.power < self.food:
            self.current_health -= self.food
        else:
            energy_block.power -= self.food

        # for key, value in list(populations.items()):
        #     if value < 1:
        #         del populations[key]

world = pygame.sprite.Group()



