
import time 
import pandas as pd
import numpy as np


##############INPUT city
while True:

    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    names = input("Enter names separated by commas: ")

    list_city=["chicago", "new york city", "washington"]
    city_entered = input('Choose a city between Chicago, New York city or Washington               ') 
#city_entered=city_entered.lower()

#city_valid=(city_entered not in list_city)
#print(city_valid)
    while (city_entered.lower() not in list_city):
        city_entered = input('Choose a city between Chicago, New York city or Washington               ') 
    print('Great ', names, '! You have choosen the city of ', city_entered.lower())

##############INPUT MONTH
    list_month=["all", "january", "february", "march", "april", "may", "june"]
    month_entered = input('Enter the month by choosing : all, january, february, march, april, may, june                  ')
    while (month_entered.lower() not in list_month):
        month_entered = input('Enter the month by choosing : all, january, february, march, april, may, june              ')
    print('Awesome, You want the data for the period ', month_entered.lower())

############ INPUT DAY
    list_day=["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day_entered = input('Enter the day by choosing : all, monday, tuesday, wednesday, thursday, friday, saturday, sunday                 ')
    while (day_entered.lower() not in list_day):
        day_entered = input('Enter the day by choosing : all, monday, tuesday, wednesday, thursday, friday, saturday, sunday                 ')
    print('Perfect, You want the data for the day(s) ', day_entered.lower())

    city=city_entered.lower()
    month=month_entered.lower()
    day=day_entered.lower()
    
    # loading data in a dataframe
    df = pd.read_csv(CITY_DATA[city])
# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
      #filter by month if applicable
    
# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        print(months.index(month))
        month = months.index(month) + 1

# filter by month to create the new dataframe
        df = df[df['month'] == month]

# filter by day of week if applicable
    if day != 'all':
# filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

#Displays statistics on the most frequent times of travel.

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

# display the most common month
    common_mth=df['month'].mode()[0]
    print('The most common month is:', common_mth)
#print(df)
#display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print('The most common day is :', common_day)

# display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print('The most common start hour is : ', common_hour)
    print("\nThis query took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Displays statistics on the most popular stations and trip.

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
#display most commonly used start station
    com_start_station=df['Start Station'].mode()[0]
    print('The most commonly used start station is : ', com_start_station)
# display most commonly used end station
    com_end_station=df['End Station'].mode()[0]
    print('The most commonly used end station is : ', com_end_station)

    # display most frequent combination of start station and end station trip
    df['Combo Station']="From "+ df['Start Station'] + " To " +df['End Station']
    com_combo_station=df['Combo Station'].mode()[0]
    print('The most frequent combination of start station and end station trip is : ', com_combo_station)
    print("\nThis took %s seconds." % (time.time() - start_time))

#Displays statistics on bikeshare users.
    print('\nCalculating User Statistics...\n')
    start_time = time.time()
    # Display counts of user types
    count_type=df['User Type'].value_counts()
    print('The frequency of the User Type variable is:')
    print(count_type)
    # Display counts of gender
    if city_entered.lower() != 'washington': 
        count_gender=df['Gender'].value_counts()
        print('The frequency of the Gender variable is:')
        print(count_gender)

    # Display earliest, most recent, and most common year of birth
        early_birth=df['Birth Year'].min(skipna = True)
        print('The earliest year of birth is : ', early_birth)
        latest_birth=df['Birth Year'].max(skipna = True)
        print('The latest year of birth is : ', latest_birth)
        com_birth=df['Birth Year'].mode()[0]
        print('The most common year of birth is : ', com_birth)
    
    if city_entered.lower()=='washington':
        print('Data related to Washignton does not contain information on Gender nor on year of Birth')
    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)  
    
    
    num=0
    while num<100 :
        if num==0 :
            topdisplay = input('\nWould you like to display the top 5 rows? Enter yes or no.\n')
        else:
            topdisplay = input('\nWould you like to display the 5 more rows? Enter yes or no.\n')
        if topdisplay.lower()=='yes':
            num+=5
            print(df.head(num))
        else:
            break
    print('-'*40," END ", '-'*40)    
    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
        break
