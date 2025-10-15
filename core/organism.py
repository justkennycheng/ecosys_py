"""Module providing a function printing python version."""
import random
import numpy as np
from core.state import IdleState
from utils import functions as func


# core/organism.py
class Organism:
    """introduction"""
    _next_id = 0
    def __init__(self, settings):
        #基本属性
        self.o_id = Organism._next_id
        Organism._next_id += 1
        # 实例属性,仅定义给具体实例
        self.map_width = settings['map_width']
        self.map_height = settings['map_height']
        self.position = np.array([random.uniform(0, self.map_width),random.uniform(0, self.map_height)])
        angle = random.uniform(0, 2 * np.pi)
        self.direction = np.array([np.cos(angle), np.sin(angle)])
        self.dt = 0.0
        self.ismale = random.randint(0, 1)
        self.health = 100.0     #暂不启用
        self.reproduction_countdown = 0.0
        self.state = IdleState() # <-- 使用状态对象
        self.generation = 1     #整数
        self.parent_id = None
        self.death_age = None
        self.death_reason = None
        self.preditor_level = -1  # 捕食者等级,0表示非捕食者
        self.species = None        #物种名称，如rabbit、wolf等
        #遗传属性
        self.reproduce_age = settings['init_reproduce_age']          #成熟年龄,秒。代替之前的的growrate
        self.hunger_desire = settings['init_hunger_desire']          #饱腹值的百分之多少开始去觅食
        self.energy_desire = settings['init_energy_desire']
        self.life_time = settings['init_life_time']
        self.vision_range = settings['init_vision_range']
        self.search_range = settings['init_search_range']
        self.standard_speed = settings['init_standard_speed']
        self.standard_value = settings['init_standard_value']
        self.reproduction_cooldown_time = settings['init_reproduction_cooldown_time']
        self.offspring_amount = settings['init_offspring_amount']
        self.givebirth_sex_bias = settings['init_givebirth_sex_bias']
        self.flee_factor = settings['init_flee_factor']
        self.flee_speed_factor = settings['init_flee_speed_factor']
        self.pregant_dur = settings['init_pregant_dur']
        #补全固定属性[避免向tick()传递settings]
        self.UL_life_time = settings['UL_life_time']
        self.LL_life_time = settings['LL_life_time']
        self.UL_hunger = settings['UL_hunger']
        self.UL_energy = settings['UL_energy']
        self.birth_max_hunger = settings['birth_max_hunger']
        self.birth_max_energy = settings['birth_max_energy']
        self.UL_speed = settings['UL_speed']
        self.LL_speed = settings['LL_speed']
        self.birth_value = settings['birth_value']
        self.hunger_consume_rate = settings['hunger_consume_rate']
        self.energy_consume_rate = settings['energy_consume_rate']
        self.energy_recovery_rate = settings['energy_recovery_rate']
        #生成属性(根据其他属性计算得到的初始值)
        self.age = func.get_random_normal(self.life_time / 2, self.life_time / 6, 0, self.life_time)
        self.speed = func.calculate_peak_value(self.age, self.reproduce_age, self.life_time, self.LL_speed, self.standard_speed)
            # 当前标准移动速度。通过CalculateSpeed()基于standardspeed生成,当前标准实际速度与年龄、能量有关。逃跑时速度X1.5
        self.value = func.calculate_scaled_value(self.age, self.reproduce_age, self.birth_value, self.standard_value)
            #被吃掉能提供的营养. 基于standrdvalue，随年龄增加，成熟时达到最大。value还用于区分动物的体型大小，用于猎物被捕获的概率。
        self.max_hunger = func.calculate_scaled_value(self.age, self.reproduce_age, self.birth_max_hunger, self.UL_hunger)
             #当前年龄的最大饱腹度,，随年龄增加，成熟时达到最大。 兔子幼年最大饱腹会降低，因而需要更频繁的进食。类似速度的算法。
        self.max_energy = func.calculate_scaled_value(self.age, self.reproduce_age, self.birth_max_energy, self.UL_energy)
            #当前年龄的最大能量,，随年龄增加，成熟时达到最大。 兔子幼年的最大能量会降低，因而需要更频繁的休息。
        self.hunger_TH = self.max_hunger * self.hunger_desire     #饥饿阈值  hungerThreshold = hungerDesireThreshold_factor * currentHungerUpperlimit
        self.energy_TH = self.max_energy * self.energy_desire      #能量阈值   energyThreshold = energyDesireThreshold_factor * currentEnergyUpperlimit
        self.givebirth_amount = func.calculate_peak_value(self.age, self.reproduce_age, self.life_time, 1, self.offspring_amount)
            #在当前繁殖的话能够出生的后代数量;使用了peak函数，但是程序机制在成年前不会繁殖所以可以使用这个函数。
        self.energy = self.max_hunger    #刚好用阈值初始化
        self.hunger = self.max_energy    #刚好用阈值初始化

    def tick(self, target_frame_time_v , all_organisms):
        """introduction"""

        #以后这里增加动态调整属性的代码

        self.dt = target_frame_time_v  # 将时间增量存储起来，以便其他方法使用

        self.age += target_frame_time_v
        self.hunger -= target_frame_time_v * self.hunger_consume_rate
        self.energy -= target_frame_time_v * self.energy_consume_rate

        #在这里增加是否饿死的代码
        
        # 状态机
        new_state = self.state.execute(self, all_organisms)    #这个execute()必须返回值，或者返回新的状态对象，或者返回None表示状态不变。
        if new_state is not None:
            self.state.exit(self)
            self.state = new_state
            self.state.enter(self)

    ###################################################################

    def if_needs_to_forage(self):
        """Checks if the organism's hunger is below its threshold."""
        return self.hunger < self.hunger_TH

    def if_needs_to_rest(self):
        """Checks if the organism's energy is below its threshold."""
        return self.energy < self.energy_TH

    def if_treathen_detected(self, all_organisms):
        """
        检查在自己的视野范围内是否有捕食者。
        捕食者的定义是任何 `preditor_level` 高于自己的生物。
        """
        # 遍历所有生物
        for other in all_organisms:
            # 检查对方是否是自己的捕食者
            if other.preditor_level > self.preditor_level:
                # 计算与捕食者之间的距离
                distance = np.linalg.norm(self.position - other.position)
                # 如果捕食者进入了视野范围，则视为威胁
                if distance < self.vision_range:
                    return True
        # 没有发现威胁
        return False

    def wander(self):
        """
        实现随机闲逛行为。
        生物会稍微改变其方向然后前进。
        """
        # 给方向向量增加一个小的随机“抖动”
        # 这个抖动向量的每个分量范围是 [-0.25, 0.25]
        jitter = (np.random.rand(2) - 0.5) * 0.5
        self.direction += jitter    #加上jitter向量会改变方向（同时也改变长度）

        # 重新归一化方向向量以保持速度恒定
        self.direction /= np.linalg.norm(self.direction)

        # 根据方向、速度和时间增量来更新位置
        self.position = self.position + self.direction * self.speed * self.dt

        # 边界检查 (简单的环绕效果)
        # 假设世界大小是 200x200
        self.position = np.mod(self.position, [self.map_width, self.map_height])  #从一侧超出地图，则从另一侧出现

    def find_nearest_grass(self, grass_positions):
        """
        向量化计算与所有草地的距离，并找到最近的一块草地。
        :param grass_positions: 形状为 (N, 2) 的 NumPy 数组，包含所有草地位置。
        :return: 最近草地的位置 (np.array)
        """
        if grass_positions.size == 0:
            return None
        
        # 1. 向量化减法：计算兔子位置与所有草地位置的差向量
        #    结果是形状为 (N, 2) 的数组
        #    self.position 是 (2,) 形状，NumPy 的广播机制自动处理
        difference = grass_positions - self.position
        # 2. 向量化求范数：计算每个差向量的欧几里得距离（L2 范数）
        #    np.linalg.norm(..., axis=1) 对每一行（即每一个差向量）求范数
        #    结果是形状为 (N,) 的距离数组
        distances = np.linalg.norm(difference, axis=1)
        # 3. 找到最小距离的索引
        min_index = np.argmin(distances)
        # 4. 根据索引获取最近草地的位置
        nearest_grass_pos = grass_positions[min_index]
        # 5. 可选：检查最近的草地是否在兔子的视野范围内
        min_distance = distances[min_index]
        if min_distance <= self.vision_range:
            return nearest_grass_pos
        else:
            return None # 视野内没有草


        
        
        ###