def stock_prices_evaluator(file, mode, list_return = 1):
"""This Function receives a CSV file, a mode (r for reading, w for writing) and an optional value for which list it should return.
Being: 1 = Best six months, 2 = Worst six months, 3 = Best six years, 4 = Worst six years, any orther value return all the months. 
"""
    count = 0 #Count of interactions
    value_month = 0 #Sum of the month's value 
    value_year = 0 #Sum of the years's value

    float_month = 0
    float_year = 0

    current_month = "" #Stores the current month in a String
    current_year = "" #Stores the current year in a String
    
    #The lists to be filled in the interations 
    list_months = []
    list_avg_months = []
    list_years = []
    list_avg_years = []

    file = open(file, mode)
    
    #Loop through the file line by line
    for line in file.read().split():
        
        #Creates a temporary array with the line values
        arr_temp = [string for string in line.split(",")]
        
        #Everything is wraped into a try/except case the file is corrupted or is invalid.
        try:
            float_day = float(arr_temp[5]) * float(arr_temp[6])
            value_day = float(arr_temp[6])

            #When the year change Add to the list the Average
            #Also sets the values to 0 to begin a new year
            if arr_temp[0][0:4] != current_year:
                current_year = arr_temp[0][0:4]
                list_years.append(current_year)
                list_avg_years.append(0)
                value_year = 0
                float_year = 0

            #When the month change Add to the list the Average
            #Also sets the values to 0 to begin a new month
            if arr_temp[0][5:7] != current_month:
                current_month = arr_temp[0][5:7]
                list_months.append(current_year + "/" + current_month)
                list_avg_months.append(0)
                value_month = 0
                float_month = 0            
            
            #Every interaction the value of the month and year is calculated
            value_month += value_day
            float_month += float_day
            avg_month = float_month / value_month
            list_avg_months[-1] = avg_month #Stores the current average in the last member

            float_year += float_day
            value_year += value_day
            avg_year = float_year / value_year
            list_avg_years[-1] = avg_year #Stores the current average in the last member
            
            #Counter not used but kept as a good practice in large files
            count += 1
        
        #There's no need to give a special treatment for the exception, so the loop will continue
        except:
            continue

    #If/Else to return the list
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
