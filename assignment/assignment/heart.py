import pygame
import sys

# 初始化 pygame
pygame.init()

# 设置窗口大小
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("点击爱心")

# 加载爱心图像
heart_image = pygame.image.load(r"E:\POLYU_SEM1\SD5913-Gio\assignment2\heart.png")  # 确保你有一个 heart.png 文件
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
            hearts.append((x, y))

    # 绘制背景
    screen.fill((255, 255, 255))

    # 绘制所有爱心
    for x, y in hearts:
        screen.blit(heart_image, (x - 25, y - 25))

    # 更新显示
    pygame.display.flip()

# 退出程序
pygame.quit()
sys.exit()