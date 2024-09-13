from aiogram.types import Message
from aiogram import F
from loader import dp,db,bot,CHANNELS
from aiogram.filters import CommandStart,Command,and_f
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import time
from aiogram.types import Message,ChatPermissions
import logging

logging.basicConfig(level=logging.INFO)

# /start komandasi
@dp.message(CommandStart())
async def start_command(message: Message):
    full_name = message.from_user.full_name
    user_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name, telegram_id=telegram_id)  # Foydalanuvchi bazaga qo'shildi
        await message.answer(text=f"👋 Salom {user_name}!\n\n"
        "Men sizning botingizman va quyidagi funktsiyalarni bajarishim mumkin:\n\n"
        "🔧 Iltimos, buyruqlarni tekshirish uchun /help komandasini yuboring.\n"
        "ℹ️ Ma'lumot uchun /about komandasini yuboring.\n\n"
        "Sizga yordam bera olishim uchun tayyorman! 😊\n\n"
        "Guruhdagi buyruqlarni ishlatishda ehtiyot bo'ling va ehtiyojlaringiz bo'lsa, adminlarga murojaat qiling.")
    except:
        await message.answer(text=f"👋 Salom {user_name}!\n\n"
        "Men sizning botingizman va quyidagi funktsiyalarni bajarishim mumkin:\n\n"
        "🔧 Iltimos, buyruqlarni tekshirish uchun /help komandasini yuboring.\n"
        "ℹ️ Ma'lumot uchun /about komandasini yuboring.\n\n"
        "Sizga yordam bera olishim uchun tayyorman! 😊\n\n"
        "Guruhdagi buyruqlarni ishlatishda ehtiyot bo'ling va ehtiyojlaringiz bo'lsa, adminlarga murojaat qiling.")


# Guruhga yangi a'zo qo'shilganda
@dp.message(F.new_chat_member)
async def new_member(message: Message):
    user = message.new_chat_member.get("first_name")
    welcome_message = f"🎉 {user}, guruhimizga xush kelibsiz! 😊\nSiz bilan tanishishdan mamnunmiz! 🌟"
    await message.answer(welcome_message)
    await message.delete()

# Guruhdan a'zo chiqib ketganda
@dp.message(F.left_chat_member)
async def member_left(message: Message):
    user = message.left_chat_member.full_name
    goodbye_message = f"😢 {user}, siz bilan xayrlashamiz! 🌙\nYana qaytib kelishingizni kutamiz! 🙌"
    await message.answer(goodbye_message)
    await message.delete()


# Adminlarni tekshirish uchun yordamchi funksiya
async def is_admin(chat_id: int, user_id: int) -> bool:
    admins = await bot.get_chat_administrators(chat_id)
    return any(admin.user.id == user_id for admin in admins)


@dp.message(Command('set_title'))
async def set_group_title(message: Message):
    if await is_admin(message.chat.id, message.from_user.id):
        title = message.text.split(maxsplit=1)[1]
        await message.chat.set_title(title)
        await message.answer(f"Guruh nomi {title} qilib o'zgartirildi. ✅")
    else:
        await message.answer("⛔ Sizda bu kommandani bajarish uchun huquq yo'q!")

# Guruh linkini o'zgartirish
@dp.message(Command('set_link'))
async def set_group_link(message: Message):
    if await is_admin(message.chat.id, message.from_user.id):
        try:
            # Yangi taklif linkini yaratish
            new_link = await bot.export_chat_invite_link(message.chat.id)
            await message.answer(f"Guruh linki muvaffaqiyatli yangilandi. 🔗 Yangi link: {new_link}")
        except Exception as e:
            await message.answer(f"⚠️ Xatolik yuz berdi: {str(e)}")
    else:
        await message.answer("⛔ Sizda bu kommandani bajarish uchun huquq yo'q!")


# Foydalanuvchini ban qilish
@dp.message(Command('ban'))
async def ban_user(message: Message):
    if await is_admin(message.chat.id, message.from_user.id):
        user_id = message.reply_to_message.from_user.id
        await message.chat.ban_user(user_id)
        await message.answer(f"🚫 {message.reply_to_message.from_user.first_name} guruhdan chiqarildi. ❌")
        await message.delete()  # Xabarni o'chirish, foydalanuvchilar ko'rmasligi uchun
    else:
        await message.answer("⛔ Sizda bu kommandani bajarish uchun huquq yo'q!")

# Foydalanuvchini unban qilish
@dp.message(Command('unban'))
async def unban_user(message: Message):
    if await is_admin(message.chat.id, message.from_user.id):
        user_id = message.reply_to_message.from_user.id
        await message.chat.unban_user(user_id)
        await message.answer(f"✅ {message.reply_to_message.from_user.first_name} guruhga qaytishingiz mumkin! 🎉")
        await message.delete()  # Xabarni o'chirish, foydalanuvchilar ko'rmasligi uchun
    else:
        await message.answer("⛔ Sizda bu kommandani bajarish uchun huquq yo'q!")

# Foydalanuvchini mute qilish
@dp.message(Command('mute'))
async def mute_user(message: Message):
    if await is_admin(message.chat.id, message.from_user.id):
        user_id = message.reply_to_message.from_user.id
        permission = ChatPermissions(can_send_messages=False)
        until_date = int(time.time()) + 60  # 1 daqiqaga mute qilinadi
        await message.chat.restrict(user_id=user_id, permissions=permission, until_date=until_date)
        await message.answer(f"🔇 {message.reply_to_message.from_user.first_name} 1 daqiqaga bloklandi. ⏳")
        await message.delete()  # Xabarni o'chirish, foydalanuvchilar ko'rmasligi uchun
    else:
        await message.answer("⛔ Sizda bu kommandani bajarish uchun huquq yo'q!")

# Foydalanuvchini unmute qilish
@dp.message(Command('unmute'))
async def unmute_user(message: Message):
    if await is_admin(message.chat.id, message.from_user.id):
        user_id = message.reply_to_message.from_user.id
        permission = ChatPermissions(can_send_messages=True)
        await message.chat.restrict(user_id=user_id, permissions=permission)
        await message.answer(f"🔓 {message.reply_to_message.from_user.first_name} endi yozishingiz mumkin. 💬")
        await message.delete()  # Xabarni o'chirish, foydalanuvchilar ko'rmasligi uchun
    else:
        await message.answer("⛔ Sizda bu kommandani bajarish uchun huquq yo'q!")


# Xaqoratli so'zlarni bloklash
xaqoratli_sozlar = {"tentak", "ahmoq", "o'jar"}  # So'zlarni kengaytirish mumkin
@dp.message(and_f(F.chat.func(lambda chat: chat.type == "supergroup"), F.text))
async def tozalash(message: Message):
    text = message.text
    for soz in xaqoratli_sozlar:
        if soz in text.lower():
            user_id = message.from_user.id
            until_date = int(time.time()) + 60  # 5 daqiqaga mute qilinadi
            permission = ChatPermissions(can_send_messages=False)
            await message.chat.restrict(user_id=user_id, permissions=permission, until_date=until_date)
            await message.answer(f"⚠️ {message.from_user.mention_html()} guruhda haqoratli so'z ishlatganingiz uchun 1 daqiqaga bloklandingiz. 🚫")
            await message.delete()
            break


