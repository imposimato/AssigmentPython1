count = 0
value_month = 0
value_year = 0

float_month = 0
float_year = 0

avg_month = 0
avg_year = 0

list_months = []
list_avg_months = []
list_years = []
list_avg_years = []

file = open("googleprices.csv", "r")

for line in file.read().split():

    arr_temp = [string for string in line.split(",")]

    try:
        float_day = float(arr_temp[5]) * float(arr_temp[6])
        value_day = float(arr_temp[6])

        #Set the values for the first interaction
        if count < 1:
            current_month = arr_temp[0][5:7]
            current_year = arr_temp[0][0:4]

            value_month += value_day
            float_month += float_day
            avg_month = float_month / value_month
            list_avg_months.append(avg_month)
            list_months.append(current_year + "/" + current_month)

            float_year += float_day
            value_year += value_day
            avg_year = float_year / value_year
            list_avg_years.append(avg_year)
            list_years.append(current_year)

        #When the month change Add to the list the Average
        if arr_temp[0][5:7] != current_month:
            list_months.append(current_year + "/" + current_month)
            list_avg_months.append(0)
            value_month = 0
            float_month = 0

        # When the year change Add to the list the Average
        if arr_temp[0][0:4] != current_year:
            list_years.append(current_year)
            list_avg_years.append(0)
            value_year = 0
            float_year = 0

        if count >= 1:
            value_month += value_day
            float_month += float_day
            avg_month = float_month / value_month
            list_avg_months[-1] = avg_month

            float_year += float_day
            value_year += value_day
            avg_year = float_year / value_year
            list_avg_years[-1] = avg_year

        current_month = arr_temp[0][5:7]
        current_year = arr_temp[0][0:4]
        count += 1

    except:
        continue


best_six_months = sorted(zip(list_avg_months, list_months), reverse=True)[:6]
print(best_six_months)

best_six_months = sorted(zip(list_avg_months, list_months))[:6]
print(best_six_months)

best_six_months = sorted(zip(list_avg_years, list_years), reverse=True)[:6]
print(best_six_months)

best_six_months = sorted(zip(list_avg_years, list_years))[:6]
print(best_six_months)