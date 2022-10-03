import asyncio
from hiex_connector import AsyncHiExMagic

PRIVATE_KEY = '<ПРИВАТНИЙ КЛЮЧ>'
PUBLIC_KEY = '<ПУБЛІЧНИЙ КЛЮЧ>'


async def main():
    hiex = AsyncHiExMagic(PRIVATE_KEY, PUBLIC_KEY)

    email = input('Введи свою пошту ->')
    auth = await hiex.user_auth(email)

    while auth.allow is False and auth.code_attempt > 0:
        code = input('Введи код з листа ->')
        await auth.code(code)

    if auth.allow:
        user = await auth.user()
        print('Авторизація успішна')
        print(f'Твій auth_key: {auth.auth_key}')
        print(f'Твоя пошта: {user.email}')
        print(f'Твій ID: {user.user_id}')
    else:
        print('Сталася помилка авторизації')

if __name__ == "__main__":
    asyncio.run(main())
