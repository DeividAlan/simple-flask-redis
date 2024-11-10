""" Test """

import redis

redis_coon = redis.Redis(host="localhost", port=6379, db=0)

redis_coon.set("key_1", "change value")

my_value = redis_coon.get("key_1").decode("utf-8")
print(my_value)

my_value = redis_coon.delete("key_1")


### comandos para hash
my_hash = {"nome": "joao", "age": 30, "city": "caruaru"}

redis_coon.hset("my_hash", "nome", "joao")
redis_coon.hset("my_hash", "age", "30")
redis_coon.hset("my_hash", "city", "caruaru")
