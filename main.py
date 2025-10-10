"""Module providing a function printing python version."""
# main.py
import time
from utils.setting_loader import load_settings
from utils.timer import SimulationTimer
from core.controller import EcoController
from core.init import InitManager

def main():
    """introduction"""
    settings = load_settings()  # 加载配置文件

    timer = SimulationTimer(settings["simulation"]["target_fps"] , settings["simulation"]["simulation_speed"])

    # 初始化种群（通过InitManager调用类方法）
    rabbits = InitManager.init_rabbits(settings)
    wolves = InitManager.init_wolves(settings)

    # 初始化控制器
    controller = EcoController(settings)

    # 记录程序开始时间
    start_time = time.time()

    # 主循环
    while True:
        # 每帧开始：获取时间步长
        target_frame_time = timer.start_frame() # 真实时间步长（秒）
        simulation_speed = timer.simulation_speed   # 仿真速率倍率
        target_frame_time_v = target_frame_time * simulation_speed  # 虚拟时间步长

        # 调度器更新生态系统状态
        controller.tick(target_frame_time_v, rabbits, wolves)  #更新生态系统状态

        # 打印个体状态（调试用）
        for r in rabbits:
            print(f"🐰 Rabbit {r.o_id}: age={r.age:.2f}, hunger={r.hunger:.1f}, state={r.state.name}")
        for w in wolves:
            print(f"🐺 Wolf {w.o_id}: age={w.age:.2f}, hunger={w.hunger:.1f}, state={w.state.name}")

        # 每帧结束：补足剩余时间，保持帧率稳定
        timer.end_frame()

        # 运行时间限制（调试用）
        if time.time() - start_time > settings["simulation"]["total_duration"]:  # 运行 到仿真时长后退出
            print(f"⏱️ 仿真已运行 {settings["simulation"]["total_duration"]} 秒，自动退出")
            break


if __name__ == "__main__":
    main()
