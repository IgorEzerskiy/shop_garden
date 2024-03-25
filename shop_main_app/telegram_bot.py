import requests


class InfoBot:
    __instance = None

    def __init__(self, api_token: str, chanel_id: str):
        self.__API_TOKEN = api_token
        self.__CHANEL_ID = chanel_id

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(InfoBot, cls).__new__(cls)

        return cls.__instance

    async def __send_message(self, msg):
        url = f"https://api.telegram.org/bot{self.__API_TOKEN}/sendMessage?chat_id={self.__CHANEL_ID}&text={msg}"
        requests.post(url=url)

    async def send_message_that_order_created(self, report_info: dict = None):
        msg = f"""💵💵💵Привіт!\nУ вас нове замовлення №{report_info.get('order_id')}.\n
---Інфо про покупця---\n
І'мя та прізвище: {report_info.get('buyer_f_l_name')};\n
Пошта: {report_info.get('buyer_email')};\n
Номер телефону: {report_info.get('buyer_phone')};\n
Місто відправки: {report_info.get('buyer_delivery_city')};\n
Відділення НП: {report_info.get('buyer_delivery_warehouse')};\n
----\n
Сума: {report_info.get('order_price')} грн."""

        await self.__send_message(msg=msg)

    async def send_message_when_the_product_is_out_of_stock(self, product_info: dict):
        msg = f"""❗️❗️❗️ Товар {product_info.get('product_name')} скінчився.\n
Посилання:
http://127.0.0.1:8000/product/{product_info.get('product_slug')}/"""

        await self.__send_message(msg=msg)
