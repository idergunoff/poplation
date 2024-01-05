from func import *
from organism import world


# Функция для отображения цифрового табло
def show_era(era, screen):
    font = pygame.font.Font(None, 40)
    text = font.render(f'ERA: {era}', True, (0, 0, 0))
    screen.blit(text, (20, 20))
    text = font.render(f'ORG: {len(world.sprites())}', True, (0, 0, 0))
    screen.blit(text, (20, 100))


def show_gen(x, y, screen):
    font = pygame.font.Font(None, 40)
    current_organism = get_sprite_at_position(world, x, y)
    if not current_organism:
        return

    text = font.render(f'health: {current_organism.health}', True, (0, 0, 0))
    screen.blit(text, (20, CANVAS_HEIGHT - 240))
    text = font.render(f'lifetime: {current_organism.lifetime}', True, (0, 0, 0))
    screen.blit(text, (20, CANVAS_HEIGHT - 200))
    text = font.render(f'food: {current_organism.food}', True, (0, 0, 0))
    screen.blit(text, (20, CANVAS_HEIGHT - 160))
    text = font.render(f'collect: {current_organism.collect}', True, (0, 0, 0))
    screen.blit(text, (20, CANVAS_HEIGHT - 120))
    text = font.render(f'attack: {current_organism.attack}', True, (0, 0, 0))
    screen.blit(text, (20, CANVAS_HEIGHT - 80))
    text = font.render(f'rest: {current_organism.rest}', True, (0, 0, 0))
    screen.blit(text, (20, CANVAS_HEIGHT - 40))
    text = font.render(f'color: {current_organism.color}', True, (0, 0, 0))
    screen.blit(text, (20, CANVAS_HEIGHT - 280))


def show_legend(screen, dict_ppl):
    n = 0
    font = pygame.font.Font(None, 40)
    sorted_ppl = dict(sorted(dict_ppl.items(), key=lambda x: x[1], reverse=True))
    for key, value in sorted_ppl.items():
        pygame.draw.rect(screen, key, (CANVAS_WIDTH + 20, 20 + n * 60, 80, 40))
        text = font.render(str(value), True, (0, 0, 0))
        screen.blit(text, (CANVAS_WIDTH + 100, 20 + n * 60))
        n += 1
    text = font.render(f'PPL: {len(dict_ppl)}', True, (0, 0, 0))
    screen.blit(text, (20, 60))