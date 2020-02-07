from enum import Enum


class WindowStage(Enum):
    EDIT_OBSTACLES = 0
    EDIT_START = 1
    EDIT_DESTINATION = 2
    FINDING_PATH = 3
