from aiogram.types import Message
from loader import dp
from aiogram.filters import Command


#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("<b>🔍 Yordam</b>\n\n"
        "Quyidagi buyruqlar yordamida botning imkoniyatlaridan foydalanishingiz mumkin:\n\n"
        "<b>1️⃣ /mute</b> - Foydalanuvchini 1 daqiqaga chatda yozish huquqidan mahrum qiladi.\n"
        "<b>2️⃣ /unmute</b> - Foydalanuvchiga yozish huquqini qaytaradi.\n"
        "<b>3️⃣ /ban</b> - Foydalanuvchini guruhdan chiqaradi.\n"
        "<b>4️⃣ /unban</b> - Foydalanuvchining guruhga qaytishiga ruxsat beradi.\n"
        "<b>5️⃣ /set_title Yangi Guruh Nomi</b> - Guruh nomini o'zgartiradi.\n"
        "<b>6️⃣ /set_photo</b> - Guruh rasmni yangilaydi.\n"
        "<b>7️⃣ /set_link</b> - Guruh linkini yangilaydi.\n\n"
        "<b>🔗 Agar qo'shimcha yordam kerak bo'lsa, /about komandasini yuboring yoki adminlarga murojaat qiling.</b>\n\n"
        "<b>🔧 Yordam berishdan mamnunman!</b>", parse_mode="html")
