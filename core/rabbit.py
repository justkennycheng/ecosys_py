"""Module providing a function printing python version."""
# core/rabbit.py
from core.organism import Organism
from core.state import RabbitState

class Rabbit(Organism):
    """introduction"""
    def __init__(self, o_id , settings):
        super().__init__(o_id, settings)
        self.state = RabbitState.Idle
        self.age = 0.0
        self.energy = 100.0
        self.hunger = 100.0
        self.age_consume_rate = 0.1
        self.hunger_consume_rate = 0.5
        self.energy_consume_rate = 0.3

    def tick(self, target_frame_time_v):
        """introduction"""
        self.age += target_frame_time_v * self.age_consume_rate
        self.hunger -= target_frame_time_v * self.hunger_consume_rate
        self.energy -= target_frame_time_v * self.energy_consume_rate

        # 状态切换逻辑（简化版）
        if self.hunger < 30:
            self.state = RabbitState.Foraging
        elif self.energy < 30:
            self.state = RabbitState.Resting
        else:
            self.state = RabbitState.Idle
