# core/Wolf.py
from core.organism import Organism
from core.state import WolfState

class Wolf(Organism):
    def __init__(self, id):
        super().__init__(id)
        self.state = WolfState.Idle
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
            self.state = WolfState.Foraging
        elif self.energy < 30:
            self.state = WolfState.Resting
        else:
            self.state = WolfState.Idle