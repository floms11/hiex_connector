from hiex_connector import *

PRIVATE_KEY = 'B4d6B8beUF479d8Ejbcz48ryGN8L5GdSK9E6JkjA5z5m9r63E766xaCAErmuKb4CrD6cEB2M5cr86rJSiGRP5pybg87sY589fa766jiLkEV37HY98iz93Rc5eDAYR5au'
PUBLIC_KEY = 'B6kgY7EKS92Gpy6K5a5s6675dpMjcFfLiEve9E59tKFHRka9Hz4s9P237f77utUDu4gf4j3jUe4PB5jMU8f28RnUP4PyE63r2H67hKk86Lhf88EYrKBYnAr349vnaL8i'

hiex = HiExConnector(PRIVATE_KEY, PUBLIC_KEY)

print(hiex.admin_coins_list())

logs = hiex.admin_logs_list()
for log in logs:
    print(f"Логи завантажено, {len(hiex.admin_logs_get(log.name))} байт")

print(hiex.admin_exchange_update(exchange_id=1))
print(hiex.admin_exchanges_list(application_id=1))
print(hiex.admin_stats_get(application_id=1))
print(hiex.admin_applications_list())
app = hiex.admin_application_create('Test', ['user_auth', 'user_get'], 1)
print(app)
print(hiex.admin_application_update(application_id=app.application_id, balance=100))
print(hiex.admin_application_details(application_id=app.application_id))
print(hiex.admin_application_delete(application_id=app.application_id))
print(hiex.admin_pairs_list())
print(hiex.admin_pair_create(currency1='USDT_TRC20', currency2='BTC', comment='Test', kyc_required=False, swap_deposit=True))
print(hiex.admin_pair_update(currency1='USDT_TRC20', currency2='BTC', swap_deposit=False))
print(hiex.admin_pair_delete(currency1='USDT_TRC20', currency2='BTC'))
print(hiex.admin_pairs_list())
print(hiex.admin_user_details(email='jeka.floms@gmail.com'))
