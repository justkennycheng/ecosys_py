"""Module providing a function printing python version."""
# core/controller.py
class EcoController:
    """introduction"""
    def __init__(self , settings):
        self.grass_timer = 0.0
        self.grass_refresh_interval = 1.0
        self.max_grass_amount = 300
        self.grass_grow_amount = 2

    def tick(self, target_frame_time_v, rabbits, wolves):
        """introduction"""
        # 更新草（后续接入数据库）
        self.grass_timer += target_frame_time_v
        if self.grass_timer >= self.grass_refresh_interval:
            self.refresh_grass()
            self.grass_timer = 0.0

        # 更新所有个体
        for r in rabbits:
            r.tick(target_frame_time_v)
        for w in wolves:
            w.tick(target_frame_time_v)

    def refresh_grass(self):
        """introduction"""
        print("🌱 Grass refreshed (stub)")
