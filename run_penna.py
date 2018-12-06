from utilities.logger import init_logging
import logging
from penna.simulation import simulate, SimulationParameters

log = logging.getLogger('Penna')
init_logging(log_level='DEBUG')

try:
    import matplotlib.pyplot as plt
    show_plots = True
except ImportError as e:
    log.exception('Could not import numpy. Error was %s' % e)
    show_plots = False

log.debug('Setup Model Parameters')

# Setup Model Parameters
parameters = SimulationParameters()
parameters.num_animals = 200
parameters.maturity = 3
parameters.birth_rate = 0.2
parameters.deadly_mutations = 8  # animal dies when number of deadly mutations is reached
parameters.initial_mutations = 1
parameters.mutations_per_year = 1
parameters.genes_length = 20

# Number of years simulated
num_years = 1000

# Run the model
log.debug('Run the Simulation')
log.info('Run the Simulation')
log.warning('Run the Simulation')
log.error('Run the Simulation')
result = simulate(parameters, num_years)

# Show results
if show_plots:
    plt.plot(result.years, result.num_animals_by_year)
    plt.ylabel('Number of Animals')
    plt.xlabel('Year')
    plt.show()

    plt.plot(result.years, result.death_cases)
    plt.ylabel('Number of Death Cases')
    plt.xlabel('Year')
    plt.show()

    plt.hist(result.dead_age, bins=range(100+1))
    plt.ylabel('Number')
    plt.xlabel('Dead Age')
    plt.show()
else:
    log.warning("Cannot show plots, maybe matplotlib could not be loaed.")
    print(result.years)
    print(result.num_animals_by_year)
    print(result.death_cases)
    print(result.dead_age)

for animal in result.population:
    print(animal.genes.genes, animal.age)
