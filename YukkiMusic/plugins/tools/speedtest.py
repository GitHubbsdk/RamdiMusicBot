import asyncio
import os

import speedtest
import wget
from pyrogram import filters

from strings import get_command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("馃檮 岽勈溼磭岽勧磱瑟纱散 岽呩磸岽∩词熱磸岽�岽� s岽┽磭岽囜磪...")
        test.download()
        m = m.edit("馃檮 岽勈溼磭岽勧磱瑟纱散 岽溼穿薀岽忈磤岽� s岽┽磭岽囜磪...")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("馃槾 岽溼穿薀岽忈磤岽吷瓷� s岽┽磭岽囜磪岽涐磭s岽� 蕗岽噑岽準熱礇s...")
        path = wget.download(result["share"])
    except Exception as e:
        return m.edit(e)
    return result, path


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("馃挮 岽浭�蕪瑟纱散 岽涐磸 岽勈溼磭岽勧磱 岽溼穿薀岽忈磤岽� 岽�纱岽� 岽呩磸岽∩词熱磸岽�岽� s岽┽磭岽囜磪...")
    loop = asyncio.get_event_loop()
    result, path = await loop.run_in_executor(None, testspeed, m)
    output = f"""**s岽┽磭岽囜磪岽涐磭s岽� 蕗岽噑岽準熱礇s**
    
<u>**岽勈熒磭纱岽�:**</u>
**__瑟s岽�:__** {result['client']['isp']}
**__岽勧磸岽溕瘁礇蕗蕪:__** {result['client']['country']}
  
<u>**s岽囀�岽犪磭蕗:**</u>
**__纱岽�岽嶀磭:__** {result['server']['name']}
**__岽勧磸岽溕瘁礇蕗蕪:__** {result['server']['country']}, {result['server']['cc']}
**__s岽┽磸纱s岽徥�:__** {result['server']['sponsor']}
**__薀岽�岽涐磭纱岽勈�:__** {result['server']['latency']}  
**__岽┥瓷�:__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=path, caption=output
    )
    os.remove(path)
    await m.delete()
