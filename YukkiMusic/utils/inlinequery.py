from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="ðŸ™„ á´©á´€á´œsá´‡ ðŸ™„",
            description=f"á´©á´€á´œsá´‡ á´›Êœá´‡ á´„á´œÊ€Ê€á´‡É´á´› á´©ÊŸá´€ÊÉªÉ´É¢ sá´›Ê€á´‡á´€á´ á´É´ á´ Éªá´…á´‡á´á´„Êœá´€á´›.",
            thumb_url="https://telegra.ph/file/701028ce085ecfa961a36.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="ðŸ˜‹ Ê€á´‡sá´œá´á´‡ ðŸ˜‹",
            description=f"Ê€á´‡sá´œá´á´‡ á´›Êœá´‡ á´©á´€á´œsá´‡á´… sá´›Ê€á´‡á´€á´ á´É´ á´ Éªá´…á´‡á´á´„Êœá´€á´›.",
            thumb_url="https://telegra.ph/file/701028ce085ecfa961a36.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="ðŸ˜ á´á´œá´›á´‡ ðŸ˜",
            description=f"á´á´œá´›á´‡ á´›Êœá´‡ á´„á´œÊ€Ê€á´‡É´á´› á´©ÊŸá´€ÊÉªÉ´É¢ sá´›Ê€á´‡á´€á´ á´É´ á´ Éªá´…á´‡á´á´„Êœá´€á´›.",
            thumb_url="https://telegra.ph/file/701028ce085ecfa961a36.jpg",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="ðŸ˜ á´œÉ´á´á´œá´›á´‡ ðŸ˜",
            description=f"á´œÉ´á´á´œá´›á´‡ á´›Êœá´‡ á´á´œá´›á´‡á´… sá´›Ê€á´‡á´€á´ á´É´ á´ Éªá´…á´‡á´á´„Êœá´€á´›.",
            thumb_url="https://telegra.ph/file/701028ce085ecfa961a36.jpg",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
        InlineQueryResultArticle(
            title="ðŸ™‚ sá´‹Éªá´© ðŸ™‚",
            description=f"sá´‹Éªá´© á´›Êœá´‡ á´„á´œÊ€Ê€á´‡É´á´› á´©ÊŸá´€ÊÉªÉ´É¢ sá´›Ê€á´‡á´€á´ á´É´ á´ Éªá´…á´‡á´á´„Êœá´€á´› á´€É´á´… á´á´á´ á´‡s á´›á´ á´›Êœá´‡ É´á´‡xá´› sá´›Ê€á´‡á´€á´.",
            thumb_url="https://telegra.ph/file/701028ce085ecfa961a36.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="ðŸ¥º á´‡É´á´… ðŸ¥º",
            description="á´‡É´á´… á´›Êœá´‡ á´„á´œÊ€Ê€á´‡É´á´› á´©ÊŸá´€ÊÉªÉ´É¢ sá´›Ê€á´‡á´€á´ á´É´ á´ Éªá´…á´‡á´á´„Êœá´€á´›.",
            thumb_url="https://telegra.ph/file/701028ce085ecfa961a36.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="ðŸ¥´ sÊœá´œÒ“Ò“ÊŸá´‡ ðŸ¥´",
            description="sÊœá´œÒ“Ò“ÊŸá´‡ á´›Êœá´‡ Ç«á´œá´‡á´œá´‡á´… sá´É´É¢s ÉªÉ´ á´©ÊŸá´€ÊÊŸÉªsá´›.",
            thumb_url="https://telegra.ph/file/701028ce085ecfa961a36.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="ðŸ˜´ sá´‡á´‡á´‹ ðŸ˜´",
            description="sá´‡á´‡á´‹ á´›Êœá´‡ á´©ÊŸá´€ÊÉªÉ´É¢ sá´›Ê€á´‡á´€á´ á´›á´ á´›Êœá´‡ É¢Éªá´ á´‡É´ á´…á´œÊ€á´€á´›Éªá´É´.",
            thumb_url="https://telegra.ph/file/701028ce085ecfa961a36.jpg",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="ðŸ¥± ÊŸá´á´á´© ðŸ¥±",
            description="ÊŸá´á´á´© á´›Êœá´‡ á´„á´œÊ€Ê€á´‡É´á´› á´©ÊŸá´€ÊÉªÉ´É¢ á´›Ê€á´€á´„á´‹ á´É´ á´ Éªá´…á´‡á´á´„Êœá´€á´›.",
            thumb_url="https://telegra.ph/file/701028ce085ecfa961a36.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
