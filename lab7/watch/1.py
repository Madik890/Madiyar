import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

mickey_body = pygame.image.load("clock.png")
right_hand = pygame.image.load("min_hand.png")
left_hand = pygame.image.load("sec_hand.png")

mickey_body = pygame.transform.scale(mickey_body, (300, 300))
right_hand = pygame.transform.scale(right_hand, (200, 300))
left_hand = pygame.transform.scale(left_hand, (300, 300))

center_x, center_y = WIDTH // 2, HEIGHT // 2

running = True
while running:
    screen.fill((0, 0, 0))  
    
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    minute_angle = - (minutes * 6)  
    second_angle = - (seconds * 6)  
    
    rotated_right_hand = pygame.transform.rotate(right_hand, minute_angle)
    rotated_left_hand = pygame.transform.rotate(left_hand, second_angle)
    
    screen.blit(mickey_body, (center_x - 150, center_y - 150))
    
    right_hand_rect = rotated_right_hand.get_rect(center=(center_x, center_y))
    left_hand_rect = rotated_left_hand.get_rect(center=(center_x, center_y))
    
    screen.blit(rotated_right_hand, right_hand_rect)
    screen.blit(rotated_left_hand, left_hand_rect)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(100)

pygame.quit()
