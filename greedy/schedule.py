# -*- using:utf-8 -*-

import sys
import math
import operator
from collections import OrderedDict


def ReadData(fileName):
    file = open(fileName)
    data = []
    i = 0
    for line in file:
        if i == 0:
            i += 1
            continue
        else:
            data.append([int(line.split()[0]),int(line.split()[1])])
    file.close()

    return data


def ScheduleDiff(data):
    """
    decreasing order of weight-length
    maximum weight <= 100
    """
    jobs = {}
    i = 0
    for pair in data:
        jobs[i] = [pair[0]*101.0/100.0 - pair[1]]
        i += 1

    orderedJobs = OrderedDict(sorted(jobs.items(), key=operator.itemgetter(1), reverse=True))

    keys = orderedJobs.keys()
    
    t = 0
    work = 0
    for index in keys:
        t += data[index][1]
        work += data[index][0]*t

    return work


def ScheduleRatio(data):
    """
    decreasing order of weight/length
    """
    jobs = {}
    i = 0
    for pair in data:
        jobs[i] = [pair[0]/pair[1]]
        i += 1

    orderedJobs = OrderedDict(sorted(jobs.items(), key=operator.itemgetter(1), reverse=True))

    keys = orderedJobs.keys()
    
    t = 0
    work = 0
    for index in keys:
        t += data[index][1]
        work += data[index][0]*t

    return work


if __name__ == '__main__':
    data = ReadData('./jobs.txt')
    work1 = ScheduleDiff(data)
    print('Solution1 = ', work1)
    work2 = ScheduleRatio(data)
    print('Solution2 = ', work2)