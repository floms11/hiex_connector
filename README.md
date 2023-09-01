Конектор для hiex.io
===
### Ця бібліотека служить для спрощення взаємодії з api.hiex.io

## Подивитися документацію з усіма доступними методами можна [тут](https://docs.hiex.io)

В бібліотеці розроблено асинхронний та синхронний (тимчасово недоступний) методи взаємодії

## Для початку взаємодії потрібно встановити бібліотеку:

* для `mac/linux`: `pip3 install https://github.com/floms11/hiex_connector/archive/refs/heads/partner.zip`;
* для `windows`: `pip install https://github.com/floms11/hiex_connector/archive/refs/heads/partner.zip`.

## До коду!

### Імпортуємо конектор

`
from hiex_connector import HiExConnector
`

_Або асинхронний варіант:_

`
from hiex_connector import AsyncHiExConnector
`

### Створюємо екземпляр

`
hiex = HiExConnector('<PRIVATE_KEY>', '<PUBLIC_KEY>'')
`

_Або асинхронний варіант:_

`
hiex = AsyncHiExConnector('<PRIVATE_KEY>', '<PUBLIC_KEY>'')
`


**Ключі потрібно отримати у [підтримки](https://t.me/hiexio) hiex.io**

### Далі всі [запити](https://docs.hiex.io) виконуються за прикладом: 

`
pairs = hiex.exchange_pairs_list()
`

_Або асинхронний варіант:_

`
pairs = await hiex.exchange_pairs_list()
`

## Контекст

### З типами можна взаємодіяти в їх контексті. Деякі приклади:

* Щоб оновити інформацію про обмін, достатньо виконати: `await exchange.reload()`
* Щоб отримати реквізити обміну, достатньо виконати: `await exchange.payment()`
* Щоб відмінити обмін, достатньо виконати: `await exchange.cancel()`
* Щоб завантажити користувача який виконав обмін, достатньо виконати: `user = await exchange.user()`
* Щоб завантажити історію обмінів, достатньо виконати: `exchanges = await user.exchanges()`

Для перегляду детальнішої інформації про контекст в типах див. вихідний код

## Сповіщення (webhooks)

У бібліотеці розроблений функціонал для обробки сповіщень від **hiex.io**.

Перед реалізацією рекомендую почитати [документацію](https://docs.hiex.io/webhooks/) про сповіщення

### Інструкція
#### Створюємо обробники
Імпоруємо `from hiex_connector import AsyncHiExExchangeUpdate, AsyncHiExUserKYCReviewed`.

Це базові обробники на основі яких ми створимо власні.

Для створення обробника потрібно створити клас який буде наслідувати базовий, 
та мати асинхронний метод `handle`.

#### Приклад з `AsyncHiExExchangeUpdate`:
```python
from hiex_connector import AsyncHiExExchangeUpdate


class ExchangeUpdate(AsyncHiExExchangeUpdate):
    async def handle(self):
        print(self.exchange)
        return True
```
`AsyncHiExExchangeUpdate` – це обробник, який виконується при зміні інформації про обмін.

`AsyncHiExUserKYCReviewed` – це обробник, який виконується при проходженні `KYC` користувачем.

#### В залежності від обробника, ти можеш отримати доступ до інформації, яка була передана в сповіщення:

* для `AsyncHiExExchangeUpdate` – `self.exchange`
* для `AsyncHiExUserKYCReviewed` – `self.user`

#### Реєструємо обробники
Бібліотека надає функціонал створення `web-серверу` та реєстрації обробників в "два кліки"

Для реєстрації обробників достатньо імпортувати `from hiex_connector import AsyncHiExNotifications` та оголосити `AsyncHiExNotifications`.

#### Приклад з `ExchangeUpdate` (налаштували вище):
```python
from hiex_connector import AsyncHiExNotifications


if __name__ == '__main__':
    AsyncHiExNotifications(
        connector=connector_hiex,
        host='0.0.0.0',
        port=8080,
        url='/bot/notifications/',
        handlers=[ExchangeUpdate],
    )
```

У `AsyncHiExNotifications` є два обов'язкових параметри:
* `connector` – конектор типу `AsyncHiExConnector`
* `handlers` – список обробників подій

#### На цьому все. Для роботи з `webhooks` потрібно тільки створити та зареєструвати обробники


### Далі буде. Це все в розробці...