import pyowm

print('OpenWeatherMap')

owm = pyowm.OWM('07268ae873196e026d66ff5b901d34a0')
observation = owm.weather_at_place('Rostov-on-Don,ru')
weather = observation.get_weather()
location = observation.get_location()

print(owm)
print(observation)
print(weather)
print(location)

