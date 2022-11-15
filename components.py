import pygame

from pyces import Component
import systems


class CVisible(Component):  # gets an entity rendered
    def __init__(self, entity):
        super().__init__(self, system=systems.SRender())
        self.name = 'is_visible'
        self.entity = entity

    def setup(self):
        self.system.setup()
        if not self.entity.surface:
            self.entity.surface = pygame.Surface((32, 32))
            self.entity.surface.fill((255, 0, 255))
        self.system.scene.append(self.entity.surface)

    def update(self):
        self.system.update()

    def end(self):
        self.system.scene.remove(self.entity.surface)

