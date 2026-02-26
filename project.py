import psycopg2

conn = psycopg2.connect("dbname='dvdrental' user='postgres' host='localhost' password='1' port='5432'")
curr = conn.cursor()

curr.execute("""
             CREATE TABLE IF NOT EXISTS mahsulot
             (
                 id    SERIAL PRIMARY KEY,
                 nomi  VARCHAR(255) NOT NULL,
                 narxi INTEGER      NOT NULL
             )""")

conn.commit()


def product_add():
    name = input("Mahsulot nomi: ")
    price = float(input("Narxi: "))

    curr.execute(
        "INSERT INTO mahsulot (nomi, narxi) VALUES (%s, %s)",
        (name, price)
    )
    conn.commit()
    print("Mahsulot qo‘shildi")


def product_view():
    curr.execute("""SELECT *
                    FROM mahsulot""")
    rows = curr.fetchall()

    if not rows:
        print('No products added')
    else:
        for i in rows:
            print(i)


def product_update():
    id = int(input("ID: "))
    new_price = float(input("Yangi narx: "))
    curr.execute("""UPDATE mahsulot
                    SET name  = %s,
                        price = %s
                    WHERE id = %s;
                 """, (new_price, id))
    conn.commit()
    print('Product updated')


def product_del():
    id = int(input("ID: "))
    curr.execute("DELETE FROM mahsulot WHERE id = %s;", (id,))
    conn.commit()
    print('Product deleted')


while True:
    print("""
1. Mahsulot qo‘shish
2. Mahsulotlarni ko‘rish
3. Mahsulotni o‘zgartirish
4. Mahsulotni o‘chirish
0. Chiqish
""")
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        product_add()
    elif tanlov == "2":
        product_view()
    elif tanlov == "3":
        product_update()
    elif tanlov == "4":
        product_del()
    elif tanlov == "0":
        print("Dastur tugadi")
        break
    else:
        print("Noto‘g‘ri tanlov")

curr.close()
conn.close()
