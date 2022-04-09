import asyncio

from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch

import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from YukkiMusic import Telegram, YouTube, app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.plugins.play.playlist import del_plist_msg
from YukkiMusic.plugins.sudo.sudoers import sudoers_list
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from YukkiMusic.utils.decorators.language import LanguageStart
from YukkiMusic.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

loop = asyncio.get_running_loop()


@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.private
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def start_comm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_text(
                _["help_1"], reply_markup=keyboard
            )
        if name[0:4] == "song":
            return await message.reply_text(_["song_2"])
        if name[0:3] == "sta":
            m = await message.reply_text(
                "ðŸ¥± É¢á´‡á´›á´›ÉªÉ´É¢ Êá´á´œÊ€ á´©á´‡Ê€sá´É´á´€ÊŸ sá´›á´€á´›s Ò“Ê€á´á´ {config.MUSIC_BOT_NAME} sá´‡Ê€á´ á´‡Ê€."
            )
            stats = await get_userss(message.from_user.id)
            tot = len(stats)
            if not stats:
                await asyncio.sleep(1)
                return await m.edit(_["ustats_1"])

            def get_stats():
                msg = ""
                limit = 0
                results = {}
                for i in stats:
                    top_list = stats[i]["spot"]
                    results[str(i)] = top_list
                    list_arranged = dict(
                        sorted(
                            results.items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    )
                if not results:
                    return m.edit(_["ustats_1"])
                tota = 0
                videoid = None
                for vidid, count in list_arranged.items():
                    tota += count
                    if limit == 10:
                        continue
                    if limit == 0:
                        videoid = vidid
                    limit += 1
                    details = stats.get(vidid)
                    title = (details["title"][:35]).title()
                    if vidid == "telegram":
                        msg += f"ðŸ”—[á´›á´‡ÊŸá´‡É¢Ê€á´€á´ á´á´‡á´…Éªá´€](https://t.me/DevilsHeavenMF) ** á´©ÊŸá´€Êá´‡á´… {count} á´›Éªá´á´‡s**\n\n"
                    else:
                        msg += f"ðŸ”— [{title}](https://www.youtube.com/watch?v={vidid}) ** played {count} times**\n\n"
                msg = _["ustats_2"].format(tot, tota, limit) + msg
                return videoid, msg

            try:
                videoid, msg = await loop.run_in_executor(
                    None, get_stats
                )
            except Exception as e:
                print(e)
                return
            thumbnail = await YouTube.thumbnail(videoid, True)
            await m.delete()
            await message.reply_photo(photo=thumbnail, caption=msg)
            return
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} á´Šá´œsá´› sá´›á´€Ê€á´›á´‡á´… á´›Êœá´‡ Ê™á´á´› á´›á´ á´„Êœá´‡á´„á´‹ <code>sá´œá´…á´ÊŸÉªsá´›</code>\n\n**á´œsá´‡Ê€ Éªá´…:** {sender_id}\n**á´œsá´‡Ê€É´á´€á´á´‡:** {sender_name}",
                )
            return
        if name[0:3] == "lyr":
            query = (str(name)).replace("lyrics_", "", 1)
            lyrical = config.lyrical
            lyrics = lyrical.get(query)
            if lyrics:
                return await Telegram.send_split_text(message, lyrics)
            else:
                return await message.reply_text(
                    "Ò“á´€ÉªÊŸá´‡á´… á´›á´ É¢á´‡á´› ÊŸÊÊ€Éªá´„s."
                )
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
        if name[0:3] == "inf":
            m = await message.reply_text("ðŸ”Ž")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[
                    0
                ]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
ðŸ˜²**á´›Ê€á´€á´„á´‹ ÉªÉ´Ò“á´Ê€É´á´€á´›Éªá´É´**ðŸ˜²

ðŸ“Œ**á´›Éªá´›ÊŸá´‡:** {title}

