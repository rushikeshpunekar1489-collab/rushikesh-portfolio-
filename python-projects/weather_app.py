"""
🌤️ Weather Lookup (CLI)
-----------------------
A simulated weather lookup tool using mock data.
Enter a city name and get the current weather report.

Author: Rushikesh Punekar
"""

import random


WEATHER_DATA = {
    "mumbai": {"temp": 32, "condition": "Partly Cloudy", "humidity": 78, "wind": 14},
    "delhi": {"temp": 28, "condition": "Hazy", "humidity": 55, "wind": 10},
    "bangalore": {"temp": 26, "condition": "Sunny", "humidity": 60, "wind": 12},
    "pune": {"temp": 30, "condition": "Clear Sky", "humidity": 50, "wind": 8},
    "kolkata": {"temp": 31, "condition": "Thunderstorm", "humidity": 85, "wind": 20},
    "chennai": {"temp": 34, "condition": "Hot & Humid", "humidity": 82, "wind": 16},
    "hyderabad": {"temp": 29, "condition": "Sunny", "humidity": 45, "wind": 11},
    "jaipur": {"temp": 27, "condition": "Clear Sky", "humidity": 35, "wind": 9},
    "new york": {"temp": 18, "condition": "Cloudy", "humidity": 65, "wind": 22},
    "london": {"temp": 12, "condition": "Rainy", "humidity": 88, "wind": 28},
    "tokyo": {"temp": 20, "condition": "Overcast", "humidity": 70, "wind": 15},
    "paris": {"temp": 15, "condition": "Partly Cloudy", "humidity": 72, "wind": 18},
}

CONDITION_ICONS = {
    "Sunny": "☀️",
    "Partly Cloudy": "⛅",
    "Cloudy": "☁️",
    "Rainy": "🌧️",
    "Thunderstorm": "⛈️",
    "Clear Sky": "🌙",
    "Hot & Humid": "🥵",
    "Hazy": "🌫️",
    "Overcast": "☁️",
    "Snowy": "❄️",
}


def get_weather(city):
    city_lower = city.strip().lower()
    if city_lower in WEATHER_DATA:
        data = WEATHER_DATA[city_lower].copy()
        # Add small random variance to make it feel dynamic
        data["temp"] += random.randint(-2, 2)
        data["humidity"] = max(0, min(100, data["humidity"] + random.randint(-5, 5)))
        return data
    return None


def display_weather(city, data):
    icon = CONDITION_ICONS.get(data["condition"], "🌡️")

    print(f"\n{'━' * 42}")
    print(f"  {icon}  Weather Report for {city.title()}")
    print(f"{'━' * 42}")
    print(f"  🌡️  Temperature :  {data['temp']}°C")
    print(f"  🌤️  Condition   :  {data['condition']}")
    print(f"  💧  Humidity    :  {data['humidity']}%")
    print(f"  💨  Wind Speed  :  {data['wind']} km/h")
    print(f"{'━' * 42}\n")


def main():
    print("=" * 42)
    print("   🌤️  WEATHER LOOKUP (CLI)  🌤️")
    print("=" * 42)
    print("\nAvailable cities:", ", ".join(c.title() for c in sorted(WEATHER_DATA)))
    print("Type 'quit' to exit.\n")

    while True:
        city = input("Enter city name: ").strip()
        if city.lower() in ("quit", "exit", "q"):
            print("\n👋 Goodbye!")
            break

        data = get_weather(city)
        if data:
            display_weather(city, data)
        else:
            print(f"❌ City '{city}' not found. Try one from the list above.\n")


if __name__ == "__main__":
    main()
