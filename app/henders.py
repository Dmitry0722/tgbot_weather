import types
import dp
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.types import InputMediaPhoto
import os
import app.keywords as kb
from aiogram.types import InputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.apitg import get_weather_data

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Это бот, в котором ты можешь посмотреть погоду!", reply_markup=kb.main)

@router.message(F.text == 'О нас')
async def about_us(message: Message):
    await message.answer("йоу, это бот, который поможет вам одеться по погоде и поднимет настроение! 🐩☂️\nскорее выбирай свой город и вычитай от влажности ~20%❗️")

@router.message(F.text == 'Погода')
async def gorod(message: Message):
    await message.answer('Выберите город', reply_markup=kb.gorod)



from aiogram.types import FSInputFile  # Используем FSInputFile вместо InputFile

@router.callback_query(F.data == 'Moscow')
async def moscow(callback: CallbackQuery):
    await callback.answer('Загружаем погоду для Москвы...')

    owm_data, wa_data = await get_weather_data("Moscow")

    if wa_data:
        media = await format_weather_message(owm_data, wa_data)
        if media:
            await callback.message.answer_media_group([media])
        else:
            await callback.message.answer("⚠️ Не удалось сформировать прогноз")
    else:
        await callback.message.answer("⚠️ Не удалось получить данные о погоде")

@router.callback_query(F.data == 'Chelyabinsk')
async def chelyabinsk(callback: CallbackQuery):
    await callback.answer('Загружаем погоду для Челябинска...')

    owm_data, wa_data = await get_weather_data("Chelyabinsk")

    if wa_data:
        media = await format_weather_message(owm_data, wa_data)
        if media:
            await callback.message.answer_media_group([media])
        else:
            await callback.message.answer("⚠️ Не удалось сформировать прогноз")
    else:
        await callback.message.answer("⚠️ Не удалось получить данные о погоде")

@router.callback_query(F.data == 'Tyumen')
async def tyumen(callback: CallbackQuery):
    await callback.answer('Загружаем погоду для Тюмени...')


    owm_data, wa_data = await get_weather_data("Tyumen")

    if wa_data:
        media = await format_weather_message(owm_data, wa_data)
        if media:
            await callback.message.answer_media_group([media])
        else:
            await callback.message.answer("⚠️ Не удалось сформировать прогноз")
    else:
        await callback.message.answer("⚠️ Не удалось получить данные о погоде")

@router.callback_query(F.data == 'Zlatoust')
async def zlatoust(callback: CallbackQuery):
    await callback.answer('Загружаем погоду для Златоуста...')

    owm_data, wa_data = await get_weather_data("Zlatoust")

    if wa_data:
        media = await format_weather_message(owm_data, wa_data)
        if media:
            await callback.message.answer_media_group([media])
        else:
            await callback.message.answer("⚠️ Не удалось сформировать прогноз")
    else:
        await callback.message.answer("⚠️ Не удалось получить данные о погоде")



@router.callback_query(F.data == 'Kostroma')
async def kostroma(callback: CallbackQuery):
    await callback.answer('Загружаем погоду для Костромы...')

    owm_data, wa_data = await get_weather_data("Kostroma")

    if wa_data:
        media = await format_weather_message(owm_data, wa_data)
        if media:
            await callback.message.answer_media_group([media])
        else:
            await callback.message.answer("⚠️ Не удалось сформировать прогноз")
    else:
        await callback.message.answer("⚠️ Не удалось получить данные о погоде")



@router.callback_query(F.data == 'Kirov')
async def kirov(callback: CallbackQuery):
    await callback.answer('Загружаем погоду для Киров...')

    owm_data, wa_data = await get_weather_data("Kirov")

    if wa_data:
        media = await format_weather_message(owm_data, wa_data)
        if media:
            await callback.message.answer_media_group([media])
        else:
            await callback.message.answer("⚠️ Не удалось сформировать прогноз")
    else:
        await callback.message.answer("⚠️ Не удалось получить данные о погоде")


