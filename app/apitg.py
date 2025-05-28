import aiohttp, asyncio

API_key_1 = "54e8fc61ee8103dd4ef29a2bf5a4a4e0"
units = 'metric'

API_key_2 = "62f38bb3fda4402aa9d110851252405"


async def edit_open_weather(data):
    lat = data[0]['lat']
    lon = data[0]['lon']
    url1 = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&lang=RU&appid={API_key_1}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url1) as response:
            info = await response.json()
            return info

async def get_data(session, url):
    try:
        async with session.get(url) as response:
            data = await response.json()
            return data
    except aiohttp.ClientError as e:
        print(f"Ошибка при запросе {url}: {e}")
        return None


async def get_weather_data(city):
    urls = [f'http://api.openweathermap.org/geo/1.0/direct?q={city},RU&limit=5&appid={API_key_1}', f"https://api.weatherapi.com/v1/current.json?key={API_key_2}&q={city}&aqi=yes"]
    data =[]
    async with aiohttp.ClientSession() as session:
        # Создаём список задач
        task = [get_data(session, url) for url in urls]

        # Параллельно ждём выполнения всех задач
        data = await asyncio.gather(*task)

    # изменнение open_weather
    data[0] = await edit_open_weather(data[0])
    return data[0], data[1]



