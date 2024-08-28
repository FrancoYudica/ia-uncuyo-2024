def apply_action_to_position(
        pos: tuple, 
        action: int):
    """
    Given position and action index returns 
    the position after the action is applied
    """

    # Left
    if action == 0:
        return pos[0], pos[1] - 1

    # Down
    if action == 1:
        return pos[0] + 1, pos[1]

    # Right
    if action == 2:
        return pos[0], pos[1] + 1

    # Up
    return pos[0] - 1, pos[1]

def build_path_from_actions(
        start_pos,
        actions: list):
    """
    Given the start position, applies a set of actions and
    calculates the resulting path, containing start and end
    """
    path = [start_pos]
    for action in actions:
        path.append(apply_action_to_position(path[len(path) - 1], action))

    return path