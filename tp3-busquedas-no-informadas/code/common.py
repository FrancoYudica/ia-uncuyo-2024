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

def find_index(lst, key):
    for i, item in enumerate(lst):
        if key(item):
            return i
    return None
        
def insert_sorted(
        sorted_list: list, 
        item, 
        key=lambda a, b: a < b):
    """
    Given a sorted list, inserts the item by comparing
    with the key, which is a function that returns True
    when a is SMALLER than b.

    Uses binary search for insertion, therefore it's O(log(n)) for search.
    """

    left_index = 0
    right_index = len(sorted_list) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        item_middle = sorted_list[middle_index]

        if key(item, item_middle):
            right_index = middle_index - 1
        else:
            left_index = middle_index + 1

    # Insert the item at the correct position
    sorted_list.insert(left_index, item)
    return sorted_list


if __name__ == "__main__":
    numbers = [1, 4, 6, 7, 10]
    numbers = insert_sorted(
        numbers,
        -1,
        lambda a, b: a < b
    )
    print(numbers)