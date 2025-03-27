import pygame

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint Program")

# Переменные
clock = pygame.time.Clock()
current_tool = "pen"
color = BLACK
radius = 5  # Размер кисти или ластика
start_pos = None

def draw_shape(screen, tool, color, start_pos, end_pos):
    if tool == "rectangle":
        pygame.draw.rect(screen, color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
    elif tool == "circle":
        radius = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])) // 2
        pygame.draw.circle(screen, color, start_pos, radius, 2)

def main():
    global current_tool, color, radius, start_pos
    screen.fill(WHITE)
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    current_tool = "pen"
                elif event.key == pygame.K_l:
                    current_tool = "rectangle"
                elif event.key == pygame.K_c:
                    current_tool = "circle"
                elif event.key == pygame.K_e:
                    current_tool = "eraser"
                elif event.key == pygame.K_r:
                    color = RED
                elif event.key == pygame.K_g:
                    color = GREEN
                elif event.key == pygame.K_b:
                    color = BLUE
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos
                if current_tool == "pen":
                    pygame.draw.circle(screen, color, event.pos, radius)
                elif current_tool == "eraser":
                    pygame.draw.circle(screen, WHITE, event.pos, radius)
            
            elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                if current_tool == "pen":
                    pygame.draw.circle(screen, color, event.pos, radius)
                elif current_tool == "eraser":
                    pygame.draw.circle(screen, WHITE, event.pos, radius)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if current_tool in ["rectangle", "circle"] and start_pos:
                    draw_shape(screen, current_tool, color, start_pos, event.pos)
                    start_pos = None
        
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
