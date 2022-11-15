class Component:
    component_next = -1

    def __init__(self, name='default_component', system=None):
        self.name = name
        self.system = system
        self.id = Component.component_next
        Component.component_next += 1

    def setup(self):
        self.system.setup()

    def update(self):
        self.system.update()

    def end(self):
        self.system.end()


class Entity:
    entity_next = -1

    def __init__(self, name='default_entity', parent=None, components=[]):
        self.id = Entity.entity_next
        self.name = name
        self.parent = parent
        self.components = components
        Entity.entity_next += 1
        self.surface = None

    def add_component(self, component):  # component in form of component obj returned from component index dict
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def setup(self):
        for component in self.components:
            component.setup()

    def update(self):
        for component in self.components:
            component.update()

    def end(self):
        for component in self.components:
            component.end()


class System:
    def __init__(self, name='default_system', parent=None):
        self.name = name
        self.parent = parent

    def setup(self):
        pass

    def update(self):
        pass

    def end(self):
        pass
