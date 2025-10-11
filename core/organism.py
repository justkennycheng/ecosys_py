"""Module providing a function printing python version."""
import random
from core.state import OrganismState
from utils.functions import calculate_scaled_value

# core/organism.py
class Organism:
    """introduction"""
    def __init__(self, o_id, settings):
        #基本属性
        self.o_id = o_id        # 实例属性,仅定义给具体实例
        self.position = ...     # 后续可接入 Vec3
        self.age = random.randint(0, settings['UL_lifetime'])
        self.ismale = random.randint(0, 1)
        self.health = 100.0     #暂不启用
        self.reproduction_countdown = 0.0
        self.state = OrganismState.Idle
        self.generation = 1
        #遗传属性
        self.growrate = ...
        self.hunger_desire = ...
        self.energy_desire = ...
        self.vision_range = ...
        self.search_range = ...
        self.standard_speed = ...
        self.standard_value = ...
        self.reproduction_cooldown_time = ...
        self.offspring_amount = ...
        self.sex_bias = ...
        self.flee_factor = ...
        self.pregant_dur = ...
        #固定属性
            #在固定属性yaml文件中
        #生成属性(根据其他属性计算得到的动态值)
        self.reproduce_age = ...               #成熟年龄。
        self.speed = ...           # 当前标准移动速度。通过CalculateSpeed()基于standardspeed生成,当前标准实际速度与年龄、能量有关。逃跑时速度X1.5
        self.value = ...           #被吃掉能提供的营养. 基于standrdvalue，通过CalculateValue()计算。
        self.max_hunger = self.calculate_max_hunger(settings)
             #当前年龄的最大饱腹度,依据当前年龄计算得出。 兔子幼年最大饱腹会降低，因而需要更频繁的进食。类似速度的算法。
        self.max_energy = self.calculate_max_energy(settings)
            #当前年龄的最大能量,依据当前年龄计算得出。 兔子幼年的最大能量会降低，因而需要更频繁的休息。
        self.hunger_TH = self.max_hunger * self.hunger_desire     #饥饿阈值  hungerThreshold = hungerDesireThreshold_factor * currentHungerUpperlimit
        self.energy_TH = self.max_energy * self.energy_desire      #能量阈值   energyThreshold = energyDesireThreshold_factor * currentEnergyUpperlimit
        self.offspring_amount = ...       #在当前繁殖的话能够出生的后代数量，使用CalculateOffspring()计算
        self.energy = ...
        self.hunger = ...

    def tick(self, target_frame_time_v):
        """introduction"""
        raise NotImplementedError("tick() must be implemented by subclass")
 
    def calculate_max_hunger(self, settings):
        """introduction"""
        return calculate_scaled_value(self.age, self.reproduce_age, settings['birth_max_hunger'], settings['UL_hunger'])

    def calculate_max_energy(self, settings):
        """introduction"""
        return calculate_scaled_value(self.age, self.reproduce_age, settings['birth_max_energy'], settings['UL_energy'])