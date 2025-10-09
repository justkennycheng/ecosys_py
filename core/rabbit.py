# core/rabbit.py
from core.organism import Organism
from core.state import RabbitState

class Rabbit(Organism):
    def __init__(self, id):
        super().__init__(id)
        self.state = RabbitState.Idle
        self.age = 0.0
        self.energy = 100.0
        self.hunger = 100.0
        self.age_consume_rate = 0.1
        self.hunger_consume_rate = 0.5
        self.energy_consume_rate = 0.3

    def tick(self, effective_time):
        # 更新基本属性
        self.age += effective_time * self.age_consume_rate
        self.hunger -= effective_time * self.hunger_consume_rate
        self.energy -= effective_time * self.energy_consume_rate

        # 状态切换逻辑（简化版）
        if self.hunger < 30:
            self.state = RabbitState.Foraging
        elif self.energy < 30:
            self.state = RabbitState.Resting
        else:
            self.state = RabbitState.Idle