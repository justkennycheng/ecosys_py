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
        # 调度器更新生态系统状态
        delta_time = timer.tick()   #获取上一帧开始到本帧开始的真实时间间隔
        simulation_speed = timer.simulation_speed   #当前仿真速度
        controller.tick(delta_time, rabbits, wolves)  #更新生态系统状态

        # 打印个体状态（调试用）
        for r in rabbits:
            print(f"🐰 Rabbit {r.id}: age={r.age:.2f}, hunger={r.hunger:.1f}, state={r.state.name}")
        for w in wolves:
            print(f"🐺 Wolf {w.id}: age={w.age:.2f}, hunger={w.hunger:.1f}, state={w.state.name}")

        # 控制仿真帧率
        timer.enforce_frame_rate()  # 补足剩余时间以控制帧率


        if time.time() - start_time > 3:  # 运行 3 秒后退出
            print("⏱️ 仿真已运行 3 秒，自动退出")
            break


if __name__ == "__main__":
    main()