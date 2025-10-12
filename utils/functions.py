"""这里放置了一些通用函数"""
import random
# utils/functions.py

def calculate_scaled_value(current_age, max_age_for_growth, min_value, max_value):
    """
    计算一个随年龄线性增长的值，在达到成年年龄之前线性增长，成年后变为最大值。

    参数:
    current_age (int): 当前年龄。
    max_age_for_growth (int): 停止生长的年龄 (例如 reproduce_age)。
    min_value (float): 0岁时的初始值 (例如 birth_max_hunger)。
    max_value (float): 达到或超过生長上限年龄时的最大值 (例如 UL_hunger)。

    返回:
    float: 根据当前年龄计算出的值。
    """
    # 如果已达到或超过生長上限年龄，或者上限年龄无效，则直接返回值
    if current_age >= max_age_for_growth or max_age_for_growth <= 0:
        return max_value
    else:
        # 计算当前的生长进度 (0.0 到 1.0 之间)
        growth_progress = current_age / max_age_for_growth

        # 在初始值和最大值之间进行线性插值
        current_value = min_value + (max_value - min_value) * growth_progress

        return current_value

##########################################################################################
def get_random_normal(mean, std_dev, min_val, max_val):
    """
    从正态分布中获取一个随机数，并确保它在指定的最小/最大值范围内。
    
    参数:
    mean (float): 分布的均值（中心值）。
    std_dev (float): 分布的标准差（控制分布的“胖瘦”）。
    min_val (float): 允许的最小值。
    max_val (float): 允许的最大值。

    返回:
    float: 在[min_val, max_val]范围内的随机数。
    """
    # 使用 random.gauss 生成一个原始的正态分布随机数
    value = random.gauss(mean, std_dev)
    
    # 将结果“钳制”在最小和最大值之间，确保不会越界
    clamped_value = max(min_val, min(value, max_val))
    
    return clamped_value

##########################################################################################

def calculate_peak_value(current_age, peak_age, max_age, min_value, peak_value):
    """
    计算一个先线性增长到峰值，然后线性下降的值。

    参数:
    current_age (float): 当前年龄。
    peak_age (float): 达到峰值时的年龄。
    max_age (float): 生命周期最大年龄，此时数值回归到最低值。
    min_value (float): 在0岁和max_age时的最低值。
    peak_value (float): 在peak_age时的峰值。

    返回:
    float: 根据当前年龄计算出的值。
    """
    if current_age < peak_age:
        # 阶段1: 成长期
        if peak_age <= 0:
            return peak_value
        
        # 计算生长进度 (0.0 to 1.0)
        progress = current_age / peak_age
        
        # 在最低值和峰值之间进行线性插值
        value = min_value + (peak_value - min_value) * progress
        return value
    else:
        # 阶段2: 衰老期
        decline_duration = max_age - peak_age
        if decline_duration <= 0:
            return min_value

        # 计算衰老期已经持续了多久
        age_past_peak = current_age - peak_age
        # 确保 age_past_peak 不会超过衰老期总时长
        age_past_peak = min(age_past_peak, decline_duration)

        # 计算衰老进度 (0.0 to 1.0)
        progress = age_past_peak / decline_duration
        
        # 在峰值和最低值之间进行线性插值
        value = peak_value - (peak_value - min_value) * progress
        return value
