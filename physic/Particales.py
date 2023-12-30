import pygame
import sys
import random
import math

# Constants
WIDTH, HEIGHT = 800, 600
PARTICLE_RADIUS = 20
SPEED = 5
FUSION_DISTANCE = 2 * PARTICLE_RADIUS

# Particle class
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.angle = 0  # Move in the same line
        self.color = color

    def update(self):
        self.x += SPEED * math.cos(self.angle)
        self.y += SPEED * math.sin(self.angle)

        # Collision with walls
        if self.x <= PARTICLE_RADIUS or self.x >= WIDTH - PARTICLE_RADIUS:
            self.angle = math.pi - self.angle
        if self.y <= PARTICLE_RADIUS or self.y >= HEIGHT - PARTICLE_RADIUS:
            self.angle = -self.angle

def distance(particle1, particle2):
    return math.sqrt((particle1.x - particle2.x)**2 + (particle1.y - particle2.y)**2)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Fusion Simulation")

# Create two particles
particle1 = Particle(WIDTH // 4, HEIGHT // 2, (255, 0, 0))  # Red
particle2 = Particle(3 * WIDTH // 4, HEIGHT // 2, (0, 0, 255))  # Blue

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update particles
    particle1.update()
    particle2.update()

    # Check for collision
    if distance(particle1, particle2) < FUSION_DISTANCE:
        # Create a new particle at the midpoint of collision with a new color
        new_particle_x = (particle1.x + particle2.x) // 2
        new_particle_y = (particle1.y + particle2.y) // 2
        new_particle_color = ((particle1.color[0] + particle2.color[0]) // 2,
                              (particle1.color[1] + particle2.color[1]) // 2,
                              (particle1.color[2] + particle2.color[2]) // 2)
        new_particle = Particle(new_particle_x, new_particle_y, new_particle_color)

        # Draw particles
        screen.fill((255, 255, 255))  # White background
        pygame.draw.circle(screen, new_particle.color, (int(new_particle.x), int(new_particle.y)), PARTICLE_RADIUS)
    else:
        # Draw particles
        screen.fill((255, 255, 255))  # White background
        pygame.draw.circle(screen, particle1.color, (int(particle1.x), int(particle1.y)), PARTICLE_RADIUS)
        pygame.draw.circle(screen, particle2.color, (int(particle2.x), int(particle2.y)), PARTICLE_RADIUS)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
