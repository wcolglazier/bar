import time

final_calculations = ['Yet to be ranked' for _ in range(10)]
start_measurement_time = [0 for _ in range(10)]
interaction_counts = [0 for _ in range(10)]

while True:
    which_bar, initial_value = map(int, input('Enter bar number (1-10) and rating (1-5), separated by a comma: ').split(','))
    current_time = time.time()
    bar_index = which_bar - 1

    if start_measurement_time[bar_index] == 0:
        start_measurement_time[bar_index] = current_time

    time_since_last_interaction = current_time - start_measurement_time[bar_index]
    time_adjustment_factor = max(0, 10 - time_since_last_interaction) / 10

    if final_calculations[bar_index] == 'Yet to be ranked':
        final_calculations[bar_index] = (initial_value + 3) / 2
    else:
        adjusted_initial_value = (initial_value * time_adjustment_factor)
        final_calculations[bar_index] = (final_calculations[bar_index] + adjusted_initial_value) / (1 + interaction_counts[bar_index] * time_adjustment_factor)

    interaction_counts[bar_index] += 1
    start_measurement_time[bar_index] = current_time

    for i, rating in enumerate(final_calculations):
        if rating != 'Yet to be ranked':
            print(f'Bar {i + 1} is {rating}/5 fun rn')
        else:
            print(f'Bar {i + 1} is Not ranked yet')
