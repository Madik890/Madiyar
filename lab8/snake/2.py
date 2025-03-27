import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки FPS
FPS = 15
FramePerSec = pygame.time.Clock()

# Константы
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
CELL_SIZE = 20
WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Классы игры
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # Начальное тело змейки
        self.direction = (CELL_SIZE, 0)  # Движение вправо
        self.grow = False

    def move(self):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])

        # Проверка столкновения со стенами
        if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
            return False  # Конец игры

        # Проверка столкновения с собой
        if head in self.body:
            return False

        self.body.insert(0, head)
        if not self.grow:
            self.body.pop()  # Удаляем последний сегмент, если не растём
        else:
            self.grow = False

        return True

    def change_direction(self, direction):
        if (direction[0] != -self.direction[0] or direction[1] != -self.direction[1]):
            self.direction = direction

    def grow_snake(self):
        self.grow = True

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self, snake_body):
        self.position = self.generate_position(snake_body)

    def generate_position(self, snake_body):
        while True:
            pos = (random.randint(0, (SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                   random.randint(0, (SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
            if pos not in snake_body:  # Еда не должна появляться на змее
                return pos

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (*self.position, CELL_SIZE, CELL_SIZE))

# Основной игровой цикл
snake = Snake()
food = Food(snake.body)
score, level = 0, 1
speed = 10
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -CELL_SIZE))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, CELL_SIZE))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-CELL_SIZE, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((CELL_SIZE, 0))

    # Движение змейки
    if not snake.move():
        running = False  # Завершаем игру при столкновении

    # Проверка на поедание еды
    if snake.body[0] == food.position:
        snake.grow_snake()
        food = Food(snake.body)
        score += 1

        # Увеличение уровня каждые 3 съеденных еды
        if score % 3 == 0:
            level += 1
            speed += 2  # Увеличение скорости

    # Отображение змеи, еды, очков и уровня
    snake.draw(screen)
    food.draw(screen)
    font = pygame.font.SysFont("Verdana", 20)
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))

    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()
