Конектор для hiex.io
===
### Ця бібліотека служить для спрощення взаємодії з api.hiex.io

## Подивитися документацію з усіма доступними методами можна [тут](https://docs.hiex.io)

В бібліотеці розроблено асинхронний та синхронний (тимчасово недоступний) методи взаємодії

## Для початку взаємодії потрібно встановити бібліотеку через `pip`:

* Завантаж архів з https://git.floms.cc/hiex/connector/-/archive/partner/connector-partner.zip
* Встанови бібліотеку: `pip3 install connector-partner.zip`

Далі можна використовувати біблітеоку в точності, як описано в [https://docs.hiex.io](тут), або використовувати "магічний конектор"

## Розглянемо базовий метод

Імпортуємо конектор
`
from hiex_connector import AsyncHiExConnector
`

Створемо екземпляр 
`
hiex = AsyncHiExConnector('<PRIVATE_KEY>', '<PUBLIC_KEY>'')
`
 (ключі потрібно отримати у підтримки hiex.io)

Далі всі [запити](https://docs.hiex.io) здійснюються за прикладом: 
`
exchange = await hiex.exchange_details('<AUTH_KEY>', <EXCHANGE_ID>)
` (<AUTH_KEY> – отримується при авторизації, <EXCHANGE_ID> – при створені обміну)

`exchange` – це об'єкт типу Exchange. Всі типи описані на на сторінці: https://docs.hiex.io/types/

## Розглянемо метод з "магічним конектором"

Імпортуємо конектор
`
from hiex_connector import AsyncHiExMagic
`

Створемо екземпляр 
`
hiex = AsyncHiExMagic('<PRIVATE_KEY>', '<PUBLIC_KEY>'')
`

Всі [запити](https://docs.hiex.io) здійснюються за прикладом: 
`
exchange = await hiex.exchange_details('<AUTH_KEY>', <EXCHANGE_ID>)
`

#### І тепер найцікавіше. 

#### З типом `exchange` (та іншими) можна взаємодіяти. Наведу кілька прикладів:

* Щоб оновити інформацію про обмін, достатньо виконати: `await exchange.reload()`
* Щоб підтвердити обмін, достатньо виконати: `await exchange.confirm()`
* Щоб відмініти обмін, достатньо виконати: `await exchange.cancel()`
* Щоб завантажити користувача який виконав обмін, достатньо виконати: `user = await exchange.user()`
* Щоб завантажити історію обмінів, достатньо виконати: `exchanges = await user.exchanges()`

### Далі буде. Це все в розробці...