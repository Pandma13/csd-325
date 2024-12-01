# Megan Wheeler
# Assignment 7.2
# 30 November 2024

def get_city_country(city, country, language='', population=''):

    # generate neatly formatted city and country name
    if population and language:
        city_country_name = f"{city}, {country} - population {population}, {language}"

    elif population:
        city_country_name = f"{city}, {country}, - population {population}"

    elif language:
        city_country_name = f"{city}, {country}, {language}"

    else:
        city_country_name = f"{city}, {country}"

    return city_country_name.title()

print("Enter 'q' at any time to quit.")

while True:

    city = input("\nPlease enter a city name: ")

    if city == 'q':
        break

    country = input("Please enter a country name: ")

    if country == 'q':
        break

    population = input("Please enter the city's population: ")

    if population == 'q':
        break

    language = input("Please enter the city's language: ")

    if language == 'q':
        break

    formatted_city_country = get_city_country(city, country, language, population)

    print(f"\tNeatly formatted name: {formatted_city_country}.")
