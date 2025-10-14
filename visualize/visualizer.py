"""视图配置"""
import pygame
from utils.setting_loader import load_settings

# --- 模拟世界配置 ---
# 根据 organism.py 中的边界检查，假设世界大小是 200x200
settings = load_settings()  # 加载配置文件
SIM_WIDTH = settings["environment"]["map_width"]     #模拟世界的逻辑宽度
SIM_HEIGHT = settings["environment"]["map_height"]    #模拟世界的逻辑宽度

# --- Pygame 窗口配置 ---
SCREEN_WIDTH = settings["environment"]["screen_width"]  # 屏幕像素宽度
SCREEN_HEIGHT = settings["environment"]["screen_height"] # 屏幕像素高度
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
TITLE = "Rabbit-Wolf-Grass Simulation"

# --- 颜色定义 ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)   # 狼
BLUE = (0, 0, 255)  # 兔子
GREEN = (0, 150, 0) # 草

# --- 绘图常量 ---
WOLF_RADIUS = 4
RABBIT_RADIUS = 2
GRASS_RADIUS = 1

class Visualizer:
    """
    处理所有基于 Pygame 的生态系统模拟可视化。
    """
    def __init__(self):
        """初始化 Pygame、屏幕, 并计算缩放比例。"""
        pygame.init()   # pylint: disable=no-member
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)
        # 计算缩放因子，用于将模拟坐标映射到屏幕坐标
        self.x_scale = SCREEN_WIDTH / SIM_WIDTH
        self.y_scale = SCREEN_HEIGHT / SIM_HEIGHT

    def _convert_pos(self, sim_pos):
        """将模拟世界的坐标 (numpy array) 转换为屏幕像素坐标 (tuple)。"""
        screen_x = int(sim_pos[0] * self.x_scale)
        screen_y = int(sim_pos[1] * self.y_scale)
        return (screen_x, screen_y)

    def draw(self, rabbits, wolves, grass_positions):
        """
        将整个模拟状态绘制到屏幕上。
        这包括处理事件、清空屏幕和绘制所有对象。
        如果用户退出，则返回 False，否则返回 True。
        """
        # 1. 处理 Pygame 事件（例如关闭窗口）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # pylint: disable=no-member
                return False  # 发送信号给主循环，让其退出

        # 2. 用背景色填充屏幕
        self.screen.fill(BLACK)

        # 3. 绘制所有的草
        for pos in grass_positions:
            pygame.draw.circle(self.screen, GREEN, self._convert_pos(pos), GRASS_RADIUS)

        # 4. 绘制所有的兔子
        for rabbit in rabbits:
            pygame.draw.circle(self.screen, BLUE, self._convert_pos(rabbit.position), RABBIT_RADIUS)

        # 5. 绘制所有的狼
        for wolf in wolves:
            pygame.draw.circle(self.screen, RED, self._convert_pos(wolf.position), WOLF_RADIUS)

        # 6. 更新显示，以展示新绘制的帧
        pygame.display.flip()

        return True  # 发送信号给主循环，表示继续运行

    def close(self):
        """关闭 Pygame 模块。"""
        pygame.quit()   # pylint: disable=no-member
