import json
def read_json(argument):
    with open (argument, 'r') as f:
        data = json.load(f)
    return data
def dump_dictionary_to_json(dict_with_results, number_of_competitors):
    with open('car_racing_result.json', 'w') as fp:
        json.dump(dict_with_results, fp, indent = 4, sort_keys=True)

class Car:
    def __init__ (self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

class Driver:
    def __init__(self, name, car: Car):
        self.name = name
        self.car = car

import random
class Race:
    def __init__(self, drivers):
        self.drivers = drivers
    
    def result(self):
        dict_with_results = {}    
        list_with_speed = [driver.car.max_speed for driver in self.drivers]
        list_with_speed.sort()

        lst_crash_chance = [random.randint(0,5) for x in range(0, len(self.drivers))]
        print(lst_crash_chance)

        points_to_be_awarded = 8
        for index, speed in enumerate(list_with_speed[::-1]):
            for driver in self.drivers:
                if driver.car.max_speed == speed:
                    if(lst_crash_chance[index] == 0):
                        dict_with_results.update({driver.name : 0})
                        continue
                    dict_with_results.update({driver.name : points_to_be_awarded})
                    points_to_be_awarded -= 2
        
        return dict_with_results
        #dump_dictionary_to_json(dict_with_results)

class Championship:
    def __init__(self, name, racers, racers_count):
        self.name = name
        self.racers = racers
        self.racers_count = racers_count

    def competition(self):
        dict_competition = {}
        for index in range(self.racers_count):
            race = Race(self.racers)
            dict_competition.update({'race{0}'.format(index + 1) : race.result()})

        dump_dictionary_to_json({self.name : dict_competition}, len(self.racers))

    def top3(self):
        pass


def main():

    list_of_drivers = []
    cars_data = read_json('cars.json')
    for person in list(cars_data.values()):
        for personal_data in person:
            car = Car(personal_data['car'], personal_data['model'], personal_data['max_speed'])
            list_of_drivers.append(Driver(personal_data['name'], car))
    
    championship = Championship("First competition", list_of_drivers, 3)
    championship.competition()

if __name__ == '__main__':
    main()