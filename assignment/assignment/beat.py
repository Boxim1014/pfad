import pygame
import random

# 初始化Pygame
pygame.init()

# 设置窗口尺寸
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("模型震动示例")

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)

# 矩形参数
rect_width, rect_height = 100, 50
rect_x, rect_y = (width - rect_width) // 2, (height - rect_height) // 2

# 震动参数
shake_intensity = 5
shake_duration = 500  # 以毫秒为单位

running = True
shaking = False
shake_start_time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect_x <= event.pos[0] <= rect_x + rect_width and rect_y <= event.pos[1] <= rect_y + rect_height:
                shaking = True
                shake_start_time = pygame.time.get_ticks()

    screen.fill(white)

    # 震动效果
    if shaking:
        current_time = pygame.time.get_ticks()
        if current_time - shake_start_time < shake_duration:
            offset_x = random.randint(-shake_intensity, shake_intensity)
            offset_y = random.randint(-shake_intensity, shake_intensity)
            pygame.draw.rect(screen, black, (rect_x + offset_x, rect_y + offset_y, rect_width, rect_height))
        else:
            shaking = False
            pygame.draw.rect(screen, black, (rect_x, rect_y, rect_width, rect_height))
    else:
        pygame.draw.rect(screen, black, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.flip()

pygame.quit()