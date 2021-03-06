# BSFKL
birth = {6, 28, 34, 39, 40, 45, 65, 67, 80}
survival = {30, 35, 46, 50, 67, 68, 70, 80}
forcing = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 42, 25, 30, 45, 46, 50}
killing = {7, 10, 14, 20, 32, 35, 50, 66, 67}
living = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
          33, 34, 35, 40, 45, 46, 60, 70}

# Information about the Rule (Must be filled)
n_states = 3  # Number of States
alternating_period = 1  # For alternating rules / neighbourhoods
colour_palette = None  # Colours of the different states
rule_name = "BSFKLWeighted_Rule_6"  # Rule Name


# Neighbourhood of the Rule (Relative Distance from Central Cell)
def get_neighbourhood(generation):  # Note (y, x) not (x, y)
    return [(2, -2), (2, -1), (2, 0), (2, 1), (2, 2),
            (1, -2), (1, -1), (1, 0), (1, 1), (1, 2),
            (0, -2), (0, -1), (0, 0), (0, 1), (0, 2),
            (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2),
            (-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2)]


# Transition Function of Rule, Last Element of Neighbours is the Central Cell
def transition_func(neighbours, generation):
    weights = [1, 2, 3, 2, 1,
               2, 4, 6, 4, 2,
               3, 6, 9, 6, 3,
               2, 4, 6, 4, 2,
               1, 2, 3, 2, 1]

    n_living, n_destructive = 0, 0
    for i in range(len(neighbours) - 1):
        if neighbours[i] == 1:
            n_living += weights[i]
        elif neighbours[i] == 2:
            n_destructive += weights[i]

    if neighbours[-1] == 1:
        if n_destructive in killing:
            return 0
        elif n_living in survival:
            return 1
        return 2

    elif neighbours[-1] == 2:
        if n_living in living:
            return 0
        return 2

    else:
        if n_destructive in forcing and n_living in birth:
            return 1
        return 0


# Does the next state of the cell depend on its neighbours?
# If yes, return next state
# If no, return -1
def depend_on_neighbours(state, generation):
    return -1
