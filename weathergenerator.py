from random import randint, choice


# This is the way to store special Unicode characters.
# I hate how they break in dumb operating systems.
degrees = chr(0xBA) + "C"
wind_directions = [chr(0x27A1) + chr(0xFE0F),   # E
                   chr(0x2B05) + chr(0xFE0F),   # W
                   chr(0x2B06) + chr(0xFE0F),   # N
                   chr(0x2B07) + chr(0xFE0F),   # S
                   chr(0x2197) + chr(0xFE0F),   # NE
                   chr(0x2198) + chr(0xFE0F),   # SE
                   chr(0x2199) + chr(0xFE0F),   # SW
                   chr(0x2196) + chr(0xFE0F)]   # NW


class WeatherGenerator:
    current_weather = str()

    def get_weather(self):
        temperature_day = randint(-25, 35)
        temperature_night = temperature_day - randint(3, 15)

        humidity = randint(20, 100)

        wind_speed_min = randint(0, 10)
        wind_speed_max = wind_speed_min + randint(1, 10)
        wind_direction = choice(wind_directions)

        self.current_weather = f"Temperature day: {temperature_day}{degrees}\n" + \
            f"Temperature night: {temperature_night}{degrees}\n" + \
            f"Humidity: {humidity}%\n" + \
            f"Wind: {wind_direction} {wind_speed_min}-{wind_speed_max} m/s"

        return self.current_weather
