# meta developer: @Berki_modul

from .. import loader, utils
import asyncio

@loader.tds
class KazikMod(loader.Module):
    """Модуль для фарма денежек в боте казикофф"""
    strings = {"name": "Kazikfarmmod"}
    
    def __init__(self):
        self.running = False 

    async def kazikoncmd(self, message):
        """Включить автоматическую отправку 🎰 Крутить 🎰 """
        if self.running:
            await message.edit("<b>❎Процесс уже запущен!</b>")
            return

        self.running = True
        await message.edit("<b>✅Автоматическая отправка 🎰 Крутить 🎰 запущена!</b>")

        while self.running:
            await message.client.send_message("@KazikoffSpinBot", "🎰 Крутить 🎰 ")
            await asyncio.sleep(3600)
    async def kazikoffcmd(self, message):
        """Отключить автоматическую отправку /🎰 Крутить 🎰 """
        if not self.running:
            await message.edit("<b>❎Процесс не запущен!</b>")
            return

        self.running = False
        await message.edit("<b>❎Автоматическая отправка 🎰 Крутить 🎰 остановлена!</b>")