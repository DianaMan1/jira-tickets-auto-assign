debug_level = 0

with open('.config/.debug/debug_level') as debug_level_file:
    debug_level_value = debug_level_file.read()
    if(debug_level_value.isdigit()):
        debug_level = int(debug_level_value)
    debug_level_file.close

def isDebugLevelOne():
    return debug_level >= 1

def isDebugLevelTwo():
    return debug_level >= 2
