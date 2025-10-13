"""Module providing a function printing python version."""
# core/Wolf.py
from core.organism import Organism

class Wolf(Organism):
    """introduction"""
    def __init__(self, settings):
        wolf_settings = settings["wolf"]
        super().__init__(wolf_settings)
        self.preditor_level = 1     #1级掠食者


    def tick(self, target_frame_time_v , all_organisms):
        """introduction"""
        super().tick(target_frame_time_v , all_organisms)

