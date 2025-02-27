from data import CountyDemographics


# Part 1
# Function takes in list of counties and returns an integer
def population_total(counties:list[CountyDemographics])->int:
    # Total population is set to 0
    total: int = 0
    # For each county 2014 population is taken and added to total
    for county in counties:
        total += county.population["2014 Population"]
    return total

# Part 2

# Function takes in list of counties as well as strint of abbreviation desired
def filter_by_state(counties: list[CountyDemographics], state_abbr: str) -> list[CountyDemographics]:
    # Returns list of counties that contained abbreviation desired
    return [county for county in counties if county.state.upper() == state_abbr.upper()]

# Part 3
# Function takes in list of counties as well as string of education key
def population_by_education(counties: list[CountyDemographics], education_key: str) -> float:
    total: float = 0.0
    # Checks every county in list
    for county in counties:
        # Gets percentage of education key desired for county
        percentage = county.education.get(education_key)
        if percentage is not None:
            # Gets total 2014 population of 2014 county
            pop_2014 = county.population.get("2014 Population", 0)
            # Converts percentage into percentage of 2014 population of county
            total += pop_2014 * (percentage / 100.0)
    return total

# Function takes in list of counties as well as a string of ethnicity key
def population_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> float:
    total: float = 0.0
    # Checks every county in list
    for county in counties:
        # Gets percentage of ethnicity desired
        percentage = county.ethnicities.get(ethnicity_key)
        if percentage is not None:
            # Gets total 2014 population of 2014 county
            population_2014 = county.population.get("2014 Population", 0)
            # Converts percentage into percentage of 2014 population of county
            total +=population_2014 * (percentage / 100.0)
    return total

# Function takes in list of counties
def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total: float = 0.0
    # Checks every county in list
    for county in counties:
        # Gets percentage of people below poverty line in county
        percentage = county.income.get("Persons Below Poverty Level")
        if percentage is not None:
            # Gets total population for 2014 of counties
            population_2014 = county.population.get("2014 Population",0)
            total += population_2014 * (percentage / 100.0)
    return total

# Part 4

# Function takes in list of counties as well as string of education key desired
def percent_by_education(counties: list[CountyDemographics], education_key: str) -> float:

    total_population = 0
    total_education_population = 0.0
    # Checks every county in list
    for county in counties:
        # Get the 2014 population for this county.
        pop_2014 = county.population.get("2014 Population", 0)
        # Adds the 2014 population of county to a total population
        total_population += pop_2014

        # Get the education percentage for the specified key.
        edu_percentage = county.education.get(education_key)
        if edu_percentage is not None:
            total_education_population += pop_2014 * (edu_percentage / 100.0)

    if total_population == 0:
        return 0.0
    return (total_education_population / total_population) * 100.0

# Part 4.1

# Function takes in list of counties as well as string of education key desired
def percent_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> float:

    total_population = 0
    total_ethnicity_population = 0.0
    # Checks every county in list
    for county in counties:
        # Get the 2014 population for this county.
        pop_2014 = county.population.get("2014 Population", 0)
        # Adds the 2014 population of county to a total population
        total_population += pop_2014
        # Gets the percentage of ethnicity key
        ethnicity_percentage = county.ethnicities.get(ethnicity_key)
        if ethnicity_percentage is not None:
            total_ethnicity_population += pop_2014 * (ethnicity_percentage / 100.0)

    if total_population == 0:
        return 0.0
    return (total_ethnicity_population / total_population) * 100.0


# Part 4.2
    # Function takes in list of counties as well as string of education key desired
def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:

    total_population = 0
    total_poverty_population = 0.0
    # Checks every county in list
    for county in counties:
        # Gets population from 2014 population and adds it to the total population
        pop_2014 = county.population.get("2014 Population", 0)
        total_population += pop_2014
        # Gets the percentage of population that is below poverty level
        poverty_percentage = county.income.get("Persons Below Poverty Level")
        if poverty_percentage is not None:
            total_poverty_population += pop_2014 * (poverty_percentage / 100.0)

    if total_population == 0:
        return 0.0
    return (total_poverty_population / total_population) * 100.0

# Part 5
#Function takes in list of counties, a string of education key desired and a float of the percentage
def education_greater_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[
    CountyDemographics]:
    # Creates new list
    result = []
    # Checks every county
    for county in counties:
        # Gets the percentage of the education key from county
        value = county.education.get(education_key)
        # Checks if county is above percentage threshold
        if value is not None and value > threshold:
            result.append(county)
    return result

# Education less than

# Function takes in list of counties, a string of education key desired and a float of the percentage
def education_less_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[
    CountyDemographics]:
    # Creates new list
    result = []
    # Checks every county in list
    for county in counties:
        # Gets the percentage of the education key from county
        value = county.education.get(education_key)
        # Checks if percentage is below percentage threshold
        if value is not None and value < threshold:
            # If county is below threshold county is appended to the new list
            result.append(county)
    return result

# Part 5.1
# Function takes in list of counties, a string of ethnicity key desired and a float of the percentage
def ethnicity_greater_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
    # Creates new list
    result = []
    # Checks every county in list
    for county in counties:
        # Gets the percentage of ethnicity key from county
        value = county.ethnicities.get(ethnicity_key)
        # Checks if percentage is above threshold
        if value is not None and value > threshold:
            # If percentage is above threshold county is appended to new list
            result.append(county)
    return result

# Ethnicity less than
# Function takes in list of counties, a string of ethnicity key desired and a float of the percentage
def ethnicity_less_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
    # Creates new list
    result = []
    # Checks every list in county
    for county in counties:
        # Gets the percentage of ethnicity key from county
        value = county.ethnicities.get(ethnicity_key)
        # Checks if percentage is below threshold
        if value is not None and value < threshold:
            # If percentage is below threshold county is appended to the new list
            result.append(county)
    return result

# Part 5.3
# Function takes in list of counties, a string of people below poverty level and a float of the percentage
def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold:float) -> list[CountyDemographics]:
    # Creates new list
    result = []
    # Checks every county in list
    for county in counties:
        # Gets percentage of people below poverty level for county
        value = county.income.get("Persons Below Poverty Level")
        # Checks if percentage is above percentage threshold
        if value is not None and value > threshold:
            # If percentage is above threshold county is appended to list
            result.append(county)
    return result

# Poverty level less than

# Function takes in list of counties, a string of people below poverty level and a float of the percentage
def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    # Creates new list
    result = []
    # Checks every county in list
    for county in counties:
        # Gets percentage of people below poverty level
        value = county.income.get("Persons Below Poverty Level")
        # Checks if percentage is below percentage threshold
        if value is not None and value < threshold:
            # If county is below threshold it is appended to new list
            result.append(county)
    return result
