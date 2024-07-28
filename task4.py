# Define the city lists per country
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# Function to determine the country of a city
def find_country(city):
    if city in india:
        return "India"
    elif city in pakistan:
        return "Pakistan"
    elif city in bangladesh:
        return "Bangladesh"
    else:
        return "Not found in any country"

# Ask user to enter a city name
city_name = input("Enter a city name: ").strip().lower()

# Find and print the country of the entered city
country = find_country(city_name)
print(f"The city '{city_name}' belongs to {country}")
