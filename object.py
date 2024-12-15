import random
from ball import Ball


class Snow(Ball):
    def __init__(self, screen, size=4, x=None, y=None,
                 vx=None, vy=None, color="white"):
        if screen is None:
            raise ValueError("Screen must be provided")
        half_w = screen.window_width() // 2
        half_h = screen.window_height() // 2
        x = x if x is not None else random.randint(-half_w + size*10, half_w - size*10)
        y = y if y is not None else random.randint(-half_h + size*10, half_h - size*10)
        vx = vx if vx is not None else random.uniform(-5, 5)
        vy = vy if vy is not None else random.uniform(-5, 5)
        super().__init__(size, x, y, vx, vy, color, status="player")


class Fire(Ball):
    def __init__(self, screen, size=3, x=None, y=None,
                 vx=None, vy=None, color="red"):
        if screen is None:
            raise ValueError("Screen must be provided")
        half_w = screen.window_width() // 2
        half_h = screen.window_height() // 2
        x = x if x is not None else random.randint(-half_w + size*10, half_w - size*10)
        y = y if y is not None else random.randint(-half_h + size*10, half_h - size*10)
        vx = vx if vx is not None else random.uniform(-5, 5)
        vy = vy if vy is not None else random.uniform(-5, 5)
        super().__init__(size, x, y, vx, vy, color, status="enemy")
