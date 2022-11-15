import sys
import time
import pygame
from pyces import *
from components import *
from entities import *

entity_list = []
root = ERoot()
root_component = Component()


def setup():
    for entity in entity_list:
        entity.setup()


def run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        frame_time = time.time()
        for entity in entity_list:
            entity.update()
        while time.time() < frame_time + 1/10:
            pass


def end():
    for entity in entity_list:
        entity.end()
        entity_list.remove(entity)


def main():
    world = Entity(name='world', parent=root)
    player = Entity(name='player', parent=world)
    player.add_component(CVisible(player))
    entity_list.append(world)
    entity_list.append(player)

    setup()
    run()
    end()


if __name__ == "__main__":
    main()

