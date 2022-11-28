# Standard Library
from enum import Enum


"""
PENDING Pendiente
DELIVERED Entregado
"""

class StatusConstants(Enum):
    PENDING = 0
    DELIVERED = 1


class IsActive(Enum):
    ACTIVE = 1
    INACTIVE = 0
