import random

def genetic (schedules):
    if random.randint(1, 100) == 1:
        mutation = random.randint(len(schedules)/2, len(schedules))
        parents = schedules[:mutation]

        for i in schedules[mutation:]:
            schedules.pop()

        for i in range(0, mutation): #create as many as were removed previously
            random1 = random.randint(0, mutation - 1)
            random2 = random.randint(0, mutation - 1)
            schedule1 = parents[random1]
            schedule2 = parents[random2]

            split = random.randint(1, 10)
            alle1 = schedule1[:split]
            alle2 = schedule2[split:]

            newSchedule = alle1 +alle2

            schedules.append(newSchedule)
    else:
        half = int(((len(schedules))/2))
        parents = schedules[:half]

        for i in schedules[half:]:
            schedules.pop()

        #create as many schedueles as were removed previously
        for i in range(0, half):
            schedule1 = parents[random.randint(0, half - 1)]
            schedule2 = parents[random.randint(0, half - 1)]

            split = random.randint(1, 10)
            alle1 = schedule1[:split]
            alle2 = schedule2[split:]

            newSchedule = alle1 + alle2

            schedules.append(newSchedule)