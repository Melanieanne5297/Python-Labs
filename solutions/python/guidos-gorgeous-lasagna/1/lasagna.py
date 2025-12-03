EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

"""Validate function.__doc__ exists for each function.
Check the attribute dictionary of each listed function
for the presence of a __doc__ key.

:return: unexpectedly None error when __doc__ key is missing.
"""
def bake_time_remaining(elapsed_bake_time):
    """return result"""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """return result"""
    return number_of_layers * PREPARATION_TIME 

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """return result"""
    prep_time = preparation_time_in_minutes(number_of_layers)
    return elapsed_bake_time + prep_time

