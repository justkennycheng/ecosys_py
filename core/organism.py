# core/organism.py
class Organism:
    def __init__(self, id, settings):
        self.id = id
        self.position = None  # 后续可接入 Vec3
        self.state = None
        self.age = 0.0
        self.energy = 100.0
        self.hunger = 100.0
        self.is_alive = True

    def tick(self, effective_time):
        raise NotImplementedError("tick() must be implemented by subclass")