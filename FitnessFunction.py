def fitnessFunction(schedules, preferred):
    for i in schedules:
        i.remove(i[-1])

        roomPoints = room(i)
        facilitatorPoints = facilitator(i, preferred)
        facilitatorActivitiesPoints = facilitatorActivities(i)
        facilitatorTimesPoints = facilitatorTimes(i)
        multipleSectionsPoints = multipleSections(i)
        correspondingSectionsPoints = correspondingSections(i)

        points = roomPoints + facilitatorPoints + facilitatorActivitiesPoints + facilitatorTimesPoints + \
                 multipleSectionsPoints + correspondingSectionsPoints


        i.append(points)


    return schedules


def room(schedule):
    points = 0

    roomSchedule = {}

    for i in schedule:
        j = i[0]
        k = i[1]
        expected = j[1]
        capacity = k[1]

        #activity is in a room too small for expected enrollement
        if capacity < expected:
            points -= .5
        #activity is in a room with capacity >3 times expected enrollement
        if (capacity/expected) > 3:
            #activity is in a room with capacity >6 times expected enrollement
            if(capacity/expected) > 6:
                points -= .4
            points -= .2
        else:
            points += .3

        if j[0] not in roomSchedule:
            roomSchedule[j[0]] = [k[0], i[2], i[4]]

    for i in roomSchedule:
        for j in roomSchedule:
            #activity is scheduled at the same time in the same room as another of the activities
            if roomSchedule[i] == roomSchedule[j]:
                points -= .5

    return points


def facilitator(schedule, preferred):
    points = 0

    for i in schedule:
        facilitator = i[3]
        j = i[0]
        activity = j[0]

        for k in preferred:
            if activity == k[0]:
                #activity is overseen by a preferred facilitator
                if facilitator in k[1]:
                    points += .5
                #activity is overseen by another facilitator listed for that activity
                elif facilitator in k[2]:
                    points += 2
                #activity is overseen by some other facilitator
                else:
                    points -= .1

    return points


def facilitatorActivities(schedule):
    points = 0

    numActivities = {}

    #keeps track of how many activities each facilitator is scheduled for
    for i in schedule:
        if i[3] not in numActivities:
            numActivities[i[3]] = 1
        elif i[3] in numActivities:
            numActivities[i[3]] += 1

    for i in numActivities:
        #facilitator is scheduled to oversee more than 4 activities total
        if numActivities[i] > 4:
            points -= .5
        #facilitator is scheduled to oversee 1 or 2 activities
        if numActivities[i] == 1 or numActivities[i] == 2:
            #Dr. Tyler can oversee less than 2 activities
            if i != "Tyler":
                points -= .4

    return points


def facilitatorTimes(schedule):
    points = 0

    activityTimes = {}

    #keeps track of how dates/times facilitator is scheduled for and if overlap
    for i in schedule:
        if i[3] not in activityTimes:
            activityTimes[i[3]] = [[i[2], i[4], 1]]
        elif i[3] in activityTimes:
            value = activityTimes[i[3]] #give the values as a list
            newInfo = [i[2], i[4]]
            check = True
            for j in value:
                if (newInfo[0] in j) and (newInfo[1] in j):
                    check = True
                else:
                    check = False

                if check:
                    scheduled = j[2]
                    scheduled += 1
                    j[2] = scheduled
                    break

            if not check:
                update = activityTimes[i[3]]
                newInfo.append(1)
                update.append(newInfo)

    for i in activityTimes:
        value = activityTimes[i]
        for j in value:
            #activity facilitator is scheduled for only one activity in this time slot
            if j[2] == 1:
                points += .2
            #activity facilitator is scheduled for more than one activity at the same time
            else:
                points -= .2
            for k in value:
                #activity facilitator has activities same day
                if j[1] == k[1]:
                    #activity facilitator has consecutive time slots
                    if j[0] == (k[0] + 1):
                        consecPoints = facultyConsecutive(schedule, j[1], j[0], k[0] + 1, i);
                        points += consecPoints
                    if j[0] == (k[0] -1):
                        consecPoints = facultyConsecutive(schedule, j[1], j[0], k[0] - 1, i);
                        points += consecPoints

    return points


def facultyConsecutive(schedule, day, time1, time2, name):
    room1 = ""
    room2 = ""

    for i in schedule:
        room = i[1]
        classRoom = room[0]
        if i[4] == day:
            if i[2] == time1:
                room1 = classRoom
            if i[2] == time2:
                room2 = classRoom

    #in the case of conseuctive time slots, one of the activities is in Roman or Beach, and the other isn't
    if (room1 == "Roman" or "Beach") and (room2 == "Roman" or "Beach"):
        return 0
    else:
        return -.4

def multipleSections(schedule):
    points = 0

    section = ""
    time1 = 0
    time2 = 0
    room1 = ""
    room2 = ""

    for i in schedule:
        index = 1
        if "SLA100" in i[0][0]:
            listRemainder = schedule[index::]
            for j in listRemainder:
                classInfo2 = j[0]
                if "SLA100" in classInfo2:
                    section = "SLA100"
                    time1 = i[2]
                    time2 = j[2]
                    room1 = i[1][0]
                    room2 = j[1][0]
                    break
        if "SLA191" in i[0][0]:
            listRemainder = schedule[index::]
            for j in listRemainder:
                classInfo2 = j[0]
                if "SLA191" in classInfo2:
                    section = "SLA191"
                    time1 = i[2]
                    time2 = i[2]
                    room1 = i[1][0]
                    room2 = j[1][0]
                    break
        index += 1

    if section == "SLA100":
        #the two sections of SLA 100 are more than 4 hours apart
        if abs(time1 - time2) > 4:
            points += .5
        #both sections of SLA 100 are in the same time slot
        if time1 == time2:
            points -= .5
    if section == "SLA191":
        #the two sections of SLA 191 are more than 4 hours apart
        if abs(time1 - time2) > 4:
            points += .5
        #both sections of SLA 191 are in the same time slot
        if time1 == time2:
            points -= .5

    return points


def correspondingSections(schedule):
    points = 0

    section = ""
    time1 = 0
    time2 = 0
    room1 = ""
    room2 = ""
    corresponding = False

    for i in schedule:
        index = 1
        if "SLA100" in i[0][0]:
            listRemainder = schedule[index::]
            for j in listRemainder:
                classInfo2 = j[0]
                if "SLA191" in classInfo2:
                    corresponding = True
                    time1 = i[2]
                    time2 = j[2]
                    room1 = i[1][0]
                    room2 = j[1][0]
                    break

    if corresponding:
        #the section of SLA 191 and 101 are overseen in consecutive time slots
        if (time1 == time2 + 1) or (time1 == time2 - 1):
            points += .5
            #In the case of consecutive time slots, one of the activities is in Roman or Beack, and the other isn't
            if (room1 == "Roman" or "Beach") and (room2 == "Roman" or "Beach"):
                points += 0
            else:
                points -= .4
        #a section of SLA 191 and a section of SLA 101 are taught seperated by 1 hour
        if abs(time1 - time2) == 1:
            points += .25
        #a section of SLA 191 and a section of SLa 101 are taught in the same time slot
        if time1 == time2:
            points -= .25

    return points