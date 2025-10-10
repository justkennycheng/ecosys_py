"""Module providing a function printing python version."""
# core/organism.py
class Organism:
    """introduction"""
    def __init__(self, o_id, settings):
        self.o_id = o_id
        self.position = None  # 后续可接入 Vec3
        self.state = None
        self.age = 0.0
        self.energy = 100.0
        self.hunger = 100.0
        self.is_alive = True

    def tick(self, target_frame_time_v):
        """introduction"""
        raise NotImplementedError("tick() must be implemented by subclass")
