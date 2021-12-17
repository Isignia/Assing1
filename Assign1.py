#!/usr/bin/env python3

import sys

#This function will show user how to use the programm.
def usage():
    '''The usage function will describe the usage of the script
    
    '''
    return "Usage: Input the data in DD-MM-YYYY format and #of days "

def dbda(start_date, num_days):
    '''
    dbda will take a date in DD-MM-YYYY format, positive or negative integer and return the date either before or after given date according to the value of integer. Will call other functions for calculations
    '''
    error = usage()
    if len(start_date) != 10:
        return "Error, wrong date entered"
    try:
        numd = int(num_days)
        tempdate = start_date
        valid = valid_date(start_date)
        if valid == False:
            sys.exit()
        else:
            while numd != 0:
                if numd > 0:
                    tempdate = after(tempdate)
                    numd = numd - 1 
                else:
                    tempdate = before(tempdate)
                    numd = numd + 1
        error = usage()
        kit = tempdate
        return kit
    except ValueError:
        return error

    
    
def days_in_mon(month):
    ''' Help on function daysinmonth. Proc will check for days in Feb'''
    leapyear = month
    proc = leap_year(leapyear)

    if proc == True:
        feb_max = 29
    elif proc == False:
        feb_max = 28
    mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return mon_max

def valid_date(date):
    ''' Help on valid_date'''
    if len(date) != 10:
        print("Error: wrong date entered ")
    else:
        valid_year = int(date)
        valid_month = int(date)
        valid_day = int(date)
        tempoday = valid_day
        tempomonth = valid_month
        days_in_month = days_in_mon(valid_year)
        if tempomonth > 12 or tempomonth < 1:
            print("Error: wrong month entered")
            return False
        else:
            if tempoday > days_in_month[valid_month]:
                print ("Error: wrong day entered")
                return False
            else:
                next_date = str(tempoday).zfill(2)+"-"+str(tempomonth).zfill(2)+"-"+str(valid_year)
                return next_date
#This is leap year function, will check if its a leap year.

def leap_year(year):
    '''takes a year in YYYY format, and returns True if it's a leap year, False otherwise.'''
    lyear = year
    if lyear % 4 == 0:
        return True
    elif lyear % 100 == 0:
        return False
    elif lyear % 400 == 0:
        return True
    else:
        return False

#This is after function, we will be using global variable to smooth the proccess
def after(today):
    '''after takes a valid date string in DD-MM-YYYY format and returns a date string for the next day in DD-MM-YYYY format.'''
    if len(today) != 10:
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        tmp_day = day + 1 # next day
        mon_max = days_in_mon(year)
        if tmp_day > mon_max[month]:
            to_day = tmp_day % mon_max[month] # if tmp_day > this month's max, reset to 1
            tmp_month = month + 1
        else:
            to_day = tmp_day
            tmp_month = month + 0

        if tmp_month > 12:
            to_month = 1
            year = year + 1
        else:
            to_month = tmp_month + 0

        next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)
        return next_date

def before(prev):
    ''' Help on before function'''
    prevyear = int(prev[0:4])
    prevmonth = int(prev[4:6])
    prevday = int(prev[6:])
    prevday_tempo = prevday -1 
    month_max = days_in_mon(prevyear)

    if prevday_tempo == 0:
        tempo_month = prevmonth - 1
        if tempo_month == 0:
            tempo_month = 12
            current = month_max[tempo_month]
            prevyear = prevyear - 1
        else:
            current = month_max[tempo_month]
    else:
        current = prevday_tempo
        tempo_month = prevmonth + 0
    if tempo_month == 0:
        gmonth = 12
        prevyear = prevyear -1
    else:
        gmonth = tempo_month + 0
    before_date = str(current).zfill(2)+"-"+str(gmonth).zfill(2)+"-"+str(prevyear)
    return before_date

    
if __name__ == "__main__":
    if len(sys.argv) == 3:
        d = sys.argv[1]
        n = sys.argv[2]
        print(dbda(d, n))
    elif len(sys.argv) == 4:
        s = sys.argv[1]
        d = sys.argv[2]
        n = sys.argv[3]
        if s == "--step":
            dbda(d, n)
        else:
            print(usage())
    else:
        print((usage()))
