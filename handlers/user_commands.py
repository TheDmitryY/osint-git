from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
import requests, json

router = Router()

builed_start = InlineKeyboardBuilder()
builed_start.add(InlineKeyboardButton(
    text="🕵️ Розпочати", callback_data="start_call"
))


@router.message(Command("start"))
async def welcome(message: Message):
    full_name = message.from_user.full_name
    text = f"""
    \n <b> 💎 Ласкаво просимо {full_name}, я бот за допомогою якого ви зможете найти інформцію про людину за допомогою GitHub логіна.</b>
      \n \n <i> ❌ Ми не беремо відповідальність за використання нашого матеріалу в поганих цілях.</i>
      \n \n <i> Натискай кнопу і вперед!</i>
      """
    welcome_sticker_id = "CAACAgIAAxkBAAMMaEVTSLc8AWr20-rIFWLH6nm5GCYAAgUAA8A2TxP5al-agmtNdTYE"
    await message.answer_sticker(sticker=welcome_sticker_id)
    await message.reply(text, reply_markup=builed_start.as_markup(), parse_mode="HTML") 

@router.message(F.sticker)
async def sticker_id(message: Message):
    sticker_ids = message.sticker.file_id
    await message.answer(f'ID: {sticker_ids}')


@router.message(F.text)
async def claim_text(message: Message):
    profile = message.text.strip().lower()
    url = f"https://api.github.com/users/{profile}"
    responce = requests.get(url)
    if responce.status_code == 200:
        data_api = json.loads(responce.text)
        login = str(data_api['login'])
        id = str(data_api['id'])
        name = str(data_api['name'])
        company = str(data_api['company'])
        location = str(data_api['location'])
        email = str(data_api['email'])
        public_repos = str(data_api['public_repos'])
        followers = str(data_api['followers'])
        created_at = str(data_api['created_at'])
        bio = str(data_api['bio'])
        info = f"""👤 Логін: {login}\n🆔 ID: {id}\n🕵️ Імя: {name}\n📔 Компанія: {company}\n🌍 Локація: {location}\n📨 Пошта: {email}\n🔧 Публічні репозиторії: {public_repos}\n👥 Підписників: {followers}\n🕐 Час створення аккаунту: {created_at}\n📌 Біо: {bio}
            """
        await message.reply(info)