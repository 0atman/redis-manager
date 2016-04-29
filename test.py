import settings, redis

r = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB
)

messages = []
for i in range(5):
    messages.append({"retries": 0, "announce_type": "created", "wait_until": "2016-04-26T11:44:14.044327", "only_for": ["trello"], "source": "hurdle", "type": "locumdocument", "id": i})


for x in messages:
    r.lpush('q:hurdle', x)
