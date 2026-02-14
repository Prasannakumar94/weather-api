def get_weather_emoji(weather_id):

    match weather_id:
        case 200 | 201 | 202 | 210 | 211 | 212 | 221:
            return "🌩️"
        case 230 | 231 | 232:
            return "🌩️"
        case 300 | 301 | 302 | 310 | 311 | 312 | 313 | 314 | 321:
            return "🌧️"
        case 500 | 501 | 502 | 503 | 504:
            return "🌧️"
        case 511:
            return "🌨️"
        case 520 | 521 | 522 | 531:
            return "🌧️"
        case 600 | 601 | 602 | 611 | 612 | 613 | 615 | 616 | 620 | 621 | 622:
            return "❄️"
        case 701 | 711 | 721 | 731 | 741 | 751 | 761 | 771 | 781:
            return "🌫️"
        case 800:
            return "☀️"
        case 801 | 802 | 803 | 804:
            return "☁️"
        case _:
            return "🌍"
