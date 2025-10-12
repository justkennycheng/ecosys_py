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
        super().tick(target_frame_time_v)

