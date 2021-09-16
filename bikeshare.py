import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['sundary', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
cities = ['chicago', 'new york city', 'washington']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
  
    
    while True:
        city = input('Would you like see data for Chicago, New York, or Washington? ').lower()
        if city in cities:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = input('Enter month to filter by month ' %months)
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input('Enter day to filter by day ' %days)
                   
    
    
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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month =  months.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]

    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
       # display the most common month
    
    print("The most common month is :", df['month'].value_counts())

    # display the most common day of week
    
    print("The most day of the week is :", df['day_of_week'].value_counts())

    # display the most common start hour

    
    print("The most common start hour is :", df['hour'].value_counts())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

    


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
 

    # TO DO: display most commonly used start station
    
    print('The most commonly user stat station is ', df['Start Station'].value_counts())  

    # TO DO: display most commonly used end station
    
    print('The most commonly end station is ', df['End Station'].value_counts()) 

    # TO DO: display most frequent combination of start station and end station trip
    
    print('The most frequent combination of start station and end station is', df[['Start Station', 'End Station']].mode())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    print('The total time travel is ', df['Trip Duration'].sum())


    # TO DO: display mean travel time
    
    print('The total mean of time travel is ', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    print('The count of user types is ', df['User Type'].count())
    
     # TO DO: Display earliest, most recent, and most common year of birth
    
    print('The earliest of birth year is ', df['Birth Year'].min())
    print('The most recent birth year is ', df['Birth Year'].max())
    print('The most common birth year is ', df['Birth Year'].value_counts())


    # TO DO: Display counts of gender
    
    print('The count of gender is ', df['Gender'].count())

   
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """The function that ask the user if they want to see raw data.
    it print the 5 rows until the user said no"""
    #df1 = df
    length_row = df.shape[0]

    # the for loop start from 0 to number of length of rows with step size 5
    for i in range(0, length_row, 5):
        
        restart = input('\nWould you like to see the raw data? Type \'yes\' or \'no\'\n> ')
        if restart.lower() != 'yes':
            break
        
       
        row_data = df.loc[i: i + 5]
        print(row_data)
        
def birth_year_filter(df):
    
    '''A function that group by birth year and 
    counts the number of month for that year.
    the function  filter for  month less than
    or equal to 4'''
    
    df = df[df['month']  <= 4]
    count = df.groupby(['Birth Year']).count()['month']
    print(count)
    return count

def filter_birth(df):
    '''A function that filter the data of 1941,
    and it  print 7 rows'''
    new_value = df[df['Birth Year'].isin([1941.0])].head(7)
    print(new_value)
    return new_value
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        birth_year_filter(df)
        filter_birth(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
