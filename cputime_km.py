#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    Professor Janet Brown-Sederberg
    CTIM-285 W01
    04 Mar 2019

"""
jobs = {'A':6,'B':12, 'C':4, 'D':16, 'E':10, 'F':2, 'G':13, 'H':8}
jobs_asc = sorted(jobs, key=jobs.__getitem__)
jobs_desc = sorted(jobs, key=jobs.__getitem__, reverse=True)
total_jobs = 0
for i in range(len(jobs_asc)):
    total_jobs = total_jobs + jobs[jobs_desc[i]]
print("Shortest Job First")
for i in range(len(jobs_asc)):
    print(jobs_asc[i] +" : " + str(jobs[jobs_asc[i]]))
print("Longest Job First")
for i in range(len(jobs_desc)):
    print (jobs_desc[i] +" : " + str(jobs[jobs_desc[i]]))

def print_job(i, jdict, jlist):
    if jdict[jlist[i]] != -1:
        print(jlist[i] +" remaining time: " + str(jdict[jlist[i]]))

def do_job(jdict, jlist):
    for i in range(len(jlist)):
        if jobs[jlist[i]] > -1:
            jobs[jlist[i]] -= 1

print("Shortest Time Remaining")
for i in range(total_jobs):
    do_job(jobs, jobs_asc)
    for j in range(len(jobs_asc)):
        print_job(j, jobs, jobs_asc)

jobs = {'A':6,'B':12, 'C':4, 'D':16, 'E':10, 'F':2, 'G':13, 'H':8}
jobs_asc = sorted(jobs, key=jobs.__getitem__)
jobs_desc = sorted(jobs, key=jobs.__getitem__, reverse=True)

print("Longest Time Remaining")
for i in range(total_jobs):
    do_job(jobs, jobs_desc)
    for j in range(len(jobs_desc)):
        print_job(j, jobs, jobs_desc)

jobs = {'A':6,'B':12, 'C':4, 'D':16, 'E':10, 'F':2, 'G':13, 'H':8}
jobs_asc = sorted(jobs, key=jobs.__getitem__)
jobs_desc = sorted(jobs, key=jobs.__getitem__, reverse=True)

print("Round Robin Priority")
for i in range(total_jobs):
    do_job(jobs, jobs_asc)
    for j in range(len(jobs_asc)):
        print_job(j, jobs, jobs_asc)
    do_job(jobs, jobs_desc)
    for k in range(len(jobs_desc)):
        print_job(k, jobs, jobs_desc)

