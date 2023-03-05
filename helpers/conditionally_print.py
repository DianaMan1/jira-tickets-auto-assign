from typing import Union
from helpers.check_for_debug_level import isDebugLevelOne


def conditionally_print(text: Union[str, None]):
    if(isDebugLevelOne()):
        print(text)
