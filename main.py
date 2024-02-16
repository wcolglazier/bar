count1 = 1
count2 = 1
count3 = 1

total_rating1 = 3
total_rating2 = 3
total_rating3 = 3

while True:
    bar1 = total_rating1 / count1
    bar2 = total_rating2 / count2
    bar3 = total_rating3 / count3

    print(f'Bar 1 is {bar1}/5 fun rn')
    print(f'Bar 2 is {bar2}/5 fun rn')
    print(f'Bar 3 is {bar3}/5 fun rn')

    Which_bar = int(input('Which bar do you wanna rate from 1-3: '))
    if Which_bar == 1:
        bar_rate_1 = int(input('Enter rating for bar 1 from 1 to 5: '))
        total_rating1 += bar_rate_1
        count1 += 1
    elif Which_bar == 2:
        bar_rate_2 = int(input('Enter rating for bar 2 from 1 to 5: '))
        total_rating2 += bar_rate_2
        count2 += 1
    elif Which_bar == 3:
        bar_rate_3 = int(input('Enter rating for bar 3 from 1 to 5: '))
        total_rating3 += bar_rate_3
        count3 += 1
