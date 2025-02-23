import pygame
import math
from collections import deque

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Bouncing Inside Rotating Hexagon")

# Colors (more natural palette)
CREAM = (245, 245, 220)  # Warm off-white background
FOREST_GREEN = (34, 139, 34)  # Natural green for hexagon
EARTH_ORANGE = (255, 140, 0)  # Softer orange for ball
SHADOW = (50, 50, 50, 100)  # Semi-transparent shadow

# Hexagon properties
center_x, center_y = WIDTH // 2, HEIGHT // 2
base_hex_radius = 100  # Base distance from center to vertex
angle = 0
rotation_speed = 0.5  # Degrees per frame
pulse_speed = 0.05  # Pulsing effect speed
pulse_amplitude = 5  # Slight size variation

# Ball properties
ball_radius = 10
ball_x, ball_y = center_x, center_y - 50  # Start near top
velocity_x, velocity_y = 5, 0  # Initial velocity
gravity = 0.3
bounce_factor = 0.991  # Near-perfect elasticity
trail = deque(maxlen=10)  # Trail for ball motion

# Game loop
clock = pygame.time.Clock()
running = True
pulse_time = 0

def line_intersection(p1, p2, p3, p4):
    """Calculate intersection point of two line segments, return None if no intersection."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denom
    if 0 <= t <= 1 and 0 <= u <= 1:
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        return (x, y)
    return None

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update rotation and pulse
    angle += rotation_speed
    angle %= 360
    pulse_time += pulse_speed
    hex_radius = base_hex_radius + math.sin(pulse_time) * pulse_amplitude

    # Calculate hexagon vertices
    hexagon_points = []
    for i in range(6):
        rad = math.radians(60 * i + angle)
        x = center_x + hex_radius * math.cos(rad)
        y = center_y + hex_radius * math.sin(rad)
        hexagon_points.append((x, y))

    # Apply gravity
    velocity_y += gravity

    # Proposed new position
    new_ball_x = ball_x + velocity_x
    new_ball_y = ball_y + velocity_y

    # Add current position to trail
    trail.append((ball_x, ball_y))

    # Collision detection and response
    collision_detected = False
    for i in range(6):
        p1 = hexagon_points[i]
        p2 = hexagon_points[(i + 1) % 6]

        # Wall vector and normal
        wall_dx = p2[0] - p1[0]
        wall_dy = p2[1] - p1[1]
        wall_length = math.hypot(wall_dx, wall_dy)
        normal_x = -wall_dy / wall_length
        normal_y = wall_dx / wall_length

        # Check distance from ball to wall
        to_wall_x = ball_x - p1[0]
        to_wall_y = ball_y - p1[1]
        dist_to_wall = to_wall_x * normal_x + to_wall_y * normal_y
        along_wall = to_wall_x * (wall_dx / wall_length) + to_wall_y * (wall_dy / wall_length)

        # Check collision
        if (abs(dist_to_wall) <= ball_radius and 0 <= along_wall <= wall_length and
                (velocity_x * normal_x + velocity_y * normal_y) < 0):
            # Reflect velocity
            dot_product = velocity_x * normal_x + velocity_y * normal_y
            velocity_x -= 2 * dot_product * normal_x
            velocity_y -= 2 * dot_product * normal_y
            velocity_x *= bounce_factor
            velocity_y *= bounce_factor

            # Correct position
            penetration = ball_radius - abs(dist_to_wall)
            ball_x += normal_x * penetration
            ball_y += normal_y * penetration
            collision_detected = True
            break

    # Update position if no collision
    if not collision_detected:
        ball_x, ball_y = new_ball_x, new_ball_y

    # Clear screen
    screen.fill(CREAM)

    # Draw shadow (slightly offset hexagon)
    shadow_points = [(x + 5, y + 5) for x, y in hexagon_points]
    pygame.draw.polygon(screen, SHADOW, shadow_points)

    # Draw hexagon
    pygame.draw.polygon(screen, FOREST_GREEN, hexagon_points, 0)  # Filled
    pygame.draw.polygon(screen, (20, 80, 20), hexagon_points, 2)  # Darker outline

    # Draw ball trail
    for i, (tx, ty) in enumerate(trail):
        alpha = int(255 * (i / len(trail)))  # Fade effect
        trail_surface = pygame.Surface((ball_radius * 2, ball_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(trail_surface, (*EARTH_ORANGE, alpha), (ball_radius, ball_radius), ball_radius)
        screen.blit(trail_surface, (int(tx - ball_radius), int(ty - ball_radius)))

    # Draw ball
    pygame.draw.circle(screen, EARTH_ORANGE, (int(ball_x), int(ball_y)), ball_radius)

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()