"""Module providing a function printing python version."""
import numpy as np
from utils.setting_loader import load_settings
# core/controller.py
class EcoController:
    """introduction"""
    def __init__(self):
        """
        初始化函数，用于设置初始参数和加载配置
        """
        settings = load_settings()  # 加载配置文件
        self.map_settings = settings["environment"]
        self.grass_timer = 0.0
        self.grass_refresh_interval = settings["grass"]["refresh_interval"]
        self.grass_max_amount = settings["grass"]["max_amount"]
        self.grass_grow_amount = settings["grass"]["grow_amount_per_refresh"]
        self.grass_value = settings["grass"]["grass_value"]
        self.grass_positions = np.array([]) # 初始化一个空的 (0, 2) 形状数组
        self.refresh_grass()  #更新草

    def tick(self, target_frame_time_v, rabbits, wolves):
        """introduction"""
        all_organisms = rabbits + wolves

        # 更新草
        self.grass_timer += target_frame_time_v
        if self.grass_timer >= self.grass_refresh_interval:
            self.refresh_grass()    # 更新草
            self.grass_timer = 0.0

        # 更新所有生物个体
        for r in rabbits:
            r.tick(target_frame_time_v , all_organisms)
            r.grass_positions = self.grass_positions    # 为食草动物更新草地位置,可以不用每次tick都更新
        for w in wolves:
            w.tick(target_frame_time_v , all_organisms)

        # 处理被吃掉的食物
        for r in rabbits:
            if r.last_eaten_food is not None:
                if r.last_eaten_food["food_type"] == "grass" and r.last_eaten_food["food_index"] is not None:
                    # 移除被吃掉的草地
                    self.grass_positions = np.delete(self.grass_positions, r.last_eaten_food["food_index"], axis=0)
                # 重置最近吃掉的食物信息
                r.last_eaten_food = None

        for w in wolves:
            if w.last_eaten_food is not None:
                if w.last_eaten_food["food_type"] == "organism" and w.last_eaten_food["food_index"] is not None:
                    # 移除被吃掉的猎物
                    prey_index = w.last_eaten_food["food_index"]
                    # 确保索引有效
                    if 0 <= prey_index < len(all_organisms):
                        prey = all_organisms[prey_index]
                        # 从all_organisms列表中移除猎物
                        all_organisms.remove(prey)
                        # 从相应的类型列表中移除猎物
                        if prey in rabbits:
                            rabbits.remove(prey)
                        elif prey in wolves:
                            wolves.remove(prey)
                # 重置最近吃掉的食物信息
                w.last_eaten_food = None

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
