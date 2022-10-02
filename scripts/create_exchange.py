import asyncio
from hiex_connector.magic_async_connector import AsyncHiExMagic

PRIVATE_KEY = '<ПРИВАТНИЙ КЛЮЧ>'
PUBLIC_KEY = '<ПУБЛІЧНИЙ КЛЮЧ>'

USER_AUTH_KEY = '<КЛЮЧ КОРИСТУВАЧА>'


async def main():
    hiex = AsyncHiExMagic(PRIVATE_KEY, PUBLIC_KEY)

    pairs = await hiex.pairs_list(currency1='USDT_TRC20', currency2='UAH_VISAMASTER')
    pair = pairs[0]

    user = await hiex.user_get(USER_AUTH_KEY)
    exchange = await user.exchange_create(pair, '<КАРТКА НА ЯКУ ОТРИМУЄМО КОШТИ>', amount1=10)
    await exchange.confirm()

    while True:
        print(exchange)
        await exchange.reload()
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
