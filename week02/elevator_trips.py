def elevator_trips(people_weight, people_floor, max_people, max_weight):
    trips = 0
    while len(people_weight) > 0:
        current_floors = [people_floor[indx]for indx, person in enumerate(people_weight) 
                        if sum(people_weight[:indx + 1]) <= max_weight
                        and len(people_weight[:indx + 1]) <= max_people]
        trips += len(set(current_floors)) + 1
        people_weight = people_weight[len(current_floors):]
        people_floor = people_floor[len(current_floors):]

    return trips