# main.py
import time
from core.controller import EcoController
from core.rabbit import Rabbit
from core.wolf import Wolf

def main():
    # 初始化控制器
    controller = EcoController()

    # 初始化种群（后续可从数据库读取）
    rabbits = [Rabbit(id=i) for i in range(10)]
    wolves = [Wolf(id=i) for i in range(3)]

    # 主循环
    while True:
        delta_time = 0.1  # 每次 tick 的时间步长（秒）
        controller.tick(delta_time, rabbits, wolves)

        # 打印状态（调试用）
        for r in rabbits:
            print(f"Rabbit {r.id}: age={r.age:.2f}, state={r.state.name}")
        for w in wolves:
            print(f"Wolf {w.id}: age={w.age:.2f}, state={w.state.name}")

        time.sleep(delta_time)

if __name__ == "__main__":
    main()
