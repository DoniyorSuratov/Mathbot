import asyncio
import random

from aiogram import types

from bot.buttons.language import uzb_lang, eng_lang, lang
from bot.buttons.reply import language_btn, level_btn
from bot.dispatcher import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.types import BotCommand


@dp.message_handler(lambda msg : msg.text in [lang.get(uzb_lang).get("back") , lang.get(eng_lang).get("back")], state="lvl")
@dp.message_handler(commands="start")

async def start_handler(msg: types.Message, state : FSMContext):
    await state.set_state("lang")
    await msg.answer("Language 👇🏿",reply_markup=language_btn())


@dp.message_handler(lambda msg: msg.text in [uzb_lang , eng_lang],state = "lang")
async def welcome_handler(msg: types.Message , state: FSMContext):

    async with state.proxy() as data:
        data["lang"] = msg.text

    logo = "https://telegra.ph/file/0e4336db700202aaf0001.png"
    data = lang.get(msg.text)
    await state.set_state("lvl")
    await msg.answer_photo(logo, data.get("welcome").format(msg.from_user.first_name), reply_markup=level_btn(data))
    await bot.set_my_commands([BotCommand("start" , "qaytadan ishlatish uchun")])
    # link = "[Ташкент, Бектемирский район, массив Сувсоз-2](http://maps.yandex.ru/?text=41.255273,69.375093)"
    # await msg.answer(link , parse_mode="Markdown")










