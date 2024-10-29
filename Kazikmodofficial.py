# meta developer: @Berki_modul

from .. import loader, utils
import asyncio

@loader.tds
class KazikMod(loader.Module):
    """Модуль для фарма билетов и денежек в @seogift_bot(в боте нужно обязательно подписатся на каналы иначе не ворк)"""
    strings = {"name": "Biletfarm"}
    
    def __init__(self):
        self.running = False 

    async def biletoncmd(self, message):
        """Включить автоматическую отправку, чтобы получить билеты """
        if self.running:
            await message.edit("<b>❎Процесс уже запущен!</b>")
            return

        self.running = True
        await message.edit("<b>✅Автоматическая отправка, чтобы получить билеты запущена!</b>")

        while self.running:
            await message.client.send_message("@seogift_bot", "🎁 Получить бесплатные билеты [1 раз в сутки]")
            await asyncio.sleep(86400)
    async def biletoffcmd(self, message):
        """Отключить автоматическую отправку, чтобы получить билеты"""
        if not self.running:
            await message.edit("<b>❎Процесс не запущен!</b>")
            return

        self.running = False
        await message.edit("<b>❎Автоматическая отправка для получения билетов остановлена!</b>")