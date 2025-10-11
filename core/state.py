"""Module providing a function printing python version."""
# core/state.py
from enum import Enum

class OrganismState(Enum):
    """introduction"""
    Idle = 0
    Foraging = 1
    Fleeing = 2
    Resting = 3
    Reproducing = 4
    Dead = 5
