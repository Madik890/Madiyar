import pygame
import random
import time
import psycopg2
import json

# === Подключение к БД ===
conn = psycopg2.connect(
    dbname="snake_game",
    user="postgres",
    password="e.madiar228",
    host="localhost",
    port="55555"
)
cur = conn.cursor()

# === Инициализация Pygame ===
pygame.init()
FPS = 10
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
CELL_SIZE = 20
WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# === База данных ===
def get_or_create_user(username):
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
        cur.execute("SELECT level, score FROM user_score WHERE user_id = %s", (user_id,))
        result = cur.fetchone()
        if result:
            return user_id, result[0], result[1]
        else:
            cur.execute("INSERT INTO user_score (user_id) VALUES (%s)", (user_id,))
            conn.commit()
            return user_id, 1, 0
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        cur.execute("INSERT INTO user_score (user_id) VALUES (%s)", (user_id,))
        conn.commit()
        return user_id, 1, 0

# === Классы ===
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (CELL_SIZE, 0)
        self.grow = False

    def move(self):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
            return False
        if head in self.body:
            return False
        self.body.insert(0, head)
        if not self.grow:
            self.body.pop()
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
        self.timer = pygame.time.get_ticks()
        self.lifetime = 3000
        self.weight = random.randint(1, 5)

    def generate_position(self, snake_body):
        while True:
            pos = (random.randint(0, (SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                   random.randint(0, (SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
            if pos not in snake_body:
                return pos

    def is_expired(self):
        return pygame.time.get_ticks() - self.timer > self.lifetime

    def draw(self, surface):
        if not self.is_expired():
            pygame.draw.rect(surface, RED, (*self.position, CELL_SIZE, CELL_SIZE))

# === Ввод пользователя ===
username = input("Enter your username: ")
user_id, level, score = get_or_create_user(username)
speed = 10 + (level - 1) * 2

# === Основной игровой цикл ===
snake = Snake()
food = Food(snake.body)
running = True
paused = False

while running:
    screen.fill(WHITE)

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
            elif event.key == pygame.K_p:
                paused = not paused
                if paused:
                    print("Game Paused. Saving...")
                    cur.execute("""
                        UPDATE user_score
                        SET score = %s, level = %s, game_state = %s, last_updated = NOW()
                        WHERE user_id = %s
                    """, (score, level, json.dumps({"snake": snake.body, "food": food.position}), user_id))
                    conn.commit()
                    print("Game Saved.")

    if paused:
        continue

    if not snake.move():
        print("Game Over")
        running = False

    if snake.body[0] == food.position:
        snake.grow_snake()
        score += food.weight
        if score % 3 == 0:
            level += 1
            speed += 2
        food = Food(snake.body)

    if food.is_expired():
        food = Food(snake.body)

    snake.draw(screen)
    food.draw(screen)
    font = pygame.font.SysFont("Verdana", 20)
    screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, BLACK), (10, 30))

    pygame.display.update()
    FramePerSec.tick(speed)

pygame.quit()
cur.close()
conn.close()
