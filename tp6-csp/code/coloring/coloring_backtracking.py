from coloring_ac3 import ac3_coloring

def backtracking_search(
        territories,
        initial_domains) -> dict:
    """
    Implementation of backtracking algorithm for CSP. It' not the most basic backtracking,
    since it requires the `initial_domains` argument, allowing previous domain optimization
    by using algorithms such as ac3
    """
    
    assignment = dict()
    if _backtrack(assignment, territories, initial_domains):
        return assignment

    return {}

def _backtrack(
        assignment: dict, 
        territories: dict,
        initial_domains: dict) -> bool:

    ## Helper functions ----------------------------------------------------
    def select_unassigned_var():
        for var in territories:
            if var not in assignment:
                return var
            
    def order_domain_values(var):
        # Iterator that removes the values from the domain once it's yield
        for _ in range(len(initial_domains[var])):
            yield initial_domains[var].pop(0)

    def is_consistent_assignment(var, value) -> bool:
        # Checks that all the neighbors have different assignments, if any
        for neighbor in territories[var]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True
    
    ## Actual code -----------------------------------------------------------

    # When all variables got assigned
    if len(assignment) == len(territories):
        return True
    
    var = select_unassigned_var()

    # Iterates through all the possible values
    for value in order_domain_values(var):

        # Skips assignments that break the restrictions
        if not is_consistent_assignment(var, value):
            continue
        
        assignment[var] = value

        # Tries to find a solution with the assignment
        if _backtrack(assignment, territories, initial_domains):
            return True
    
    return False
    

if __name__ == "__main__":

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

    # Applies ac3 to get initial reduced domain
    initial_domains = {territory_name: [i for i in range(3)] for territory_name in territories.keys()}
    initial_domains["WA"] = [0]
    initial_domains["V"] = [0]
    if not ac3_coloring(territories, initial_domains):
        print(f"No solution possible for reduced domains: {initial_domains}")
        exit(0)

    print(f"Reduced domains to: {initial_domains}")
    print("Running backtracking...")
    final_assignment = backtracking_search(territories, initial_domains)

    if final_assignment:
        print("Solution found!")
        print(final_assignment)
    else:
        print("There aren't solutions for this configuration...")