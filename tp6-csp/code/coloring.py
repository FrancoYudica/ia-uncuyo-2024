def get_neighbors(territories, territory_name) -> list:
    return territories[territory_name]


def revise(
        domains, 
        xi, 
        xj) -> bool:
    """
    Revises the domain of Xi by removing the value 
    of Xj if the Xj value is already set
    """

    xi_domain = domains[xi]
    xj_domain = domains[xj]

    # xj_domain should have one element
    # Revision works when xj has set it's final value, 
    # therefore the length of the domain should be 1
    if len(xj_domain) != 1:
        return False

    # Removes xj variable value from the domain if xi
    xj_value = xj_domain[0]

    if xj_value in xi_domain:
        xi_domain.remove(xj_value)
        return True
    
    return False


def ac3_painting(territories, domains) -> bool:

    # Initializes queue with all the neighbors of all the cells. This will
    # create an array of N*N*(3*(N-1)) = 9*9*(3*(9-1)) = 1944
    queue = []
    for territory_name in territories.keys():
        for neighbor_name in get_neighbors(territories, territory_name):
            queue.append((territory_name, neighbor_name))

    while queue:
        xi, xj = queue.pop(0)

        # If the domain of Xj is reduced
        if revise(domains, xi, xj):

            # If the domain is empty, there isn't solution
            if len(domains[xi]) == 0:
                return False

            # Adds all the neighbors of xi to the queue
            for neighbor in get_neighbors(territories, xi):

                # Except for xj
                if neighbor != xj:
                    queue.append((neighbor, xi))
    return True


def test_wa_red_v_blue():

    # Defines map as a graph with a dictionary
    territories = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["Q", "SA", "V"],
        "V": ["SA", "NSW"],
        "T": []
    }

    domains = {territory_name: [i for i in range(3)] for territory_name in territories.keys()}
    domains["WA"] = [0]
    domains["V"] = [2]

    print(domains)

    if ac3_painting(territories, domains):
        print("Solution possible!")
        print(domains)
    else:
        print("No solution possible...")
        print(domains)


if __name__ == "__main__":
    test_wa_red_v_blue()
