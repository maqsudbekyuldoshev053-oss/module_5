from redis_dict import RedisDict
d = RedisDict()
d['name'] = 42
print(d['k1'])

from redis import Redis
from redis_dict import RedisDict
d = RedisDict(redis=Redis(host='10.30.4.7'))
d['maqsud'] = '1234'
print(d)


import psycopg2

conn = psycopg2.connect("dbname='dvdrental' user='postgres' host='localhost' password='1'")

cur = conn.cursor()
query = "select * from actor limit 5"
cur.execute(query)

actors = cur.fetchall()
for i in actors:
    print(i)

curr = conn.cursor()

def get_actors(c):
    curr.execute("select * from actor")
    return curr.fetchall()

for i in get_actors(curr):
    print(i)


curr = conn.cursor()

def get_actors(c):
    curr.execute("select * from actor")
    # print(c.description)
    for i in c.description:
        print(i[0])
    return curr.fetchall()

get_actors(curr)



def get_actors(c):
   cur.execute("select * from actor ORDER BY actor_id")
   return cur.fetchall()

def update_actor(c, actor_id, first_name, last_name):
    cur.execute("UPDATE actor SET first_name = %s WHERE actor_id = %s;",())
    conn.commit()

def delete_actor(c, actor_id):
    cur.execute("DELETE FROM actor WHERE actor_id = %s;",(actor_id,))
    conn.commit()

def insert_actor(c, first_name, last_name):
    cur.execute("INSERT INTO actor(first_name, last_name) VALUES(%s, %s);",(first_name, last_name))
    conn.commit()

cur = conn.cursor()
actors = get_actors(cur)
for i in actors:
    print(i)
delete_actor(cur,201)
insert_actor(cur, "Tolib", "Botirov")


conn.autocommit = True

cur = conn.cursor()
year = 2005

query = """
        select f.title, f.release_year, count(a.actor_id)
        from film f
                 join film_actor fa on f.film_id = fa.film_id
                 join actor a on fa.actor_id = a.actor_id
        where f.release_year >= %s
        group by f.title,  f.release_year;
        """
cur.execute(query, (year,))

actors = cur.fetchall()
for actor in actors:
    print(actor)


curr = conn.cursor()

print(get_actor(cur, 201))
insert_actor(cur, 'Shavkat', 'Botirov')
delete_actor(cur, 201)
actors = get_actors(cur)
for actor in actors:
    print(*actor)

