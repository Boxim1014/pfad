from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime

def generate_chart(date_str, time_str, lat, lon):
    date = Datetime(date_str, time_str, '+00:00')
    position = (lat, lon)
    chart = Chart(date, position)

    planets = [const.SUN, const.MOON, const.MERCURY, const.VENUS, const.MARS,
               const.JUPITER, const.SATURN, const.URANUS, const.NEPTUNE, const.PLUTO]

    results = {}
    for planet in planets:
        obj = chart.get(planet)
        results[planet] = (obj.sign, obj.signlon)

    return results

# 示例使用
date_of_birth = '1990/01/01'
time_of_birth = '12:00'
latitude = '51n30'  # 伦敦的纬度
longitude = '0w07'  # 伦敦的经度

chart_data = generate_chart(date_of_birth, time_of_birth, latitude, longitude)

for planet, (sign, position) in chart_data.items():
    print(f"{planet}: {sign} {position}")