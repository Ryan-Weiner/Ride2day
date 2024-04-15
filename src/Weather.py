# import the module
import python_weather

import asyncio
import os
class Weather:
    async def getweather(city):
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
        async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
            # fetch a weather forecast from a city
            weather = await client.get(city)
            
            # returns the current day's forecast temperature (int)
            print(weather.temperature)

            rain = False
            
            # get the weather forecast for a few days
            for daily in weather.daily_forecasts:
                print(daily)
                # hourly forecasts
                for hourly in daily.hourly_forecasts:

                    print(f'{hourly.time}: {hourly.chances_of_rain}')
                    if (hourly.chances_of_rain > 0):
                        rain = True
                    else:
                        print("got here without rain ")

                
                if (rain):
                    print("no riding today :(")
            



if __name__ == '__main__':
  asyncio.run(Weather.getweather(input("Enter your city:\n")))