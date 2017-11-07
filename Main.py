def stock_prices_evaluator(file, mode, list_return = 1):

    count = 0
    value_month = 0
    value_year = 0

    float_month = 0
    float_year = 0

    current_month = ""
    current_year = ""

    list_months = []
    list_avg_months = []
    list_years = []
    list_avg_years = []

    file = open(file, mode)

    for line in file.read().split():

        arr_temp = [string for string in line.split(",")]

        try:
            float_day = float(arr_temp[5]) * float(arr_temp[6])
            value_day = float(arr_temp[6])

            # When the year change Add to the list the Average
            if arr_temp[0][0:4] != current_year:
                current_year = arr_temp[0][0:4]
                list_years.append(current_year)
                list_avg_years.append(0)
                value_year = 0
                float_year = 0

            #When the month change Add to the list the Average
            if arr_temp[0][5:7] != current_month:
                current_month = arr_temp[0][5:7]
                list_months.append(current_year + "/" + current_month)
                list_avg_months.append(0)
                value_month = 0
                float_month = 0


            value_month += value_day
            float_month += float_day
            avg_month = float_month / value_month
            list_avg_months[-1] = avg_month

            float_year += float_day
            value_year += value_day
            avg_year = float_year / value_year
            list_avg_years[-1] = avg_year

            count += 1

        except:
            continue

    if list_return == 1:
        best_six_months = sorted(zip(list_avg_months, list_months), reverse=True)[:6]
        print(best_six_months)

    elif list_return == 2:
        worst_six_months = sorted(zip(list_avg_months, list_months))[:6]
        print(worst_six_months)

    elif list_return == 3:
        best_six_years = sorted(zip(list_avg_years, list_years), reverse=True)[:6]
        print(best_six_years)

    elif list_return == 4:
        worst_six_years = sorted(zip(list_avg_years, list_years))[:6]
        print(worst_six_years)

    else:
        print(list(zip(list_avg_months, list_months)))

stock_prices_evaluator("googleprices.csv", "r")