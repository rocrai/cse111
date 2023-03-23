import random

def main():
    population_size = int(input("Enter the population size: "))
    initial_infected = int(input("Enter the number of initially infected people: "))
    infection_rate = float(input("Enter the infection rate (between 0 and 1): "))
    recovery_rate = float(input("Enter the recovery rate (between 0 and 1): "))
    num_days = int(input("Enter the number of days to simulate: "))
  
    run_simulation(population_size, initial_infected, infection_rate, recovery_rate, num_days)

def initialize_population(population_size, initial_infected):
    population = ["susceptible"] * (population_size - initial_infected) + ["infected"] * initial_infected
    random.shuffle(population)
    return population

def simulate_day(population, infection_rate, recovery_rate):
    new_population = []
    for person in population:
        if person == "infected":
            if random.random() < recovery_rate:
                new_population.append("recovered")
            else:
                new_population.append("infected")
        else:
            num_infected_neighbors = sum([1 for neighbor in random.sample(population, k=10) if neighbor == "infected"])
            if num_infected_neighbors > 0 and random.random() < infection_rate * num_infected_neighbors:
                new_population.append("infected")
            else:
                new_population.append("susceptible")
    return new_population

def run_simulation(population_size, initial_infected, infection_rate, recovery_rate, num_days):
    population = initialize_population(population_size, initial_infected)
    for day in range(num_days):
        print(f"Day {day}: {population.count('susceptible')} susceptible, {population.count('infected')} infected, {population.count('recovered')} recovered")
        population = simulate_day(population, infection_rate, recovery_rate)

if __name__ == '__main__':
    main()