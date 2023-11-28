
# TOKEN = "6782805349:AAFVDk09liV2zT0I0OEGV7WR49-BrKD9hrI"
# STICKER_ID = "CAACAgIAAxkBAAECLUJlZYeMgutJzwABDE7tl8_bAVH3w-QAAjwzAAIeN2FIOtfo50BPxfIzBA"
# "-4070673928"

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# Токен вашего бота
TOKEN = "6782805349:AAFVDk09liV2zT0I0OEGV7WR49-BrKD9hrI"

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

posolstvo = "CAACAgIAAxkBAAECLUJlZYeMgutJzwABDE7tl8_bAVH3w-QAAjwzAAIeN2FIOtfo50BPxfIzBA"
nazarov = "CAACAgIAAxkBAAECLZ1lZZ2f5IlMZkFmVFh_HT0e8Vs_rQACKz4AApEw-UqVdgIbBu2QQDME"
vse_v_zhopu = "CAACAgIAAxkBAAECLbtlZaRtg-yLs-tTRyTFN1cNqTbC3wAC1TsAAmPlsEkVPZfw8QXGRDME"
nards = "CAACAgIAAxkBAAECLcNlZaUjqbMIcGoPzt647J6waW6NVQACuDUAAtt9AUrA7DI4OzHIejME"
tryaska = "CAACAgIAAxkBAAECLctlZadA8Xx5ylAcKjKzmnxl4TigKQACV0QAAg8qKUspfw5mYVzAeDME"
cuckold = "CAACAgIAAxkBAAECLfNlZatJJ3d0iJtGY-zAODAI1g2vOAACyDMAAqqh-EoPqEa3La-lDDME"

# Массив слов и соответствующих им стикеров
sticker_mapping = {
    'посольство': posolstvo,
    'штефан': posolstvo,
    'депортация': posolstvo,
    'депортируют': posolstvo,
    'а.н': nazarov,
    'назаров': nazarov,
    "да пошло все в жопу": vse_v_zhopu,
    "нарды": nards,
    "арам": nards,
    "тряска": tryaska,
    "тряски": tryaska,
    "тряску": tryaska,
    "трясусь": tryaska,
    "трястись": tryaska,
    "куколд": cuckold,
    "осуждаем": cuckold,
}

# Обработчик события получения сообщения от пользователя
@dp.message_handler()
async def handle_message(message: types.Message):
    # Проверяем, есть ли слово в массиве
    for word, sticker in sticker_mapping.items():
        if word in message.text.lower():
            # Отправляем стикер в чат
            await message.reply_sticker(sticker)
            break

# Функция запуска бота
async def main():
    # Старт бота
    await dp.start_polling()

# Запускаем бота
if __name__ == '__main__':
    asyncio.run(main())


