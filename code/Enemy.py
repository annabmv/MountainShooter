from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIND_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.vertical_direction = -1  # 1 for moving down, -1 for moving up

    def move(self):
        if self.name == 'Enemy3':
            # Move horizontally from right to left
            self.rect.centerx -= ENTITY_SPEED[self.name]
            # Move vertically with a "bounce" effect
            self.rect.centery += ENTITY_SPEED[self.name] * self.vertical_direction

            # Change direction if hitting the screen boundaries
            if self.rect.top <= 0:
                self.vertical_direction = 2  # Move down faster
            elif self.rect.bottom >= WIND_HEIGHT:
                self.vertical_direction = -1  # Move up

        else:
            # Default movement for other enemies
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
