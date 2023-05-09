# Exercise 6: Nested dictionaries
# ==========
#
# Assume a dictionary that has country names as keys and as values another
# dictionary with the following keys: `continent`, `capital` and `population`.
# Example:
#
#     {
#       'The Netherlands': {
#         'capital': 'Amsterdam',
#         'population': 17283008,
#         'continent': 'Europe',
#       },
#       'France': {
#         'capital': 'Paris',
#         'population': 67186638,
#         'continent': 'Europe',
#       },
#       'USA': {
#         'capital': 'Washington, D.C.',
#         'population': 327167434,
#         'continent': 'North America',
#       }
#     }
#
# - Allow for user input to add new countries in the dictionary.
# - Print the country with the largest population (both its name and its
#   population).
# - Print how many countries are from a particular continent, which is
#   introduced by the user.

countries = {
    'The Netherlands': {
        'capital': 'Amsterdam',
        'population': 17283008,
        'continent': 'Europe',
    },
    'France': {
        'capital': 'Paris',
        'population': 67186638,
        'continent': 'Europe',
    },
    'USA': {
        'capital': 'Washington, D.C.',
        'population': 327167434,
        'continent': 'North America',
    }
}

# - Allow for user input to add new countries in the dictionary.
while True:
    status = input("If you want to exit, type 'yes', otherwise press any other key: ")
    if status == 'yes':
        break
    country = input('Country name: ')
    capital = input('Capital: ')
    population = int(input('Population: '))
    continent = input('Continent: ')
    countries[country] = {'capital': capital,
                          'population': population,
                          'continent': continent}

# - Print the country with the largest population (both its name and its
#   population).
if len(countries) == 0:
    print('No countries in the dictionary.')
else:
    largest_population = 0
    # It could be multiple countries with the same population
    largest_population_countries = []

    for country in countries:
        if countries[country]['population'] > largest_population:
            largest_population = countries[country]['population']

    for country in countries:
        if countries[country]['population'] == largest_population:
            largest_population_countries.append(country)

    # Printing the results
    if len(largest_population_countries) == 1:
        print('{} has the largest population, of {} people.'.format(
            largest_population_countries[0], largest_population))
    else:
        print('The following countries have the largest population:')
        for country in largest_population_countries:
            print('- {}: {}'.format(country, largest_population))


# - Print how many countries are from a particular continent, which is
#   introduced by the user.
continent = input('Introduce the continent: ')
number = 0
for country in countries:
    if countries[country]['continent'] == continent:
        number += 1
print('There are {} countries from {}.'.format(number, continent))
