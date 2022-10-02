import asyncio
from hiex_connector import AsyncHiExMagic

PRIVATE_KEY = '<ПРИВАТНИЙ КЛЮЧ>'
PUBLIC_KEY = '<ПУБЛІЧНИЙ КЛЮЧ>'


async def main():
    hiex = AsyncHiExMagic(PRIVATE_KEY, PUBLIC_KEY)
    application = await hiex.application_details()
    print("{:<20} {}".format("Назва:", application.name))
    print("{:<20} {}".format("Баланс:", application.balance))
    print("{:<20} {}".format("%:", application.interest))
    print("{:<20} {}".format("URL для сповіщень:", application.notification_url))

if __name__ == "__main__":
    asyncio.run(main())
