from chess_board_state import ChessBoardState
from local_search_algo.utils import random_successor_chess_board
from local_search_algo.local_search_result import LocalSearchResult
import random
import time


def get_best_individual(population):
    return min(population, key=lambda individual: fitness(individual))


def get_mating_pool(population):
    """Returns mating individuals by their rank"""
    ranked_population = sorted(
        population, 
        key=lambda board: board.cached_threats)

    pool_size = len(population)
    probabilities = [1/(i+1) for i in range(pool_size)]
    mating_pool = random.choices(
        ranked_population, 
        weights=probabilities, 
        k=pool_size)
    
    return mating_pool


def fitness(individual) -> float:
    return individual.cached_threats


def reproduce(individual_x, individual_y):
    """Crossover operation"""
    n = individual_x.size

    # Crossover index
    i = random.randrange(1, n)
    child_columns = individual_x.columns[:i] + individual_y.columns[i:] 
    return ChessBoardState(size=n, columns=child_columns)


def mutate(individual):
    """Moves a queen along it's column"""
    n = individual.size
    mutation_column_index = random.randrange(0, n)
    current_row = individual.columns[mutation_column_index]

    # Ensures that a new row value is selected
    new_row = None
    while new_row is None or new_row == current_row:
        new_row = random.randrange(0, n)

    individual.columns[mutation_column_index] = new_row
    individual.recalculate_threats()


def get_next_generation(parents, children, elite_percentage=0.1):
    """Keeps the best X% of parents and adds children"""
    elite_size = int(elite_percentage * len(parents))  # Keep top 10% of parents as elite
    random_size = len(children) - elite_size  # Fill the rest with children

    sorted_parents = sorted(parents, key=lambda parent: fitness(parent))
    new_population = sorted_parents[:elite_size]  # Keep the best
    
    # Randomly select from the rest of the children to maintain diversity
    new_population += random.sample(children, random_size)
    
    return new_population



def genetic(
        initial_board: ChessBoardState,
        maximum_states: int = 200,
        population_size: int = 200,
        children_per_generation: int = 200,
        initial_mutation_rate: float = 0.40) -> LocalSearchResult:

    result = LocalSearchResult()
    result.board = initial_board
    t0 = time.time()
    population_size = 30 * initial_board.size
    children_per_generation = population_size - 10
    # Creates random population
    population = []
    for _ in range(population_size):
        population.append(ChessBoardState(initial_board.size))

    best_individual = None

    for generation in range(maximum_states):

        # Checks if there is a solution individual --------------------------------
        best_individual = get_best_individual(population)
        result.h_values.append(fitness(best_individual))
        if fitness(best_individual) == 0:
            break
        
        # Creates all the new children --------------------------------------------
        mutation_rate = initial_mutation_rate * (1.0 - generation / maximum_states)
        mating_pool = get_mating_pool(population)
        children = []
        for _ in range(children_per_generation):

            # Selects parents
            parent1 = random.choice(mating_pool)
            parent2 = random.choice(mating_pool)

            child = reproduce(parent1, parent2)
            # Mutates
            if random.random() < mutation_rate:
                mutate(child)

            children.append(child)

        # Updates the population with children
        population = get_next_generation(population, children)

    result.traversed_states = generation + 1
    result.time_taken = time.time() - t0
    result.board = best_individual
    return result