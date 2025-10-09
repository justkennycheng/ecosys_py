# core/controller.py

class EcoController:
    def __init__(self):
        self.simulation_speed = 1.0
        self.grass_timer = 0.0
        self.grass_refresh_interval = 1.0
        self.max_grass_amount = 300
        self.grass_grow_amount = 2

    def tick(self, delta_time, rabbits, wolves):
        # 更新草（后续接入数据库）
        self.grass_timer += delta_time
        if self.grass_timer >= self.grass_refresh_interval / self.simulation_speed:
            self.refresh_grass()
            self.grass_timer = 0.0

        # 更新所有个体
        for r in rabbits:
            r.tick(delta_time * self.simulation_speed)
        for w in wolves:
            w.tick(delta_time * self.simulation_speed)

    def refresh_grass(self):
        print("🌱 Grass refreshed (stub)")
