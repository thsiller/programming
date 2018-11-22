from penna.animal import Animal
from penna.genes import Genes
import logging

log = logging.getLogger(__name__)

class SimulationResults(object):
    pass


class SimulationParameters(object):
    pass


def simulate(parameters, steps):
    population = [Animal(parameters.maturity, parameters.birth_rate, parameters.death_rate)
                  for i in range(parameters.num_animals)]

    years = list(range(steps))
    num_animals_by_year = []
    death_cases = []
    dead_age = []

    for year in years:
        log.info('year %s' % year)
        newborns = []
        initial_population = population
        initial_num_animals = len(initial_population)
        for animal in initial_population:
            animal.age_one_year()
            newborns = newborns + animal.give_birth()

        new_population = [animal for animal in initial_population if animal.is_alive]

        num_death_cases = initial_num_animals - len(new_population)
        death_cases.append(num_death_cases)

        dead_age += [animal.age for animal in initial_population if not animal.is_alive]

        population = new_population + newborns
        current_num_animals = len(population)
        log.debug('current number of animals is: %s' % current_num_animals)
        num_animals_by_year.append(current_num_animals)

    results = SimulationResults()
    results.years = years
    results.num_animals_by_year = num_animals_by_year
    results.death_cases = death_cases
    results.dead_age = dead_age

    return results
