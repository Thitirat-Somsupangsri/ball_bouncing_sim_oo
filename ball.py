import math
import random


class Ball:
    def __init__(self, size, x, y, vx, vy, color, status):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.status = status

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def bounce(self, width, height):
        half_w = width // 2
        half_h = height // 2
        radius = self.size * 10
        if self.x + radius > half_w or self.x - radius < -half_w:
            self.vx = -self.vx
        if self.y + radius > half_h or self.y - radius < -half_h:
            self.vy = -self.vy

    def distance_to(self, x, y):
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)

    def reset_position(self, width, height):
        half_w = width // 2
        half_h = height // 2
        self.x = random.randint(-half_w + self.size*10, half_w - self.size*10)
        self.y = random.randint(-half_h + self.size*10, half_h - self.size*10)
