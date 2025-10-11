"""这里放置了一些通用函数"""
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
