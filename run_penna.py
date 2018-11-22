import matplotlib.pyplot as plt
from penna.simulation import simulate, SimulationParameters
from utilities.logger import init_logging
import logging

log = logging.getLogger('Penna')
init_logging(log_level='DEBUG')

log.debug('Setup Model Parameters')

# Setup Model Parameters
parameters = SimulationParameters()
parameters.num_animals = 200
parameters.death_rate = 0.05
parameters.maturity = 20
parameters.birth_rate = 0.13

# Number of years simulated
num_years = 1000

# Run the model
log.debug('Run the Simulation')
log.info('Run the Simulation')
log.warning('Run the Simulation')
log.error('Run the Simulation')
result = simulate(parameters, num_years)

# Show results
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