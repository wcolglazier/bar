count1 = 1
count2 = 1
count3 = 1

bar1 = 3
bar2 = 3
bar3 = 3

while True:
    print(f'Bar 1 is {bar1}/5 fun rn')
    print(f'Bar 2 is {bar2}/5 fun rn')
    print(f'Bar 3 is {bar3}/5 fun rn')
    Which_bar = int(input('Which bar do you wanna rate from 1-3:'))
    if Which_bar == 1:
        bar_rate_1 = int(input('Enter rating for bar 1 from 1 to 5:'))
        count1 += 1
        bar1 = (3 + bar_rate_1) / count1
    if Which_bar == 2:
        bar_rate_2 = int(input('Enter rating for bar 1 from 1 to 5:'))
        count2 += 1
        bar2 = (3 + bar_rate_2) / count2
    if Which_bar == 3:
        bar_rate_3 = int(input('Enter rating for bar 1 from 1 to 5:'))
        count3 += 1
        bar3 = (3 + bar_rate_3) / count3





