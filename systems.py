import pygame
from pyces import System


class SRender(System):      # Owns the output display surface, manages
    def __init__(self, x_res=800, y_res=600, resizeable=True):
        super().__init__(self)
        self.display_size = x_res, y_res
        if resizeable:
            self.flags = pygame.RESIZABLE
        else:
            self.flags = None
        self.render_out = None
        self.scene = []

    def setup(self):
        self.render_out = pygame.display.set_mode(self.display_size, self.flags)

    def update(self):
        self.render_out.fill((0, 0, 0))     # Reset the screen to black
        for surface in self.scene:
            rect = surface.get_rect
            self.render_out.blit(self.render_out, rect)
        pygame.display.flip()

    def end(self):
        pass
