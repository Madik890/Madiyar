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
current_tool = "pen"  # Текущий инструмент
color = BLACK  # Начальный цвет
radius = 5  # Размер кисти или ластика
start_pos = None  # Начальная позиция для рисования фигур

# Функция для рисования различных фигур
def draw_shape(screen, tool, color, start_pos, end_pos):
    if tool == "rectangle":  # Рисование прямоугольника
        pygame.draw.rect(screen, color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
    elif tool == "circle":  # Рисование круга
        radius = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])) // 2
        pygame.draw.circle(screen, color, start_pos, radius, 2)
    elif tool == "square":  # Рисование квадрата
        side_length = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))  # Сторона квадрата
        pygame.draw.rect(screen, color, (*start_pos, side_length, side_length), 2)
    elif tool == "right_triangle":  # Рисование прямоугольного треугольника
        points = [start_pos, (end_pos[0], start_pos[1]), (start_pos[0], end_pos[1])]
        pygame.draw.polygon(screen, color, points, 2)
    elif tool == "equilateral_triangle":  # Рисование равностороннего треугольника
        height = abs(end_pos[0] - start_pos[0]) * (3 ** 0.5) / 2  # Высота равностороннего треугольника
        points = [
            start_pos,
            (start_pos[0] + (end_pos[0] - start_pos[0]) / 2, start_pos[1] - height),
            (end_pos[0], start_pos[1])
        ]
        pygame.draw.polygon(screen, color, points, 2)
    elif tool == "rhombus":  # Рисование ромба
        width = abs(end_pos[0] - start_pos[0])  # Ширина ромба (горизонтальная диагональ)
        height = abs(end_pos[1] - start_pos[1])  # Высота ромба (вертикальная диагональ)

        # Находим центр ромба (среднюю точку между начальной и конечной позицией)
        center_x, center_y = (start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2

        # Вычисление координат четырёх углов ромба с учетом диагоналей
        points = [
            (center_x, start_pos[1]),  # Верхняя точка ромба
            (start_pos[0], center_y),  # Левая точка ромба
            (center_x, end_pos[1]),  # Нижняя точка ромба
            (end_pos[0], center_y)  # Правая точка ромба
        ]

    # Рисование ромба
    pygame.draw.polygon(screen, color, points, 2)


# Основной игровой цикл
def main():
    global current_tool, color, radius, start_pos
    screen.fill(WHITE)
    running = True

    # Цикл для обработки событий
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Изменение текущего инструмента по нажатию клавиш
                if event.key == pygame.K_p:
                    current_tool = "pen"  # Кисть
                elif event.key == pygame.K_l:
                    current_tool = "rectangle"  # Прямоугольник
                elif event.key == pygame.K_c:
                    current_tool = "circle"  # Круг
                elif event.key == pygame.K_e:
                    current_tool = "eraser"  # Ластик
                elif event.key == pygame.K_r:
                    current_tool = "rectangle"  # Прямоугольник
                elif event.key == pygame.K_q:
                    current_tool = "square"  # Квадрат
                elif event.key == pygame.K_t:
                    current_tool = "right_triangle"  # Прямоугольный треугольник
                elif event.key == pygame.K_y:
                    current_tool = "equilateral_triangle"  # Равносторонний треугольник
                elif event.key == pygame.K_u:
                    current_tool = "rhombus"  # Ромб
                elif event.key == pygame.K_r:
                    color = RED  # Красный цвет
                elif event.key == pygame.K_g:
                    color = GREEN  # Зелёный цвет
                elif event.key == pygame.K_b:
                    color = BLUE  # Синий цвет

            # Обработка события нажатия кнопки мыши
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos
                if current_tool == "pen":
                    pygame.draw.circle(screen, color, event.pos, radius)  # Рисование кистью
                elif current_tool == "eraser":
                    pygame.draw.circle(screen, WHITE, event.pos, radius)  # Ластик

            # Обработка движения мыши при зажатой кнопке
            elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                if current_tool == "pen":
                    pygame.draw.circle(screen, color, event.pos, radius)  # Рисование кистью
                elif current_tool == "eraser":
                    pygame.draw.circle(screen, WHITE, event.pos, radius)  # Ластик

            # Завершение рисования фигур
            elif event.type == pygame.MOUSEBUTTONUP:
                if current_tool in ["rectangle", "circle", "square", "right_triangle", "equilateral_triangle", "rhombus"] and start_pos:
                    draw_shape(screen, current_tool, color, start_pos, event.pos)
                    start_pos = None  # Сброс начальной позиции

        pygame.display.update()  # Обновление экрана
        clock.tick(60)  # Частота кадров

    pygame.quit()  # Закрытие Pygame

# Запуск программы
if __name__ == "__main__":
    main()
