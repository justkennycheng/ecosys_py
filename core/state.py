"""Module providing a function printing python version."""
# core/state.py
from enum import Enum

class RabbitState(Enum):
    """introduction"""
    Idle = 0
    Foraging = 1
    Fleeing = 2
    Resting = 3
    Reproducing = 4
    Dead = 5

class WolfState(Enum):
    """introduction"""
    Idle = 0
    Foraging = 1
    Fleeing = 2
    Resting = 3
    Reproducing = 4
    Dead = 5
