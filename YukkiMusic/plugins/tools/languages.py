from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, Message

from config import BANNED_USERS
from strings import get_command, get_string
from YukkiMusic import app
from YukkiMusic.utils.database import get_lang, set_lang
from YukkiMusic.utils.decorators import (ActualAdminCB, language,
                                         languageCB)

# Languages Available


def lanuages_keyboard(_):
    keyboard = InlineKeyboard(row_width=2)
    keyboard.row(
        InlineKeyboardButton(
            text="馃嚘馃嚭 岽嚿瓷⑹熒猻蕼 馃嚘馃嚭",
            callback_data=f"languages:en",
        ),
        InlineKeyboardButton(
            text="馃嚠馃嚦 啶灌た啶ㄠ啶︵ 馃嚠馃嚦",
            callback_data=f"languages:hi",
        ),
    )
    keyboard.row(
        InlineKeyboardButton(
            text="馃嚤馃嚢 喾冟窉喽傕穭喽� 馃嚤馃嚢",
            callback_data=f"languages:si",
        ),
        InlineKeyboardButton(
            text="馃嚘馃嚳 Az蓹rbaycan 馃嚘馃嚳",
            callback_data=f"languages:az",
        ),
    )
    keyboard.row(
        InlineKeyboardButton(
            text="馃嚠馃嚦 嗒椸珌嗒溹嗒距喃� 馃嚠馃嚦",
            callback_data=f"languages:gu",
        ),
        InlineKeyboardButton(
            text="馃嚬馃嚪 T眉rkiye T眉rk莽esi 馃嚬馃嚪",
            callback_data=f"languages:tr",
        ),
    )
    keyboard.row(
        InlineKeyboardButton(
            text="馃悤 岽勈溼磭岽囜磵s 馃悤",
            callback_data=f"languages:cheems",
        ),
    )
    keyboard.row(
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSE_BUTTON"], callback_data=f"close"
        ),
    )
    return keyboard


LANGUAGE_COMMAND = get_command("LANGUAGE_COMMAND")


@app.on_message(
    filters.command(LANGUAGE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def langs_command(client, message: Message, _):
    keyboard = lanuages_keyboard(_)
    await message.reply_text(
        _["setting_1"].format(message.chat.title, message.chat.id),
        reply_markup=keyboard,
    )


@app.on_callback_query(filters.regex("LG") & ~BANNED_USERS)
@languageCB
async def lanuagecb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(
        reply_markup=keyboard
    )


@app.on_callback_query(
    filters.regex(r"languages:(.*?)") & ~BANNED_USERS
)
@ActualAdminCB
async def language_markup(client, CallbackQuery, _):
    langauge = (CallbackQuery.data).split(":")[1]
    old = await get_lang(CallbackQuery.message.chat.id)
    if str(old) == str(langauge):
        return await CallbackQuery.answer(
            "蕪岽忈礈'蕗岽� 岽�薀蕗岽囜磤岽吺� 岽渟瑟纱散 s岽�岽嶀磭 薀岽�纱散岽溼磤散岽� 覔岽徥� 岽浭溕猻 岽勈溼磤岽�.", show_alert=True
        )
    try:
        _ = get_string(langauge)
        await CallbackQuery.answer(
            "s岽溼磩岽勧磭ss覔岽準熓熓� 岽勈溼磤纱散岽囜磪 蕪岽忈礈蕗 薀岽�纱散岽溼磤散岽�.", show_alert=True
        )
    except:
        return await CallbackQuery.answer(
            "覔岽�瑟薀岽囜磪 岽涐磸 岽勈溼磤纱散岽� 薀岽�纱散岽溼磤散岽� 岽徥� 岽浭溼磭 薀岽�纱散岽溼磤散岽� 瑟s 岽溕瘁磪岽囀� 岽嶀磤瑟纱岽涐磭纱岽�纱岽勧磭.",
            show_alert=True,
        )
    await set_lang(CallbackQuery.message.chat.id, langauge)
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(
        reply_markup=keyboard
    )
