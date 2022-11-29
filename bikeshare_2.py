import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! So happy to see you. Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_cities = ['washington','chicago','new york city']
    city = input("Choose one of the three cities, chicago, new york city, or washington: ").lower()
    while city not in valid_cities:
            print("you entered an invalid option!!")
            city = input("Choose one of the three cities, chicago, new york city, or washington: ").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    valid_month = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input("Select a month from January to June, or type all to see the whole date set: ").lower()
    while month not in valid_month:
            print("That\'s not a valid entry. Please try again")
            month = input("Select a month from January to June, or type all to see the whole date set: ").lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Select one day from Monday to Sunday, or type all to see the whole week: ").lower()
            break
        except ValueError:
            print("That\'s not a valid entry. Please try again")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)
        df = df[df['month'] == month]

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most commonly month is: ", popular_month)
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day of week is: ", popular_day)
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The most common start hour is: ", popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_sta = df['Start Station'].mode()[0]
    print("The most commonly used end station is: ", popular_start_sta)
    # TO DO: display most commonly used end station
    popular_end_sta = df['End Station'].mode()[0]
    print("The most commonly used end station is: ", popular_end_sta)
    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " - " + df['End Station']
    popular_trip = df['Trip'].mode()[0]
    print("The most commonly frequent combination of start station and end station trip is: ", popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_traveltime = df["Trip Duration"].sum()
    print("the total trip duration is {} seconds.".format(total_traveltime))
    # TO DO: display mean travel time
    mean_traveltime = df["Trip Duration"].mean()
    print("the average trip duration is {} seconds.".format(mean_traveltime))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        user_gender = df['Gender'].value_counts()
    else:
        print('The gender column is not found.')
# TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        user_gender = df['Birth Year'].value_counts()
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print("The earliest year of birth is: ", earliest_year)
        print("The most recent year of birth is: ", most_recent_year )
        print("The most common year of birth is: ", most_common_year )
    else:
        print('The birth year column is not found.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_3_rows(df):
    view_data = input('\nWould you like to view 3 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data != 'no':
        print(df.iloc[start_loc:(start_loc+3)])
        start_loc += 3
        view_data = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        view_5_rows(df)

        restart = input('\nWould you like to restart or say goodbye? Enter restart or goodbye.\n')
        if restart.lower() != 'restart':
            break


if __name__ == "__main__":
	main()
