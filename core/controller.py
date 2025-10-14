"""Module providing a function printing python version."""
import numpy as np
from utils.setting_loader import load_settings
# core/controller.py
class EcoController:
    """introduction"""
    def __init__(self):
        settings = load_settings()  # 加载配置文件
        self.map_settings = settings["environment"]
        self.grass_timer = 0.0
        self.grass_refresh_interval = settings["grass"]["refresh_interval"]
        self.grass_max_amount = settings["grass"]["max_amount"]
        self.grass_grow_amount = settings["grass"]["grow_amount_per_refresh"]
        self.grass_value = settings["grass"]["grass_value"]
        self.grass_positions = np.array([]) # 初始化一个空的 (0, 2) 形状数组
        self.refresh_grass()  #模拟世界的逻辑宽度        #更新草

    def tick(self, target_frame_time_v, rabbits, wolves):
        """introduction"""
        all_organisms = rabbits + wolves

        # 更新草
        self.grass_timer += target_frame_time_v
        if self.grass_timer >= self.grass_refresh_interval:
            self.refresh_grass()
            self.grass_timer = 0.0

        # 更新所有生物个体
        for r in rabbits:
            r.tick(target_frame_time_v , all_organisms)
        for w in wolves:
            w.tick(target_frame_time_v , all_organisms)

    def refresh_grass(self):
        """
        Grows a fixed amount of new grass, up to the maximum limit.
        """
        current_amount = self.grass_positions.shape[0]
        
        # Determine how much new grass to grow, capped by the remaining capacity.
        amount_to_grow = min(self.grass_grow_amount, self.grass_max_amount - current_amount)

        if amount_to_grow > 0:
            # Randomly generate new grass positions
            new_x = np.random.uniform(0, self.map_settings["map_width"], amount_to_grow)
            new_y = np.random.uniform(0, self.map_settings["map_height"], amount_to_grow)
            new_grass = np.stack((new_x, new_y), axis=1)

            # Add the new grass to the existing array
            if self.grass_positions.size > 0:
                self.grass_positions = np.concatenate([self.grass_positions, new_grass], axis=0)
            else:
                self.grass_positions = new_grass
                
            print(f"🌱 {amount_to_grow} grass grew. Total: {self.grass_positions.shape[0]}")
