"""Module providing a function printing python version."""
import random
import numpy as np
from core.state import OrganismState, IdleState, ForagingState, FleeingState, RestingState, ReproducingState, DeadState
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
        self.position = self.position = np.array([random.uniform(0, 100), random.uniform(0, 100)])
        self.ismale = random.randint(0, 1)
        self.health = 100.0     #暂不启用
        self.reproduction_countdown = 0.0
        self.state = IdleState() # <-- 使用状态对象
        self.generation = 1     #整数
        self.parent_id = None
        self.death_age = None
        self.death_reason = None
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
        self.energy = self.hunger_TH    #刚好用阈值初始化
        self.hunger = self.energy_TH    #刚好用阈值初始化

    def if_needs_to_forage(self):
        """Checks if the organism's hunger is below its threshold."""
        return self.hunger < self.hunger_TH

    def if_needs_to_rest(self):
        """Checks if the organism's energy is below its threshold."""
        return self.energy < self.energy_TH
    
    def if_treathen_detected(self , all_organisms):
        """检查是否有猎食者."""
        pass
    
    def wander(self):
        """
        Makes the organism move randomly.
        (Currently a placeholder with no logic).
        """
        pass
        

    def tick(self, target_frame_time_v , all_organisms):
        """introduction"""
        self.age += target_frame_time_v
        self.hunger -= target_frame_time_v * self.hunger_consume_rate
        self.energy -= target_frame_time_v * self.energy_consume_rate

        # 状态机
        new_state = self.state.execute(self, all_organisms)    #这个execute()必须返回值，或者返回新的状态对象，或者返回None表示状态不变。
        if new_state is not None:
            self.state.exit(self)
            self.state = new_state
            self.state.enter(self)

        ###