# https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
import math

import pandas as pd

def cumsum(a):
    cumsum_ = [0]*len(a)
    cumsum_[0] = a[0]
    for i in range(1,len(a)):
        cumsum_[i] = cumsum_[i-1]+a[i]
    return cumsum_
mon_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 8, 'Aug': 8, 'Sep': 9, 'Oct': 10,
            'Nov': 11, 'Dec': 12}

monthdays_non_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthdays_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def convert_tz(tz_val):
    sign = -1 if tz_val[0] == '-' else 1
    hours = int(tz_val[1:3])
    mins = int(tz_val[3:])

    acc = hours * 60 * 60
    acc += mins * 60
    return acc * sign


def num_leaps_between(year1, year2):
    assert year1 <= year2

    n = 1 if year1 % 4 == 0 else 0
    if year1 % 4 == 0:
        n += int((year2 - year1) / 4)
        return n
    else:
        next_leap = year1 + 4 - (year1 + 4) % 4
        if next_leap >= year2:
            return n
        n += int(math.ceil((year2 - next_leap) / 4.0))
        return n


def parse_time(t_str):
    t_splits = t_str.split(' ')
    t_dict = {}
    t_dict['day'] = int(t_splits[1])
    t_dict['Mon'] = int(mon_dict[t_splits[2]])
    t_dict['Year'] = int(t_splits[3])
    hms = t_splits[4]
    hms_splits = hms.split(':')
    t_dict['Hour'] = int(hms_splits[0])
    t_dict['Min'] = int(hms_splits[1])
    t_dict['Sec'] = int(hms_splits[2])
    t_dict['tz'] = t_splits[5]
    return t_dict


def _timedelta(t1_, t2_):
    sec_diff = t2_['Sec'] - t1_['Sec']
    min_diff = (t2_['Min'] - t2_['Min']) * 60
    hour_diff = (t2_['Hour'] - t2_['Hour']) * 60 * 60
    day_diff = (t2_['Day'] - t2_['Day']) * 24 * 60 * 60


def get_sec_from_year_start(t_):
    # get t1 time from the same year origin
    if t_['Year'] % 4 == 0:
        cum_mon_days = cumsum(monthdays_leap)
    else:
        cum_mon_days = cumsum(monthdays_non_leap)
    mon_idx = t_['Mon'] - 1
    num_days_months_before = 0
    if mon_idx >= 0:
        num_days_months_before = cum_mon_days[mon_idx - 1]
    acc = t_['Sec']
    acc += t_['Min'] * 60
    acc += t_['Hour'] * 60 * 60
    acc += (t_['day'] - 1) * 24 * 60 * 60
    acc += num_days_months_before * 24 * 60 * 60
    return acc


def time_delta(t1, t2):
    t1_dict = parse_time(t1)
    t2_dict = parse_time(t2)
    if t1_dict['Year'] > t2_dict['Year']:
        tmp = t1_dict
        t1_dict = t2_dict
        t2_dict = tmp

    t1_abs = get_sec_from_year_start(t1_dict)
    t1_abs += convert_tz(t1_dict['tz'])
    t2_abs = get_sec_from_year_start(t2_dict)
    t2_abs += convert_tz(t2_dict['tz'])
    n_leaps = num_leaps_between(t1_dict['Year'],t2_dict['Year'])
    diff_year = (t2_dict['Year']-t1_dict['Year'])*365*24*60*60+n_leaps*24*60*60
    delta = diff_year-t1_abs+t2_abs

    return str(abs(delta))


if __name__ == '__main__':
    x1 = pd.to_datetime('2015-05-2T19:54:36+05:30')
    x2 = pd.to_datetime('2015-05-1T13:54:36+00:00')
    print((x1-x2).seconds)
    fptr = open('out.txt', 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()
