from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    # pygame draw methods
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    # Split method for when shot
    def split(self) -> None:
        self.kill()
        if self.radius is ASTEROID_MIN_RADIUS:
            return None
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        first_new_asteroid = Asteroid(
            self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS
        )
        first_new_asteroid.velocity = self.velocity.rotate(split_angle) * 1.2
        second_new_asteroid = Asteroid(
            self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS
        )
        second_new_asteroid.velocity = self.velocity.rotate(-split_angle) * 1.2
