import pygame
import sys
import random
import math

pygame.init()

# WINDOW
WIDTH = 500
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Ring Toss")

clock = pygame.time.Clock()

# COLORS
PINK = (255, 182, 193)
BLUE = (173, 216, 230)
WHITE = (255, 255, 255)
YELLOW = (255, 230, 120)

# CONTAINER
container_x = 50
container_y = 100
container_width = 400
container_height = 500

# RINGS
rings = []

for i in range(10):
    ring = {
        "x": random.randint(100, 400),
        "y": random.randint(250, 550),
        "radius": 12,
        "speed_y": 0,
        "speed_x": random.uniform(-1, 1)
    }

    rings.append(ring)

gravity = 0.15

# PEGS
pegs = [
    {"x": 180, "y": 250, "radius": 8},
    {"x": 250, "y": 220, "radius": 8},
    {"x": 320, "y": 250, "radius": 8},
]

while True:

    # EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # WATER PUSH
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                for ring in rings:
                    ring["speed_y"] = random.uniform(-4, -7)

    # UPDATE RINGS
    for ring in rings:

        # GRAVITY
        ring["speed_y"] += gravity

        # MOVE
        ring["y"] += ring["speed_y"]
        ring["x"] += ring["speed_x"]

        # WALL COLLISION
        left_limit = container_x + ring["radius"]
        right_limit = container_x + container_width - ring["radius"]

        if ring["x"] < left_limit:
            ring["x"] = left_limit
            ring["speed_x"] *= -1

        if ring["x"] > right_limit:
            ring["x"] = right_limit
            ring["speed_x"] *= -1

        # FLOOR COLLISION
        bottom_limit = container_y + container_height - ring["radius"]

        if ring["y"] > bottom_limit:
            ring["y"] = bottom_limit
            ring["speed_y"] *= -0.3

        # PEG COLLISION
        for peg in pegs:

            dx = ring["x"] - peg["x"]
            dy = ring["y"] - peg["y"]

            distance = math.sqrt(dx**2 + dy**2)

            # collision detected
            if distance < ring["radius"] + peg["radius"]:

                ring["speed_y"] *= -0.7

                # small random movement
                ring["speed_x"] += random.uniform(-1, 1)

    # DRAW
    screen.fill(BLUE)

    # CONTAINER
    pygame.draw.rect(
        screen,
        PINK,
        (container_x, container_y, container_width, container_height),
        border_radius=25
    )

    # PEGS
    for peg in pegs:

        pygame.draw.circle(
            screen,
            YELLOW,
            (peg["x"], peg["y"]),
            peg["radius"]
        )

    # RINGS
    for ring in rings:

        pygame.draw.circle(
            screen,
            WHITE,
            (int(ring["x"]), int(ring["y"])),
            ring["radius"],
            4
        )

    pygame.display.update()
    clock.tick(60)