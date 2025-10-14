"""Module providing a function printing python version."""
#init.py
class InitManager:
    """
    初始化管理器：负责初始化生态系统中的各种对象。
    """

    @classmethod    # 类方法，方法作用于类本身
    def init_rabbits(cls, settings: dict):
        """
        初始化兔子种群。
        :param settings: 配置字典，包含种群数量信息。
        :return: 兔子列表。
        """
        from core.rabbit import Rabbit

        # 从配置中获取兔子数量
        num_rabbits = settings["population"]["initial_rabbits"]

        # 初始化兔子列表
        rabbits = []  # 创建一个空列表来存储兔子对象
        for _ in range(num_rabbits):
            rabbit = Rabbit(settings)  # 创建一个 Rabbit 对象
            rabbits.append(rabbit)  # 将 Rabbit 对象添加到列表中

        return rabbits  # 返回兔子列表

    @classmethod    # 类方法，方法作用于类本身
    def init_wolves(cls, settings: dict):
        """
        初始化狼种群。
        :param settings: 配置字典，包含种群数量信息。
        :return: 狼列表。
        """
        from core.wolf import Wolf

        # 从配置中获取狼数量
        num_wolves = settings["population"]["initial_wolves"]

        # 初始化狼列表
        wolves = []     # 创建一个空列表来存储狼对象
        for _ in range(num_wolves):
            wolf = Wolf(settings)  # 创建一个 Wolf 对象
            wolves.append(wolf)  # 将 Wolf 对象添加到列表中

        return wolves  # 返回狼列表
