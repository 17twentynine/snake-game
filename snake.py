import pygame

pygame.display.set_caption('Snake IO')

game_window = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

snake_start_x = 0
snake_start_y = 0
block_height = 40
block_width = 40

snake_blocks = []
for block in range(5):
    snake_blocks.append( (snake_start_x + (block * block_height), snake_start_y) )

cl = green
running = True

def tick():
    global running, snake_blocks, cl
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                snake_blocks.pop(0)
                x, y = snake_blocks[-1]
                snake_blocks.append((x + block_width, y))
            elif event.key == pygame.K_LEFT or event.key == ord('a'):
                snake_blocks.pop(-1)
                x, y = snake_blocks[0]
                snake_blocks.insert(0, (x - block_width, y))
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                snake_blocks.pop(0)
                x, y = snake_blocks[-1] 
                snake_blocks.append((x, y + block_height))
            elif event.key == pygame.K_UP or event.key == ord('e'):
                snake_blocks.pop(0)
                x, y = snake_blocks[-1] 
                snake_blocks.append((x, y - block_height))

        game_window.fill(black)

        for idx, (block_x, block_y) in enumerate(snake_blocks):
            if idx == len(snake_blocks) - 1:
                cl = blue
            else:
                cl = green
            pygame.draw.rect(game_window, cl, pygame.Rect(block_x, block_y, block_width-2, block_height-2))

        # Refresh game screen
        pygame.display.update()

        # Refresh rate
        # clock.tick(60)

if __name__ == "__main__":
    while running:
        tick()
    pygame.quit()