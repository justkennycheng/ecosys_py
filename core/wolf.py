"""Module providing a function printing python version."""
# core/Wolf.py
from core.organism import Organism

class Wolf(Organism):
    """introduction"""
    def __init__(self, settings):
        wolf_settings = settings["wolf"]
        super().__init__(wolf_settings)


    def tick(self, target_frame_time_v):
        """introduction"""
        self.age += target_frame_time_v
        self.hunger -= target_frame_time_v * self.hunger_consume_rate
        self.energy -= target_frame_time_v * self.energy_consume_rate

        # 状态机

