import asyncio
from hiex_connector import AsyncHiExConnector

PRIVATE_KEY = '<ПРИВАТНИЙ КЛЮЧ>'
PUBLIC_KEY = '<ПУБЛІЧНИЙ КЛЮЧ>'


async def main():
    hiex = AsyncHiExConnector(PRIVATE_KEY, PUBLIC_KEY)

    email = input('Введи свою пошту ->')
    user_auth = await hiex.user_auth(email)

    while user_auth.allow is False and user_auth.code_attempt > 0:
        code = input('Введи код з листа ->')
        user_auth = await hiex.user_auth_code(user_auth.auth_key, code)

    if user_auth.allow:
        print('Авторизація успішна')
        print(f'Твій auth_key: {user_auth.auth_key}')
    else:
        print('Сталася помилка авторизації')

if __name__ == "__main__":
    asyncio.run(main())
