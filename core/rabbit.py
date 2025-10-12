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
        super().tick(target_frame_time_v)