@router.callback_query(F.data == 'Kaliningrad')
async def kaliningrad(callback: CallbackQuery):
    await callback.answer('Загружаем погоду для Калининград...')

    owm_data, wa_data = await get_weather_data("Kaliningrad")

    if wa_data:
        media = await format_weather_message(owm_data, wa_data)
        if media:
            await callback.message.answer_media_group([media])
        else:
            await callback.message.answer("⚠️ Не удалось сформировать прогноз")
    else:
        await callback.message.answer("⚠️ Не удалось получить данные о погоде")

@router.callback_query(F.data == 'Ekaterinburg')
async def ekaterinburg(callback: CallbackQuery):
    await callback.answer('Загружаем погоду для Екатеринбурга...')

    owm_data, wa_data = await get_weather_data("Ekaterinburg")

    if wa_data:
        media = await format_weather_message(owm_data, wa_data)
        if media:
            await callback.message.answer_media_group([media])
        else:
            await callback.message.answer("⚠️ Не удалось сформировать прогноз")
    else:
        await callback.message.answer("⚠️ Не удалось получить данные о погоде")

@router.callback_query(F.data == 'Korenovsk')
async def korenovsk(callback: CallbackQuery):
    await callback.answer('Загружаем погоду для Кореновска...')

    owm_data, wa_data = await get_weather_data("Korenovsk")

    if wa_data:
        media = await format_weather_message(owm_data, wa_data)
        if media:
            await callback.message.answer_media_group([media])
        else:
            await callback.message.answer("⚠️ Не удалось сформировать прогноз")
    else:
        await callback.message.answer("⚠️ Не удалось получить данные о погоде")

@router.callback_query(F.data == 'Ufa')
async def ufa(callback: CallbackQuery):
    await callback.answer('Загружаем погоду для Уфы...')

    owm_data, wa_data = await get_weather_data("Ufa")

    if wa_data:
        media = await format_weather_message(owm_data, wa_data)
        if media:
            await callback.message.answer_media_group([media])
        else:
            await callback.message.answer("⚠️ Не удалось сформировать прогноз")
    else:
        await callback.message.answer("⚠️ Не удалось получить данные о погоде")
@router.callback_query(F.data == 'Kurgan')
async def kurgan(callback: CallbackQuery):
    await callback.answer('Загружаем погоду для Кургана...')

    owm_data, wa_data = await get_weather_data("Kurgan")

    if wa_data:
        media = await format_weather_message(owm_data, wa_data)
        if media:
            await callback.message.answer_media_group([media])
        else:
            await callback.message.answer("⚠️ Не удалось сформировать прогноз")
    else:
        await callback.message.answer("⚠️ Не удалось получить данные о погоде")

@router.callback_query(F.data == 'Kemerovo')
async def kemerovo(callback: CallbackQuery):
    await callback.answer('Загружаем погоду для Кемерово...')

    owm_data, wa_data = await get_weather_data("Kemerovo")

    if wa_data:
        media = await format_weather_message(owm_data, wa_data)
        if media:
            await callback.message.answer_media_group([media])
        else:
            await callback.message.answer("⚠️ Не удалось сформировать прогноз")
    else:
        await callback.message.answer("⚠️ Не удалось получить данные о погоде")

@router.callback_query(F.data == 'Kazan')
async def kazan(callback: CallbackQuery):
    await callback.answer('Загружаем погоду для Казани...')

    owm_data, wa_data = await get_weather_data("Kazan")

    if wa_data:
        media = await format_weather_message(owm_data, wa_data)
        if media:
            await callback.message.answer_media_group([media])
        else:
            await callback.message.answer("⚠️ Не удалось сформировать прогноз")
    else:
        await callback.message.answer("⚠️ Не удалось получить данные о погоде")


