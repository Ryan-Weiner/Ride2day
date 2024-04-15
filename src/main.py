import Weather
import asyncio


city = input("Enter your city:\n")
asyncio.run(Weather.Weather.getweather(city))