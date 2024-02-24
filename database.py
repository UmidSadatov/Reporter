import psycopg2
import sqlite3

# Подключение к базе данных
postgre_connection = psycopg2.connect(
    # 94.158.59.109   Global
    # 192.168.0.164   Local
    host="192.168.0.164",  # Адрес сервера, например, "localhost" или IP-адрес
    database="ReporterDB",  # Имя базы данных
    user="postgres",  # Имя пользователя
    password="umid6666543"  # Пароль
)

# Создание курсора для выполнения операций с базой данных
postgre_cursor = postgre_connection.cursor()

# Выполнение SQL-запроса
# postgre_cursor.execute("SELECT version();")

# SQLITE
sqlite_connection = sqlite3.connect('reports.db')
sqlite_connection.row_factory = sqlite3.Row
sqlite_cursor = sqlite_connection.cursor()

sqlite_cursor.execute("""SELECT * FROM All_Regions""")
Regions_Data = sqlite_cursor.fetchall()
sqlite_connection.commit()

for Region_Data in Regions_Data:
    postgre_cursor.execute(
        'INSERT INTO public."RegionsUnnorm"(region,norm_id) '
        'VALUES (%s,%s)',
        (
            Region_Data['unique_region'],
            Region_Data['general_id'],
        )
    )


# postgre_cursor.execute("""CREATE TABLE "RegionsUnnorm" (
#     id SERIAL PRIMARY KEY,
#     "region" TEXT UNIQUE,
#     norm_id INTEGER,
#     FOREIGN KEY (norm_id) REFERENCES "Regions"(id)
# );
# """)

postgre_connection.commit()
