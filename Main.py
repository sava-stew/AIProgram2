from Random import generateRandom
from FitnessFunction import fitnessFunction
from Genetic import genetic

def myFunc(e):
    return e[-1]

if __name__ == '__main__':
    activities = [["SLA100A", 50], ["SLA100B", 50], ["SLA191A", 50], ["SLA191B", 50], ["SLA201", 50], ["SLA291", 50],
                  ["SLA303", 60], ["SLA304", 25], ["SLA394", 20], ["SLA449", 60], ["SLA451", 100]]
    rooms = [["Slater 003", 45], ["Roman 216", 30], ["Loft 206", 75], ["Roman 201", 50], ["Loft", 310], ["Beach 201", 60],
             ["Beach 301", 75], ["Logos 325", 450], ["Frank 119", 60]]
    time = [10, 11, 12, 13, 14, 15]
    facilitators = ["Lock", "Glen", "Banks", "Richards", "Shaw", "Singer", "Uther", "Tyler", "Numen", "Zeldin"]
    days = ["M", "W", "F"]
    preferredFacilitators = [["SLA100A", ["Glen", "Lock", "Banks", "Zeldin"], ["Numen", "Richards"]],
                             ["SLA100B", ["Glen", "Lock", "Banks", "Zeldin"], ["Numen", "Richards"]],
                             ["SLA191A", ["Glen", "Lock", "Banks", "Zeldin"], ["Numen", "Richards"]],
                             ["SLA191B", ["Glen", "Lock", "Banks", "Zeldin"], ["Numen", "Richards"]],
                             ["SLA201", ["Glen", "Banks", "Zeldin", "Shaw"], ["Numen", "Richards", "Singer"]],
                             ["SLA291", ["Locks", "Banks", "Zeldin", "Singer"], ["Numen", "Richards", "Shaw", "Tyler"]],
                             ["SLA303", ["Glen", "Zeldin", "Banks"], ["Numen", "Singer", "Shaw"]],
                             ["SLA304", ["Glen", "Banks", "Tyler"], ["Numen", "Singer", "Shaw", "Richards", "Uther", "Zeldin"]],
                             ["SLA394", ["Tyler", "Singer"], ["Richards", "Zeldin"]],
                             ["SLA449", ["Tyler", "Singer", "Shaw"], ["Zeldin", "Uther"]],
                             ["SLA451", ["Tyler", "Singer", "Shaw"], ["Zeldin", "Uther", "Richards", "Banks"]]]

    previousAverage = 1
    improvement = 0

    randomSchedules = generateRandom(activities, rooms, time, facilitators, days)
    schedules = fitnessFunction(randomSchedules, preferredFacilitators)

    for i in range(1, 100):
        averageFitness = 0
        schedules.sort(reverse = True, key=myFunc)
        print(schedules[0])
        genetic(schedules)
        schedules = fitnessFunction(randomSchedules, preferredFacilitators)
        for j in schedules:
            averageFitness += j[-1]
        currentAverage = averageFitness
        improvement = previousAverage/previousAverage
        previousFitness = currentAverage

    schedules.sort(reverse = True, key = myFunc)

    while improvement < .01:
        averageFitness = 0
        schedules.sort(reverse = True, key=myFunc)
        print(schedules[0])
        genetic(schedules)
        schedules = fitnessFunction(randomSchedules, preferredFacilitators)
        for j in schedules:
            averageFitness += j[-1]
        currentAverage = averageFitnesss
        improvement = previousAverage/previousAverage
        previousFitness = currentAverage


    schedules.sort(reverse = True, key = myFunc)


    with open(r'output.txt', 'w') as output:
        for i in schedules[0]:
            output.write(str(i))
            output.write("\n")