import sys

def sum_times():
    time_1, time_2, sum_time = dict(), dict(), dict()
    time_1['h'] = int(input('Enter hour of time 1: '))
    time_1['m'] = int(input('Enter minute of time 1: '))
    time_1['s'] = int(input('Enter second of time 1: '))
    time_2['h'] = int(input('Enter hour of time 2: '))
    time_2['m'] = int(input('Enter minute of time 2: '))
    time_2['s'] = int(input('Enter second of time 2: '))
    sum_time['h'] = time_1['h'] + time_2['h']
    sum_time['m'] = time_1['m'] + time_2['m']
    sum_time['s'] = time_1['s'] + time_2['s']
    if sum_time['s'] >= 60:
        sum_time['m'] += 1
        sum_time['s'] -= 60
    if sum_time['m'] >= 60:
        sum_time['h'] += 1
        sum_time['m'] -= 60
    print('{}:{}:{}'.format(sum_time['h'], sum_time['m'], sum_time['s']))

def subtract_times():
    time_1, time_2, sub_time = dict(), dict(), dict()
    time_1['h'] = int(input('Enter hour of time 1: '))
    time_1['m'] = int(input('Enter minute of time 1: '))
    time_1['s'] = int(input('Enter second of time 1: '))
    time_2['h'] = int(input('Enter hour of time 2: '))
    time_2['m'] = int(input('Enter minute of time 2: '))
    time_2['s'] = int(input('Enter second of time 2: '))
    sub_time['h'] = time_1['h'] - time_2['h']
    sub_time['m'] = time_1['m'] - time_2['m']
    sub_time['s'] = time_1['s'] - time_2['s']
    if sub_time['s'] < 0:
        sub_time['m'] -= 1
        sub_time['s'] += 60
    if sub_time['m'] <0:
        sub_time['h'] -= 1
        sub_time['m'] += 60
    print('{}:{}:{}'.format(sub_time['h'], sub_time['m'], sub_time['s']))

def convert_time2seconds():
    org_time = dict()
    org_time['h'] = int(input('Enter hour of time: '))
    org_time['m'] = int(input('Enter minute of time: '))
    org_time['s'] = int(input('Enter second of time: '))
    converted_time = org_time['h'] * 3600 + org_time['m'] * 60 + org_time['s']
    print('{} seconds'.format(converted_time))

def convert_seconds2time():
    org_time = int(input('Enter time in seconds: '))
    converted_time = dict()
    converted_time['h'] = org_time // 3600
    org_time = org_time % 3600
    converted_time['m'] = org_time // 60
    converted_time['s'] = org_time % 60
    print('{}:{}:{}'.format(converted_time['h'], converted_time['m'], converted_time['s']))

def exit():
    sys.exit()

if __name__ == '__main__':
    while True:
        print('1- Sum of two times\n2- Subtraction of two times\n3- Convert seconds to time\n4- Convert time to seconds\n5- Exit')
        operation = input('Enter your operation: ')
        if operation == '1':
            sum_times()
        elif operation == '2':
            subtract_times()
        elif operation == '3':
            convert_seconds2time()
        elif operation == '4':
            convert_time2seconds()
        elif operation == '5':
            exit()
        else:
            print('Wrong operation')
