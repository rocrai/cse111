from datetime import datetime
def main():
    gender = input('Please enter your gender (M or F): ')
    birthday = input('Enter your birthdate (YYYY-MM-DD):')
    pounds  = float(input('Enter your weight in U.S. pounds:'))
    height = float(input('Enter your height in U.S. inches: '))
    years = compute_age(birthday)
    kg = kg_from_lb(pounds)
    cm = cm_from_in(height)
    bmi = body_mass_index(kg, cm)
    bmr = basal_metabolic_rate(gender, kg, cm, years)
    print(f'Age (years): {years}')
    print(f'Weight (kg): {kg:.2f}')
    print(f'Height (cm): {cm:.1f}')
    print(f'Body mass index: {bmi:.1f}')
    print(f'Basal metabolic rate (kcal/day): {bmr:.0f}')
    pass
def kg_from_lb(pounds):
    kg = pounds * 0.45359237
    return kg
def cm_from_in(inches):
    cm = inches * 2.54
    return cm
def body_mass_index(kg, cm):
    bmi = (10000*kg)/(cm**2)
    return bmi
def basal_metabolic_rate(gender, kg, cm, age):
    if gender.lower() == 'f':
        bmr = 447.593 + (9.247*kg) + (3.098*cm) - (4.330*age)
        return bmr
    elif gender.lower() == 'm':
        bmr = 88.362 + (13.397*kg) + (4.799*cm) - (5.677*age)
        return bmr
    else:
        print('choose a gender')

def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years

main()