import sqlite3


def create_table():
    # Подлючаемся к бдхе
    conn = sqlite3.connect("game_bot.db")
    # Создать курсор
    cur = conn.cursor()

    # Выполняем какую-то команду
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    knb_win INTEGER,
                    knb_games INTEGER
    )""")

    # Сохранить если было изменение
    conn.commit()
    # Подключение закрыть
    conn.close()


def create_user(id, name):
    # Подлючаемся к бдхе
    conn = sqlite3.connect("game_bot.db")
    # Создать курсор
    cur = conn.cursor()
    cur.execute(f"SELECT id FROM users WHERE id = {id}")
    user_data = cur.fetchone()  # none / (123, )
    if user_data == None:
        cur.execute(f'INSERT INTO users VALUES({id}, "{name}", 0, 0)')

        conn.commit()

    # Подключение закрыть
    conn.close()


def update_wins_knb(id, result):
    # Подлючаемся к бдхе
    conn = sqlite3.connect("game_bot.db")
    # Создать курсор
    cur = conn.cursor()
    cur.execute(
        f"UPDATE users SET knb_win = knb_win + 1, knb_games = knb_games + 1 WHERE id = {id}"
    )
    if result == "w":
        cur.execute(
            f"UPDATE users SET knb_win = knb_win + 1, knb_games = knb_games + 1 WHERE id = {id}"
        )
    else:
        cur.execute(f"UPDATE users SET knb_games = knb_games + 1 WHERE id = {id}")
    cur.execute
    conn.commit()
    # Подключение закрыть
    conn.close()


def select_stat():
    # Подлючаемся к бдхе
    conn = sqlite3.connect("game_bot.db")
    # Создать курсор
    cur = conn.cursor()
    cur.execute("SELECT name,  knb_win, knb_games FROM users")
    data = cur.fetchall()  # (['user1', 5, 8], ['user2', 7, 10])

    # 1 ([62.5, 'user1'], [70, 'user2'])
    # 2 lst.sort(reverse=True)
    # return lst