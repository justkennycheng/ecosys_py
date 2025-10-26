"""Module providing a function printing python version."""
# core/rabbit.py
from core.organism import Organism

class Rabbit(Organism):
    """introduction"""
    def __init__(self, settings):
        rabbit_settings = settings["rabbit"]
        rabbit_settings["map_width"] = settings["environment"]["map_width"]
        rabbit_settings["map_height"] = settings["environment"]["map_height"]
        rabbit_settings["grass_value"] = settings["grass"]["grass_value"]
        super().__init__(rabbit_settings)
        self.preditor_level = 0     #0表示不是掠食者
        


    def tick(self, target_frame_time_v , all_organisms):
        """introduction"""
        super().tick(target_frame_time_v , all_organisms)