async def format_weather_message(owm_data: dict, wa_data: dict) -> tuple:
    try:
        # Формируем текстовое сообщение
        city = wa_data.get('location', {}).get('name', 'Неизвестный город')

        details_owm = [
            "Прогноз c openweathermap:",
            f"🌏Погода: {owm_data['weather'][0]['description']}",
            f"💧Влажность: {owm_data['main']['humidity']}%",
            f"🌡Температура: {owm_data['main']['temp']}℃\nОщущается как: {owm_data['main']['feels_like']}℃",
            f"💨Скорость ветра: {owm_data['wind']['speed']}м/с\n",
        ]

        details_wa = [
            "Прогноз c Weatherapi:",
            f"🌏Погода: {wa_data['current']['condition']['text']}",
            f"💧Влажность: {wa_data['current']['humidity']}%",
            f"🌡Температура: {wa_data['current']['temp_c']}℃\nОщущается как: {wa_data['current']['feelslike_c']}℃",
            f"💨Скорость ветра: {wa_data['current']['wind_kph'] * 1000 / 3600:.1f}м/с\n",
        ]

        message = "\n".join([
            f"🌦 Погода в {city}",
            *details_owm, *details_wa,
            f"\nОбновлено: {wa_data.get('current', {}).get('last_updated', '')}"
        ])

        # Создаем медиа объект с фото
        photo_path = r"C:\Users\annae\Desktop\фото погоды\ааааа.jpg"
        media = InputMediaPhoto(
            media=FSInputFile(photo_path),
            caption=message
        )

        if  wa_data['current']['condition']['text'] == "Sunny":
            photo_path = r"C:\Users\annae\Desktop\фото погоды\гаити.jpg"
            media = InputMediaPhoto(
                media=FSInputFile(photo_path),
                caption=message
            )

        if  wa_data['current']['condition']['text'] == "Clear":
            photo_path = r"C:\Users\annae\Desktop\фото погоды\ясно-понятно.jpg"
            media = InputMediaPhoto(
                media=FSInputFile(photo_path),
                caption=message
            )

        if owm_data['main']['humidity'] >= 80 and owm_data['main']['temp'] <= 2:
            photo_path = r"C:\Users\annae\Desktop\фото погоды\смог.jpg"
            media = InputMediaPhoto(
                media=FSInputFile(photo_path),
                caption=message
            )

        if owm_data['main']['temp'] <= -15:
            photo_path = r"C:\Users\annae\Desktop\фото погоды\шашлыки.jpg"
            media = InputMediaPhoto(
                media=FSInputFile(photo_path),
                caption=message
            )

        if owm_data['main']['temp'] >= -4 and owm_data['main']['temp'] <= -2:
            photo_path = r"C:\Users\annae\Desktop\фото погоды\мэри-попинс.jpg"
            media = InputMediaPhoto(
                media=FSInputFile(photo_path),
                caption=message
            )

        if owm_data['main']['temp'] >= 15 and wa_data['current']['condition']['text'] == "Clear":
            photo_path = r"C:\Users\annae\Desktop\фото погоды\пиво.jpg"
            media = InputMediaPhoto(
                media=FSInputFile(photo_path),
                caption=message
            )

        if (city == "Zlatoust" or city == "Tyumen" or city == "Ekaterinburg" or city == "Chelyabinsk" ) and owm_data['weather'][0]['description'] == "Sunny" and owm_data['main']['temp'] >= 20:
            photo_path = r"C:\Users\annae\Desktop\фото погоды\осел.jpg"
            media = InputMediaPhoto(
                media=FSInputFile(photo_path),
                caption=message
            )

        if owm_data['main']['temp'] >= 10 and owm_data['main']['temp'] < 15:
            photo_path = r"C:\Users\annae\Desktop\фото погоды\лежак.jpg"
            media = InputMediaPhoto(
                media=FSInputFile(photo_path),
                caption=message
            )

        if owm_data['main']['humidity'] == 100:
            photo_path = r"C:\Users\annae\Desktop\фото погоды\корова.jpg"
            media = InputMediaPhoto(
                media=FSInputFile(photo_path),
                caption=message
            )

        if owm_data['wind']['speed'] >= 10:
            photo_path = r"C:\Users\annae\Desktop\фото погоды\ураган.jpg"
            media = InputMediaPhoto(
                media=FSInputFile(photo_path),
                caption=message
            )






        return media


    except Exception as e:
        print(f"Ошибка форматирования: {e}")
        return None