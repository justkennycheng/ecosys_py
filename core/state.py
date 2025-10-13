"""Module providing a function printing python version."""
import enum

class OrganismState(enum.Enum):
    """定义生物体的各种状态"""
    IDLE = 0
    FORAGING = 1
    FLEEING = 2
    RESTING = 3
    REPRODUCING = 4
    DEAD = 5

class State:
    """
    这是一个所有状态的“基类”或“模板”。
    """

    def enter(self, agent):
        """进入此状态时执行的代码"""
        pass  # pass 表示什么也不做，具体功能留给子类去实现

    def execute(self, agent, all_organisms):
        """每个循环更新时执行的代码（主要逻辑）"""
        pass  # 留给子类去实现

    def exit(self, agent):
        """离开此状态时执行的代码"""
        pass  # 留给子类去实现

# ==================================
#         Concrete States
# ==================================

class IdleState(State):
    """
    生物空闲时的状态。根据生物的需求转换到其他状态。
    """
    def execute(self, agent , all_organisms):
        # 饱腹度低的生物应该开始觅食
        if agent.if_needs_to_forage():
            return ForagingState()
        
        # 能量低的生物应该开始休息
        if agent.if_needs_to_rest():
            return RestingState()

        #检查四周是否有威胁需要逃跑
        if agent.if_treathen_detected(all_organisms):
            return FleeingState()
        
        # 如果没有紧急需求，就四处闲逛
        # 我们假设 agent 对象上未来会有一个 wander() 方法
        agent.wander()

        # 返回 None 表示继续保持当前状态
        return None

class ForagingState(State):
    """
    生物觅食时的状态。
    """
    def execute(self, agent, all_organisms):
        # 1. 安全第一：检查是否有天敌
        # if agent.is_predator_nearby():
        #     return FleeingState()
        pass # 暂不实现

        # 2. 检查是否吃饱
        # if agent.is_full():
        #     return IdleState()
        pass # 暂不实现

        # 3. 寻找食物
        # food = agent.find_food()
        # if food:
        #     pass # 走向食物
        # else:
        #     pass # 闲逛
        pass # 暂不实现

        return None # 暂时保持觅食状态

class FleeingState(State):
    """
    生物逃跑时的状态。
    """
    def execute(self, agent, all_organisms):
        # 1. 找到最近的天敌
        # predator = agent.find_nearest_predator()
        # if predator:
        #     # 2. 朝反方向高速移动
        #     agent.move_away_from(predator)
        # else:
        #     # 3. 天敌消失，切换回空闲状态
        #     return IdleState()
        pass # 暂不实现
 
        return None # 暂时保持逃跑状态

class RestingState(State):
    """
    生物休息时的状态，用于恢复能量。
    """
    def execute(self, agent, all_organisms):
        # 1. 休息时也要警惕天敌
        # if agent.is_predator_nearby():
        #     return FleeingState()
 
        # 2. 恢复能量
        # agent.recover_energy()

        # 3. 如果能量满了，切换回空闲状态
        # if agent.is_energy_full():
        #     return IdleState()
        pass # 暂不实现

        return None # 暂时保持休息状态

class ReproducingState(State):
    """
    生物繁殖时的状态。
    """
    def execute(self, agent, all_organisms):
        # 1. 繁殖时也要警惕天敌
        # if agent.is_predator_nearby():
        #     return FleeingState()
 
        # 2. 寻找配偶
        # mate = agent.find_mate()
        # if mate:
        #     # 3. 繁殖
        #     agent.reproduce_with(mate)
        #     return IdleState() # 繁殖后进入空闲
        # else:
        #     # 4. 没找到配偶，闲逛
        #     agent.wander()
        pass # 暂不实现

        return None # 暂时保持繁殖状态

class DeadState(State):
    """死亡状态的占位符"""
    def execute(self, agent, all_organisms):
        # 死亡的生物什么也不做
        pass