â³**á´…á´œÊ€á´€á´›Éªá´É´:** {duration} á´ÉªÉ´á´œá´›á´‡s
ðŸ‘€**á´ Éªá´‡á´¡s:** `{views}`
â°**á´©á´œÊ™ÊŸÉªsÊœá´‡á´… á´É´:** {published}
ðŸŽ¥**á´„Êœá´€É´É´á´‡ÊŸ:** {channel}
ðŸ“Ž**á´„Êœá´€É´É´á´‡ÊŸ ÊŸÉªÉ´á´‹:** [á´ ÉªsÉªá´› á´„Êœá´€É´É´á´‡ÊŸ]({channellink})
ðŸ”—**ÊŸÉªÉ´á´‹:** [á´¡á´€á´›á´„Êœ á´É´ Êá´á´œá´›á´œÊ™á´‡]({link})

ðŸ’– sá´‡á´€Ê€á´„Êœ á´©á´á´¡á´‡Ê€á´‡á´… Ê™Ê {config.MUSIC_BOT_NAME}"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="â€¢ Êá´á´œá´›á´œÊ™á´‡ â€¢", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="â€¢ á´„ÊŸá´sá´‡ â€¢", callback_data="close"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} á´Šá´œsá´› sá´›á´€Ê€á´›á´‡á´… Ê™á´á´› á´›á´ á´„Êœá´‡á´„á´‹ <code>á´›Ê€á´€á´„á´‹ ÉªÉ´Ò“á´Ê€á´á´€á´›Éªá´É´</code>\n\n**á´œsá´‡Ê€ Éªá´…:** {sender_id}\n**á´œsá´‡Ê€É´á´€á´á´‡:** {sender_name}",
                )
    else:
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = None
        out = private_panel(_, app.username, OWNER)
        if config.START_IMG_URL:
            try:
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_2"].format(
                        config.MUSIC_BOT_NAME
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            except:
                await message.reply_text(
                    _["start_2"].format(config.MUSIC_BOT_NAME),
                    reply_markup=InlineKeyboardMarkup(out),
                )
        else:
            await message.reply_text(
                _["start_2"].format(config.MUSIC_BOT_NAME),
                reply_markup=InlineKeyboardMarkup(out),
            )
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.first_name
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} á´Šá´œsá´› sá´›á´€Ê€á´›á´‡á´… Êá´á´œÊ€ Ê™á´á´›.\n\n**á´œsá´‡Ê€ Éªá´…:** {sender_id}\n**á´œsá´‡Ê€É´á´€á´á´‡:** {sender_name}",
            )


@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def testbot(client, message: Message, _):
    out = start_pannel(_)
    return await message.reply_text(
        _["start_1"].format(
            message.chat.title, config.MUSIC_BOT_NAME
        ),
        reply_markup=InlineKeyboardMarkup(out),
    )


welcome_group = 2


@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "**á´©Ê€Éªá´ á´€á´›á´‡ á´á´œsÉªá´„ Ê™á´á´›**\n\ná´É´ÊŸÊ Ò“á´Ê€ á´›Êœá´‡ á´„Êœá´€á´›s á´€á´œá´›Êœá´Ê€Éªsá´‡á´… Ê™Ê á´Ê á´á´¡É´á´‡Ê€, Ê€á´‡Ç«á´œá´‡sá´› ÉªÉ´ á´Ê á´á´¡É´á´‡Ê€'s á´©á´ á´›á´ á´€á´œá´›Êœá´Ê€Éªsá´‡ Êá´á´œÊ€ á´„Êœá´€á´› á´€É´á´… ÉªÒ“ Êá´á´œ á´…á´É´'á´› á´¡á´€É´á´› á´›á´ á´…á´ sá´ á´›Êœá´‡É´ Ò“á´œ*á´‹ á´Ò“Ò“ Ê™á´‡á´„á´€á´œsá´‡ Éª'á´ ÊŸá´‡á´€á´ ÉªÉ´É¢."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != "supergroup":
                    await message.reply_text(_["start_6"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_7"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                out = start_pannel(_)
                await message.reply_text(
                    _["start_3"].format(
                        config.MUSIC_BOT_NAME,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in config.OWNER_ID:
                return await message.reply_text(
                    _["start_4"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_5"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            return
        except:
            return
