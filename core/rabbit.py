"""Module providing a function printing python version."""
# core/rabbit.py
from core.organism import Organism

class Rabbit(Organism):
    """introduction"""
    def __init__(self, settings):
        rabbit_settings = settings["rabbit"]
        super().__init__(rabbit_settings)


    def tick(self, target_frame_time_v):
        """introduction"""
        self.age += target_frame_time_v
        self.hunger -= target_frame_time_v * self.hunger_consume_rate
        self.energy -= target_frame_time_v * self.energy_consume_rate

        # 状态机