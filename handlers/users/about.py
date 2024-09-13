from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("<b>ℹ️ Bot Haqida</b>\n\n"
        "Men <b>Group Assistant Bot</b>man, sizga guruhda quyidagi funktsiyalarni taqdim etaman:\n\n"
        "<b>👥 Foydalanuvchilarni boshqarish</b>\n"
        "<b>🔇</b> Foydalanuvchilarni vaqtincha bloklash va blokdan chiqarish.\n"
        "<b>🚫</b> Foydalanuvchilarni guruhdan chiqarish va qaytarish.\n\n"
        "<b>🛠️ Guruhni boshqarish</b>\n"
        "<b>🖼️</b> Guruh rasm va nomini yangilash.\n"
        "<b>🔗</b> Guruh linkini yangilash.\n\n"
        "<b>👨‍💻 Botni yaratgan: [Sizning Ismingiz] 🤖</b>\n"
        "<b>📩 Bog'lanish: [Sizning Kontakt Ma'lumotlaringiz]</b>\n\n"
        "<b>Sizga yordam bera olishim uchun tayyorman!</b>", parse_mode="html")

