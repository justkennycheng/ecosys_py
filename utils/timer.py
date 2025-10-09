# utils/timer.py
import time

class SimulationTimer:
    def __init__(self, target_fps=60, simulation_speed=1.0):
        self.simulation_speed = simulation_speed
        self.target_frame_time = 1.0 / target_fps  # 每帧目标时间（秒）
        self.last_real_time = time.time()
        self.total_simulation_time = 0.0

    def tick(self):
        """
        每轮调用一次，返回虚拟世界中本轮的时间步长。
        自动控制帧率，确保每轮间隔接近目标帧时间。
        """
        current_time = time.time()

        # 计算真实时间间隔
        delta_real_time = current_time - self.last_real_time
        self.last_real_time = current_time

        # 计算虚拟时间步长
        delta_simulation_time = delta_real_time * self.simulation_speed
        self.total_simulation_time += delta_simulation_time

        return delta_simulation_time  # 返回虚拟时间间隔


    def enforce_frame_rate(self):
        """
        在每轮结束后调用，补足剩余时间以控制帧率。
        """
        elapsed = time.time() - self.last_real_time
        sleep_time = max(0.0, self.target_frame_time - elapsed)
        time.sleep(sleep_time)

    def set_speed(self, new_speed: float):
        self.simulation_speed = new_speed

    def get_total_simulation_time(self):
        return self.total_simulation_time