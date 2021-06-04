import time
import pandas as pd
import numpy as np


def get_filters(city,month,day):


    """
    Asks user to input month, city and day to analyze.

    def get_filters()
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = city.lower()
    month = month.lower()
    day = day.lower()



    city = city
    cities = ['chicago','new york city','washington']
    cit_in = 0
    while cit_in == 0:
        if city in cities:
            city_in = 1
            break
        else:
            city = input("enter a valid city name to continue :")
            city = city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)

    months = ['january','february','march','april','may','june','july','augest','september','octomber','november','desember','all']
    mo = 'no'
    while mo == 'no':
        if month in months:
            mo = 'yes'
            month = months.index(month) + 1
            break
        else:
            month = input("enter a valid month to continue :")
            month = month.lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['monday','tuesday','wednesday','thursday','fryday','saturday','sunday','all']

    c = 0
    while c == 0:
        if day in days:
            c = 1
            break

        else:
            day = input("enter a valid day to continue :")
            day = day.lower()

    print('-'*40)
    return city, month, day





def load_data(city, month, day):

    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    if month != 13:
        df = df[df['month'] == month]
    df['day'] = df['Start Time'].dt.weekday_name
    if day != 'all':
        df = df[df['day'] == day]


    return df


def time_stats(df):


    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mcm = df['month'].mode()
    print("the most common month is: ",mcm)

    # TO DO: display themmon day of week
    mcd = df['day'].mode()
    print("the most common weekday is: ",mcd)

    # TO DO: display the most common start hour
    df['start hour'] = df['Start Time'].dt.hour
    mcs = df['start hour'].mode()
    print("the most common start hour is: ",mcs)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    mcss = df['Start Station'].mode()
    print("the most commonly used start station is :",mcss)



    # TO DO: display most commonly used end station
    mces = df['End Station'].mode()
    print("the most commonly used end station is  :",mces)

    # TO DO: display most frequent combination of start station and end station trip
    df['se'] = df['Start Station']+ df['End Station']
    mfc = df['se'].mode()
    print("the most frequent combination of start station and end station trip is:  ",mfc)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel time is: ",total_travel_time)

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print("\nmean travel time is: ",mean )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    useer_types = df['User Type'].value_counts()
    print('total counts of user types: ',useer_types)
    # TO DO: Display counts of gender
    if city != 'washington':
        useer_gender = df['Gender'].value_counts()
        print('total counts of gender: ',useer_gender)
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].max()
        print('earliest birth year:',earliest)
        most_reasent = df['Birth Year'].min()
        print('most resent birth year:',most_reasent)
        avg = df['Birth Year'].mean()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)

def viw_data(city):
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
    df = pd.read_csv(CITY_DATA[city])

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:(start_loc+5)])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
def main():
    while True:
        print("Hellow let's explore some us bikeshare data")


        city, month, day = get_filters(city = input("please enter a city:"),month = input("please enter a month:"),day = input("please enter a day:"))
        print('reading data relavent to :',city,'     in the month :',month,'     on the week day :',day)
        df = load_data(city, month, day)
        restart = input('\nWould you like to get statistics on the most frequent times of travel and continue? Enter yes or no.\n')
        if restart.lower() == 'yes':
            time_stats(df)
            restart = input('\nWould you like to get statistics on the most frequent stations and continue ? Enter yes or no.\n')
            if restart.lower() == 'yes':
                station_stats(df)
                restart = input('\nWould you like to get statistics on trip durations? Enter yes or no.\n')
                if restart.lower() == 'yes':
                    trip_duration_stats(df)
                    restart = input('\nWould you like to get statistics on user? Enter yes or no.\n')
                    if restart.lower() == 'yes':
                        user_stats(df,city)
                    else:
                        restart = input('\nWould you like to get statistics on user? Enter yes or no.\n')
                        if restart.lower() == 'yes':
                            user_stats(df,city)

                else:
                    restart = input('\nWould you like to get statistics on trip durations? Enter yes or no.\n')
                    if restart.lower() == 'yes':
                       trip_duration_stats(df)
                    else:
                        restart = input('\nWould you like to get statistics on user? Enter yes or no.\n')
                        if restart.lower() == 'yes':
                            user_stats(df,city)

            else:
                restart = input('\nWould you like to get statistics on the most frequent stations and continue ? Enter yes or no.\n')
                if restart.lower() == 'yes':
                    station_stats(df)
                    restart = input('\nWould you like to get statistics on trip durations? Enter yes or no.\n')
                    if restart.lower() == 'yes':
                       trip_duration_stats(df)
                       restart = input('\nWould you like to get statistics on user? Enter yes or no.\n')
                       if restart.lower() == 'yes':
                        user_stats(df,city)

                    else:
                        restart = input('\nWould you like to get statistics on user? Enter yes or no.\n')
                        if restart.lower() == 'yes':
                            user_stats(df,city)

                else:
                    restart = input('\nWould you like to get statistics on trip durations? Enter yes or no.\n')
                    if restart.lower() == 'yes':
                        trip_duration_stats(df)
                        restart = input('\nWould you like to get statistics on user? Enter yes or no.\n')
                        if restart.lower() == 'yes':
                            user_stats(df,city)




                    else:
                        restart = input('\nWould you like to get statistics on user? Enter yes or no.\n')
                        if restart.lower() == 'yes':
                            user_stats(df,city)
        viw_data(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
