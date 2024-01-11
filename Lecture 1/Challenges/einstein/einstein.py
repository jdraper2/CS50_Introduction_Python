# Define the main function
def main():
    # Ask the user for the mass and convert it to a float
    mass = float(input("m:"))
    # Calculate the energy equivalent of the mass
    en = energy(mass)
    # Print the energy, rounded to the nearest whole number
    print(f"E: {en:.0f}")

# Define a function that calculates the energy equivalent of a mass
def energy(mass):
    # Return the energy equivalent of the mass using Einstein's mass-energy equivalence formula E=mc^2
    return mass * (pow(300000000, 2))

# Call the main function
main()