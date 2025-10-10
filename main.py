# main.py
import time
from core.controller import EcoController
from core.rabbit import Rabbit
from core.wolf import Wolf
from utils.timer import SimulationTimer


def main():
    
    timer = SimulationTimer(target_fps=2, simulation_speed=1.0)

    # 初始化控制器
    controller = EcoController()

    # 初始化种群（后续可从数据库读取）
    rabbits = [Rabbit(id=i) for i in range(10)]
    wolves = [Wolf(id=i) for i in range(3)]
    
    # 记录程序开始时间
    start_time = time.time()
    
    # 主循环
    while True:
        # 每帧开始：获取时间步长
        target_frame_time = timer.start_frame() # 真实时间步长（秒）
        simulation_speed = timer.simulation_speed   # 仿真速率倍率
        target_frame_time_V = target_frame_time * simulation_speed  # 虚拟时间步长

        # 调度器更新生态系统状态
        controller.tick(target_frame_time_V, rabbits, wolves)  #更新生态系统状态

        # 打印个体状态（调试用）
        for r in rabbits:
            print(f"🐰 Rabbit {r.id}: age={r.age:.2f}, hunger={r.hunger:.1f}, state={r.state.name}")
        for w in wolves:
            print(f"🐺 Wolf {w.id}: age={w.age:.2f}, hunger={w.hunger:.1f}, state={w.state.name}")

        # 每帧结束：补足剩余时间，保持帧率稳定
        timer.end_frame()



        if time.time() - start_time > 3:  # 运行 3 秒后退出
            print("⏱️ 仿真已运行 3 秒，自动退出")
            break


if __name__ == "__main__":
    main()