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
    controller = EcoController()

    # 记录程序开始时间
    start_time = time.time()

    # 主循环
    while True:
        # 每帧开始：获取时间步长
        target_frame_time = timer.start_frame() # 真实时间步长（秒）
        simulation_speed = timer.simulation_speed   # 仿真速率倍率
        target_frame_time_v = target_frame_time * simulation_speed  # 虚拟时间步长
        # 1/fps * speed = speed / fps = 虚拟步长
        # 即，仿真速度/帧率 = 虚拟步长 = 仿真精度
        # 虚拟步长越大，每一次计算中系统的动作步长就越大（动物走的越远，饥饿和能量下降越多），模拟的精度越差。
        # 因而为了保障仿真精度，如果增加了仿真速度，最好也增加帧率。

        # 调度器更新生态系统状态
        controller.tick(target_frame_time_v, rabbits, wolves)  #更新生态系统状态

        # 打印个体状态（调试用）
        for r in rabbits:
            sex = 'M' if r.ismale else 'F'
            print(f"🐰 Rabbit id={r.o_id} gen={r.generation} {sex} state={r.state.name} | age={r.age:.1f}, speed={r.speed:.2f}, hunger={r.hunger:.1f}, energy={r.energy:.1f}")
        for w in wolves:
            sex = 'M' if w.ismale else 'F'
            print(f"🐺 Wolf  id={w.o_id} gen={w.generation} {sex} state={w.state.name} | age={w.age:.1f}, speed={w.speed:.2f}, hunger={w.hunger:.1f}, energy={w.energy:.1f}")

        # 每帧结束：补足剩余时间，保持帧率稳定
        timer.end_frame()

        # 打印帧状态（调试用）
        print(f"[STATS] FPS: {settings['simulation']['target_fps']} | Speed: {timer.simulation_speed}x |Target_frame_time: {timer.target_frame_time:.8f}s | Runtime: {timer.frame_runtime:.8f}s | Sleep: {timer.sleep_time:.8f}s")

        # 运行结束后提示（调试用）
        if time.time() - start_time > settings["simulation"]["total_duration"]:  # 运行 到仿真时长后退出
            print(f"⏱️ 仿真已运行 {settings["simulation"]["total_duration"]} 秒，自动退出")
            break


if __name__ == "__main__":
    main()
