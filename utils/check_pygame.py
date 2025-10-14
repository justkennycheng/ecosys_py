import pygame

print(f"Pygame version: {pygame.version.ver}")

# 初始化 Pygame (必须步骤)
pygame.init()   # pylint: disable=no-member

# 定义窗口大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置窗口标题
pygame.display.set_caption("Pygame Test Window")

# 颜色定义 (R, G, B)
WHITE = (255, 255, 255)

# 游戏主循环
running = True
while running:
    # 事件处理循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # pylint: disable=no-member
            running = False

    # 填充屏幕背景色
    screen.fill(WHITE)

    # 刷新屏幕显示
    pygame.display.flip()

# 退出 Pygame
pygame.quit()   # pylint: disable=no-member
print("Pygame 窗口已关闭。")