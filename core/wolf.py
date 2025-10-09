# core/wolf.py
from core.organism import Organism
from core.state import RabbitState

class wolf(Organism):
    def __init__(self, id):
        super().__init__(id)
        self.state = RabbitState.Idle
        self.age = 0.0
        self.energy = 100.0
        self.hunger = 100.0

    def tick(self, delta_time):
        self.age += delta_time * 0.1
        self.hunger -= delta_time * 0.5
        self.energy -= delta_time * 0.3

        # 简化状态切换逻辑
        if self.hunger < 30:
            self.state = RabbitState.Foraging
        elif self.energy < 30:
            self.state = RabbitState.Resting
        else:
            self.state = RabbitState.Idle

