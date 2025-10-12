"""Module providing a function printing python version."""
# utils/timer.py
import time

class SimulationTimer:
    """introduction"""
    def __init__(self, target_fps=60, simulation_speed=1.0):
        self.target_frame_time = 1.0 / target_fps  # 每帧真实时间步长（秒）
        self.simulation_speed = simulation_speed   # 仿真速率倍率
        self.total_simulation_time = 0.0           # 累计虚拟时间
        self.current_frame_start = None            # 当前帧开始时间
        self.frame_runtime = 0.0                   # 当前帧耗时
        self.sleep_time = 0.0                      # 本帧最后的休眠时间

    def start_frame(self):
        """
        在每帧开始前调用，记录开始时间。
        返回真实时间步长（target_frame_time），供 controller 使用。
        """
        self.current_frame_start = time.perf_counter()
        return self.target_frame_time

    def end_frame(self):
        """
        在每帧结束后调用，计算执行耗时并补足剩余时间。
        更新 frame_runtime。
        """
        now = time.perf_counter()
        self.frame_runtime = now - self.current_frame_start
        self.sleep_time = max(0.0, self.target_frame_time - self.frame_runtime)
        time.sleep(self.sleep_time)

        # 更新累计仿真时间
        self.total_simulation_time += self.target_frame_time * self.simulation_speed

    def set_speed(self, new_speed: float):
        """introduction"""
        self.simulation_speed = new_speed

    def get_total_simulation_time(self):
        """introduction"""
        return self.total_simulation_time

    def get_frame_runtime(self):
        """introduction"""
        return self.frame_runtime
