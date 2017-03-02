import java.util.Random


class WeatherGenerator {
    var random = Random()
    var time = Time()

    var currentWeather: String = ""

    val hotWeathers = arrayOf("rain", "fair", "shower", "thunderstorm")
    val coldWeathers = arrayOf("snow", "snowstorm", "drizzle")

    val bothWeathers = arrayOf("fog", "wind", "hail", "sunny", "sunny", "sunny",
            "overcast", "overcast", "cloudy", "cloudy")

    fun randomize(): String {
        if (time.isNextDay()) {
            val temperature = randomTemperature()
            var weathers = bothWeathers

            if (temperature >= 0) weathers += hotWeathers
            else weathers += coldWeathers

            currentWeather = "Weather: ${weathers[random.nextInt(weathers.size)]}\n" +
                    "Temperature: ${temperature}ºC"
            return currentWeather
        }
        else {
            return currentWeather
        }
    }

    fun randomTemperature() : Int {
        val min = -20
        val max = 35
        return random.nextInt(max + 1 - min) + min
    }
}
