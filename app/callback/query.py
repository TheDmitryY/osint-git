from aiogram.types import CallbackQuery
from aiogram import Router, F
router = Router()

@router.callback_query(F.data.in_(["start_call"]))
async def process_callback(callback_query: CallbackQuery):
    data = callback_query.data
    if data == "start_call":
        await callback_query.message.answer("📔 Відправте назву профілю")