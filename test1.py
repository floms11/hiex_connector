from hiex_connector import *

PRIVATE_KEY = 'B4d6B8beUF479d8Ejbcz48ryGN8L5GdSK9E6JkjA5z5m9r63E766xaCAErmuKb4CrD6cEB2M5cr86rJSiGRP5pybg87sY589fa766jiLkEV37HY98iz93Rc5eDAYR5au'
PUBLIC_KEY = 'B6kgY7EKS92Gpy6K5a5s6675dpMjcFfLiEve9E59tKFHRka9Hz4s9P237f77utUDu4gf4j3jUe4PB5jMU8f28RnUP4PyE63r2H67hKk86Lhf88EYrKBYnAr349vnaL8i'

hiex = HiExConnector(PRIVATE_KEY, PUBLIC_KEY)

logs = hiex.admin_logs_list()
for log in logs:
    print(hiex.admin_logs_get(log.name))
