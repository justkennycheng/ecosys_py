# core/controller.py
class EcoController:
    def __init__(self, simulation_speed=1.0):
        self.simulation_speed = simulation_speed
        self.grass_timer = 0.0
        self.grass_refresh_interval = 1.0
        self.max_grass_amount = 300
        self.grass_grow_amount = 2

    def tick(self, delta_time, rabbits, wolves):
        # 计算虚拟世界中流逝的时间
        effective_time = delta_time * self.simulation_speed

        # 更新草（后续接入数据库）
        self.grass_timer += effective_time
        if self.grass_timer >= self.grass_refresh_interval:
            self.refresh_grass()
            self.grass_timer = 0.0

        # 更新所有个体
        for r in rabbits:
            r.tick(effective_time)
        for w in wolves:
            w.tick(effective_time)

    def refresh_grass(self):
        print("🌱 Grass refreshed (stub)")