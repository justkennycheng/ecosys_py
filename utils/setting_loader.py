"""Module providing a function printing python version."""
# utils/setting_loader.py
import os
import yaml

# 1. 获取当前文件(setting_loader.py)所在的目录的绝对路径
_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# 2. 从当前目录向上一级，得到项目的根目录
_PROJECT_ROOT = os.path.dirname(_CURRENT_DIR)
# 3. 拼接出配置文件的绝对路径
_DEFAULT_PATH = os.path.join(_PROJECT_ROOT, 'config', 'settings.yaml')

def load_settings(path=_DEFAULT_PATH): #使用计算出的绝对路径作为默认值
    """introduction"""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
