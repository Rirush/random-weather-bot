from random import randint

degrees = chr(0xBA) + "C"


class WeatherGenerator:
    current_weather = str()

    def get_weather(self):
        temperature_day = randint(-25, 35)
        temperature_night = temperature_day - randint(3, 15)

        self.current_weather = f"Temperature day: {temperature_day}{degrees}\n" + \
            f"Temperature night: {temperature_night}{degrees}"

        return self.current_weather
