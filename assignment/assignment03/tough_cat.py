import pygame
import sys
import time
import math
import random

# Initialize pygame
pygame.init()

# Set window size
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("点击爱心")

# Load heart image
heart_image = pygame.image.load(r"E:\POLYU_SEM1\SD5913_Gio\pfad\assignment\assignment03\assets\heart.png")
heart_image = pygame.transform.scale(heart_image, (50, 50))

# Load and scale cat image
cat_image_original = pygame.image.load(r"E:\POLYU_SEM1\SD5913_Gio\pfad\assignment\assignment03\assets\cat.png")
cat_image_original = pygame.transform.scale(cat_image_original, (150, 150))

# Load sound effect
click_sound = pygame.mixer.Sound(r"E:\POLYU_SEM1\SD5913_Gio\pfad\assignment\assignment03\assets\Touch Sound _Cute.mp3")

# Load background music
pygame.mixer.music.load(r"E:\POLYU_SEM1\SD5913_Gio\pfad\assignment\assignment03\assets\cute-music-26476.mp3")
pygame.mixer.music.play(-1)  # -1 for infinite loop

# Cat properties
cat_pos = [random.randint(0, width - 150), random.randint(0, height - 150)]
click_count = 0
click_target = random.randint(5, 12)
shake_duration = 0.1  # Shake duration
last_shake_time = 0

# Main loop
running = True
hearts = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse click position
            x, y = event.pos

            # Check if cat is clicked
            cat_rect = cat_image_original.get_rect(topleft=cat_pos)
            if cat_rect.collidepoint(x, y):
                click_sound.play()
                click_count += 1
                last_shake_time = time.time()

                # Check click count
                if click_count >= click_target:
                    click_count = 0
                    click_target = random.randint(5, 15)
                    cat_pos = [random.randint(0, width - 150), random.randint(0, height - 150)]

            # Store current time, position, and random offset as a tuple
            hearts.append((x, y, time.time(), random.uniform(-1.0, 1.0)))

    # Draw background
    screen.fill((255, 255, 255))

    # Check shake time
    if time.time() - last_shake_time < shake_duration:
        scale_factor = 1.1  # Scale up
    else:
        scale_factor = 1.0  # Normal size

    # Generate shaking cat image
    cat_image = pygame.transform.scale(
        cat_image_original,
        (int(150 * scale_factor), int(150 * scale_factor))
    )
    cat_rect = cat_image.get_rect(center=(cat_pos[0] + 75, cat_pos[1] + 75))

    # Draw cat
    screen.blit(cat_image, cat_rect.topleft)

    # Draw hearts
    current_time = time.time()
    new_hearts = []

    for x, y, start_time, x_offset in hearts:
        elapsed_time = current_time - start_time
        if elapsed_time < 1:  # Fade out over one second
            y_offset = elapsed_time * 50
            alpha = max(0, 255 - int(elapsed_time * 255))
            angle = math.sin(elapsed_time * 2 * math.pi) * 10

            # Adjust random sideways movement speed
            x += x_offset * 0.1

            heart = pygame.transform.rotate(heart_image, angle)
            heart.set_alpha(alpha)
            rect = heart.get_rect(center=(x, y - y_offset))
            screen.blit(heart, rect.topleft)
            new_hearts.append((x, y, start_time, x_offset))

    hearts = new_hearts

    # Update display
    pygame.display.flip()

# Quit program
pygame.quit()
sys.exit()