def health_caculator(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

winstons_data = [22, 5, 0]

health_caculator(winstons_data[0], winstons_data[1], winstons_data[2])

health_caculator(*winstons_data)