# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ayad Masud
# Section:      520
# Assignment:   11.13 Lab
# Date:         11/2/23
# comment

with open('WeatherDataCLL.csv', 'r') as file:
    next(file)

    dict = {'January': '1',
            'February': '2',
            'March': '3',
            'April': '4',
            'May': '5',
            'June': '6',
            'July': '7',
            'August': '8',
            'September': '9',
            'October': '10',
            'November': '11',
            'December': '12'}
    
    
    # part 1: finding max and min temp
    max_temp = []
    min_temp = []
    data_date = {}
    dates = []
    for line in file:
        # getting all max and min temp values
        s = line.split(',')
        # check if data point actually exists
        if s[-1] == '':
            continue
        if s[-2] == '':
            continue
        stripped = s[-1].strip()
        s[-1] = stripped
        max_temp.append(s[-2])
        min_temp.append(s[-1])
        dates.append(s[0])
        data_date[s[0]] = s  # key: date   value: data points
    # converting max and min lists to int
    max_t = max([eval(i) for i in max_temp])
    min_t = min([eval(i) for i in min_temp])
    print(f"10-year maximum temperature: {max_t} F")
    print(f"10-year minimum temperature: {min_t} F")
    # part 2: finding data about given month
    print()
    month = input('Please enter a month: ') # july
    year = input('Please enter a year: ') # 2013
    correct_date = []
    for date in dates:
        s = date.split('/')
        m = s[0]
        y = s[-1]
        if m == dict[month] and y == year:
            correct_date.append(s)
    
    correct_data = []
    for i in correct_date:
        joined_string = '/'.join(i)
        if joined_string in data_date:
            correct_data.append(data_date[joined_string])  # now has correct data for given month
    
    num_days = {'January': 31,
            'February': 28,
            'March': 31,
            'April': 30,
            'May': 31,
            'June': 30,
            'July': 31,
            'August': 31,
            'September': 30,
            'October': 31,
            'November': 30,
            'December': 31}
    
    # mean average daily temp (3rd from the right)
    mean_average_temp = []
    for point in correct_data:
        if point[-3] == '':
            continue
        else:
            mean_average_temp.append(point[-3])

    # mean relative humidity
    mean_relative_humidty = []
    for point in correct_data:
        if point[-4] == '':
            continue
        else:
            mean_relative_humidty.append(point[-4])

    # mean daily wind speed
    mean_daily_windspeed = []
    for point in correct_data:
        if point[1] == '':
            continue
        else:
            mean_daily_windspeed.append(point[1])

    # percentage of days with precipitation
    precipitation = []
    for point in correct_data:
        if point[2] == '':
            continue
        elif float(point[2]) > 0:
            precipitation.append(point[2])

    if len(mean_average_temp) == 0:
        temp = 0
    else:
        a = [eval(i) for i in mean_average_temp]
        temp = (sum(a) / len(mean_average_temp))

    if len(mean_relative_humidty) == 0:
        humidity = 0
    else:
        b = [eval(i) for i in mean_relative_humidty]
        humidity = (sum(b) / len(mean_relative_humidty))

    if len(mean_daily_windspeed) == 0:
        wind = 0
    else:
        c = [eval(i) for i in mean_daily_windspeed] 
        wind = (sum(c) / len(mean_daily_windspeed))

    if len(precipitation) == 0:
        percent = 0
    else:
        percent = (len(precipitation) / num_days[month]) * 100

    # printing all output
    print()
    print(f"For {month} {year}:")
    print(f"Mean average daily temperature: {temp:.1f} F")
    print(f"Mean relative humidity: {humidity:.1f}%")
    print(f"Mean daily wind speed: {wind:.2f} mph")
    print(f"Percentage of days with precipitation: {percent:.1f}%")

#print(data_date)
        


    
