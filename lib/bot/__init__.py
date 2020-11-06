from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed, File
from datetime import datetime
from discord.ext.commands import CommandNotFound
import time
from selenium import webdriver
import bs4 as bs
from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
import lib.bot.main as ipcheck

PREFIX = "+"
OWNER_IDS = [618038532665114624]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        

        super().__init__(command_prefix = PREFIX, owner_ids = OWNER_IDS)
    
    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("Running bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("BOT has been CONNECTED!")

    async def on_disconnect(self):
        print("BOT has been DISCONNECTED!")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Something went wrong!")
        
        else:
            channel = self.get_channel(757016278060761178)
            await channel.send("Dude your code freaking sucks, and error occured right here!")
        
        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass

        elif hasattr(exc, "original"):
            raise exc.original
            
        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(746850984701198437)
            print("BOT is ready!")

            channel = self.get_channel(757016278060761178)
            await channel.send("Now online!")

            embed = Embed(title="Now online!", url="https://www.github.com/woosal1337",
                          description="MadeInAZE is now online.",
                          colour=0xFF0000,
                          timestamp=datetime.utcnow())
            fields = [("Name", "Value", True),
                      ("Another field", "Next to the first one", True),
                      ("A non-inline field", "This field will appear on third row.", False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            embed.set_author(name="@woosal1337", icon_url=self.guild.icon_url)
            embed.set_footer(text="This is a footer xD?")
            embed.set_thumbnail(url=self.guild.icon_url)
            embed.set_image(url=self.guild.icon_url)
            #await channel.send(embed=embed)
            await channel.send("Started the Service.")
            await channel.send("Scraping ProtonMail")

            with open("lib/bot/warnings.txt", "r") as theWarningFile:
                firstLength = 0 #len(theWarningFile.read())


            while True:


                # with open("lib/bot/warnings.txt", "r") as theWarningFile:
                #     currentLength = len(theWarningFile.read())
                #     print(theWarningFile.read())
                #     print("current length is: ", currentLength)
                #     print("first length is ", firstLength)
                #     if currentLength != firstLength:
                #         f = open("lib/bot/warnings.txt", "r")
                #         lastLine = f.readlines()[-1]
                #         firstLength = currentLength
                #         time.sleep(0.5)
                #         await channel.send(lastLine)

            #await channel.send(file=File("./data/images/elon.gif"))

        else:
            print("BOT reconnected!")

    async def on_message(self, message):
        pass

bot = Bot()