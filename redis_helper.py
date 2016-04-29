import settings, redis

r = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB
)

def get_lists():
    lists = []
    for key in r.keys():
        if r.type(key) == 'list':
            lists.append(key)
    return lists

def get_list_items(list):
    return r.lrange(list, 0, -1)

def get_all_lists_with_items():
    all_lists_with_items = []
    for key in get_lists():
        list_items = get_list_items(key)
        all_lists_with_items.append(
            {
                'name': key,
                'messages': list_items
            }
        )
    return all_lists_with_items

def delete_message_from_list(list, message):
    print "Deleting message '{}' from '{}'".format(message, list)
    r.lrem(list, 0, message)

def lpush_message(list, message):
    print "lpush-ing message '{}' to '{}'".format(message, list)
    r.lpush(list, message)

def rpush_message(list, message):
    print "r-pushing message '{}' to '{}'".format(message, list)
    r.lrem(list, message)
