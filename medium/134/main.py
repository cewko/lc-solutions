def canCompleteCircuit(gas, cost):
    if sum(cost) > sum(gas):
        return -1

    start_station = 0
    total_tank = 0

    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]

        if total_tank < 0:
            total_tank = 0
            start_station = i + 1

    return start_station
