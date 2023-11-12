import random

def generateRandom(activities, rooms, time, facilitators, days):

    schedules = []

    for i in range(500):
        schedule = []
        for j in activities:
            activity = []
            activity.append(j)
            activity.append(rooms[random.randint(0, (len(rooms)-1))])
            activity.append(time[random.randint(0, (len(time)-1))])
            activity.append(facilitators[random.randint(0, (len(facilitators)-1))])
            activity.append(days[random.randint(0, (len(days)-1))])
            schedule.append(activity)
        schedule.append(1)
        schedules.append(schedule)

    return schedules