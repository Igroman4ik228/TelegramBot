from aiogram import types, F, Router
from aiogram.filters import CommandStart, Command

from .keyboards import main_kb, setting_kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Здравствуйте {message.from_user.id}, вас приветствует элитный бот расписания",
                         reply_markup=main_kb(message.from_user.id))


@router.message(F.text.lower().contains("расписание"))
@router.message(Command("schedule"))
async def schedule(message: types.Message):
    await message.answer("Расписание на сегодня") # Из бд 
    
    
@router.message(F.text.lower().contains("настройки"))
@router.message(Command("settings"))
async def setting(message: types.Message):
    await message.reply("Настройки бота...",
                         reply_markup=setting_kb(message.from_user.id))


# @router.callback_query(lambda c: c.data == "ToggleNotification")
# async def toggle_notification_callback(callback_query: types.CallbackQuery):
    
#     current_state = user_notification_state.get(str(callback_query.from_user.id), False)
#     new_state = not current_state
#     user_notification_state[callback_query.from_user.id] = new_state
    
#     save_notification_state(user_notification_state)

#     notification_text = "включены" if new_state else "отключены"
#     await callback_query.answer(f"Уведомления {notification_text}!")
    
#     new_reply_markup = setting_kb(callback_query.from_user.id, user_notification_state)
#     await callback_query.message.edit_reply_markup(reply_markup=new_reply_markup)
