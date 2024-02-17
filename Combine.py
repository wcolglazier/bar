import time


final_calculation1 = 'Yet to be ranked'
final_calculation2 = 'Yet to be ranked'


start_measurement_time = 0
interaction_count = 1

while True:

    Which_bar, initial_value = map(int, input('Enter bar number (1-3) and rating (1-5), separated by a comma: ').split(','))
    current_time = time.time()

    if Which_bar == 1:

        if start_measurement_time == 0:
            start_measurement_time = current_time

        time_since_last_interaction = current_time - start_measurement_time

        part1 = (initial_value + 3) / 2
        print(f'Bar 1 is {part1}/5 fun rn')
        print('Bar 2 is Not ranked yet')

        start_measurement_time = current_time
        Which_bar, subsequent_value = map(int, input('Enter bar number (1-3) and rating (1-5), separated by a comma: ').split(','))
        if Which_bar == 1:
            current_time = time.time()

            time_since_last_interaction = current_time - start_measurement_time


            start_measurement_time = current_time

            time_adjustment_factor = max(0, 10 - time_since_last_interaction) / 10
            adjusted_initial_value = (initial_value * max(0, 10 - time_since_last_interaction)) / 10

            final_calculation1 = (subsequent_value + adjusted_initial_value) / (
                        1 + interaction_count * time_adjustment_factor)
            if final_calculation1 != 'Yet to be ranked':
                print(f'Bar 1 is {final_calculation1}/5 fun rn')
            else:
                print('Bar 2 is Not ranked yet')
            if final_calculation2 != 'Yet to be ranked':
                print(f'Bar 2 is {final_calculation2}/5 fun rn')
            else:
                print('Bar 2 is Not ranked yet')
        if Which_bar == 2:
            part1 = (initial_value + 3) / 2
            print(f'Bar 1 is {part1}/5 fun rn')
            sub1 = (subsequent_value + 3) / 2
            print(f'Bar 2 is {sub1}/5 fun rn')


    elif Which_bar == 2:

        if start_measurement_time == 0:
            start_measurement_time = current_time

        time_since_last_interaction = current_time - start_measurement_time

        print('Bar 1 is Not ranked yet')
        part1 = (initial_value + 3) / 2
        print(f'Bar 2 is {part1}/5 fun rn')

        start_measurement_time = current_time
        Which_bar, subsequent_value = map(int, input('Enter bar number (1-3) and rating (1-5), separated by a comma: ').split(','))
        if Which_bar == 1:
            part1 = (initial_value + 3) / 2
            print(f'Bar 1 is {part1}/5 fun rn')
            sub1 = (subsequent_value + 3) / 2
            print(f'Bar 2 is {sub1}/5 fun rn')
        if Which_bar == 2:
            current_time = time.time()

            time_since_last_interaction = current_time - start_measurement_time

            start_measurement_time = current_time

            time_adjustment_factor = max(0, 10 - time_since_last_interaction) / 10
            adjusted_initial_value = (initial_value * max(0, 10 - time_since_last_interaction)) / 10
            final_calculation2 = (subsequent_value + adjusted_initial_value) / (
                        1 + interaction_count * time_adjustment_factor)
            if final_calculation1 != 'Yet to be ranked':
                print(f'Bar 1 is {final_calculation1}/5 fun rn')
            else:
                print('Bar 2 is Not ranked yet')
            if final_calculation2 != 'Yet to be ranked':
                print(f'Bar 2 is {final_calculation2}/5 fun rn')
            else:
                print('Bar 2 is Not ranked yet')