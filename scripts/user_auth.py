import asyncio
from hiex_connector import AsyncHiEMagic

PRIVATE_KEY = '<ПРИВАТНИЙ КЛЮЧ>'
PUBLIC_KEY = '<ПУБЛІЧНИЙ КЛЮЧ>'


async def main():
    hiex = AsyncHiEMagic(PRIVATE_KEY, PUBLIC_KEY)

    email = input('Введи свою пошту ->')
    user_auth = await hiex.user_auth(email)

    while user_auth.allow is False and user_auth.code_attempt > 0:
        code = input('Введи код з листа ->')
        await user_auth.code(code)

    if user_auth.allow:
        user = await user_auth.user()
        print('Авторизація успішна')
        print(f'Твій auth_key: {user_auth.auth_key}')
        print(f'Твоя пошта: {user.email}')
        print(f'Твій ID: {user.user_id}')
    else:
        print('Сталася помилка авторизації')

if __name__ == "__main__":
    asyncio.run(main())
