import pygame
import sys
import time
import math
import random

# 初始化 pygame
pygame.init()

# 设置窗口大小
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("点击爱心")

# 加载爱心图像
heart_image = pygame.image.load(r"E:\POLYU_SEM1\SD5913-Gio\assignment2\heart.png")
heart_image = pygame.transform.scale(heart_image, (50, 50))

# 程序主循环
running = True
hearts = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 获取鼠标点击位置
            x, y = event.pos
            # 将当前时间、位置和随机偏移量存储为元组
            hearts.append((x, y, time.time(), random.uniform(-0.5, 0.5)))

    # 绘制背景
    screen.fill((255, 255, 255))

    # 绘制所有爱心
    current_time = time.time()
    new_hearts = []

    for x, y, start_time, x_offset in hearts:
        elapsed_time = current_time - start_time
        if elapsed_time < 1:  # 一秒内逐渐消失
            y_offset = elapsed_time * 50  # 调整上升速度
            alpha = max(0, 255 - int(elapsed_time * 255))  # 计算透明度
            angle = math.sin(elapsed_time * 2 * math.pi) * 10  # 旋转角度

            # 调整随机左右移动速度
            x += x_offset * 0.1  # 减小移动幅度

            heart = pygame.transform.rotate(heart_image, angle)
            heart.set_alpha(alpha)
            rect = heart.get_rect(center=(x, y - y_offset))
            screen.blit(heart, rect.topleft)
            new_hearts.append((x, y, start_time, x_offset))

    hearts = new_hearts

    # 更新显示
    pygame.display.flip()

# 退出程序
pygame.quit()
sys.exit()