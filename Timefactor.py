import time

start_measurement_time = 0
interaction_count = 1

while True:
    initial_value = int(input('Enter initial value: '))
    current_time = time.time()

    if start_measurement_time == 0:
        start_measurement_time = current_time

    time_since_last_interaction = current_time - start_measurement_time
    print("Time since last input:", time_since_last_interaction, "seconds")


    start_measurement_time = current_time
    subsequent_value = int(input('Enter subsequent value: '))
    current_time = time.time()

    time_since_last_interaction = current_time - start_measurement_time
    print("Time since last input:", time_since_last_interaction, "seconds")

    start_measurement_time = current_time

    time_adjustment_factor = max(0, 10 - time_since_last_interaction) / 10
    adjusted_initial_value = (initial_value * max(0, 10 - time_since_last_interaction)) / 10
    print("Time adjustment factor:", time_adjustment_factor)
    print("Adjusted initial value:", adjusted_initial_value)
    final_calculation = (subsequent_value + adjusted_initial_value) / (1 + interaction_count * time_adjustment_factor)
    print("Final calculated value:", final_calculation)
