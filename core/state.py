# core/state.py
from enum import Enum

class RabbitState(Enum):
    Idle = 0
    Foraging = 1
    Fleeing = 2
    Resting = 3
    Reproducing = 4
    Dead = 5

class WolfState(Enum):
    Idle = 0
    Foraging = 1
    Fleeing = 2
    Resting = 3
    Reproducing = 4
    Dead = 5

