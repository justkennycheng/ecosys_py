# main.py
import time
from core.controller import EcoController
from core.rabbit import Rabbit
from core.wolf import Wolf

def main():
    # 仿真参数
    delta_time = 0.1              # 每轮 tick 的真实时间步长（秒）
    simulation_speed = 1.0        # 仿真倍率（虚拟世界时间流速）

    # 初始化控制器
    controller = EcoController(simulation_speed)

    # 初始化种群（后续可从数据库读取）
    rabbits = [Rabbit(id=i) for i in range(10)]
    wolves = [Wolf(id=i) for i in range(3)]

    # 主循环
    while True:
        # 调度器更新生态系统状态
        controller.tick(delta_time, rabbits, wolves)

        # 打印个体状态（调试用）
        for r in rabbits:
            print(f"🐰 Rabbit {r.id}: age={r.age:.2f}, hunger={r.hunger:.1f}, state={r.state.name}")
        for w in wolves:
            print(f"🐺 Wolf {w.id}: age={w.age:.2f}, hunger={w.hunger:.1f}, state={w.state.name}")

        # 控制仿真节奏
        time.sleep(delta_time)

if __name__ == "__main__":
    main()