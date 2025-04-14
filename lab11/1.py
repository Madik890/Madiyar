import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="phonebook_db2",
    user="postgres",
    password="e.madiar228",  
    host="localhost",
    port="55555"
)
cur = conn.cursor()

def search_by_pattern(pattern):
    cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
    results = cur.fetchall()
    print("\n🔍 Результаты поиска:")
    for row in results:
        print(f"Name: {row[0]}, Phone: {row[1]}")

def insert_or_update_user(name, phone):
    cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
    conn.commit()
    print(f"✅ Пользователь {name} добавлен или обновлён.")

def insert_many_users(user_list):
    cur.execute("CALL insert_many_users(%s);", (user_list,))
    conn.commit()
    print("✅ Массовая вставка завершена.")

def get_paginated_contacts(limit, offset):
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
    results = cur.fetchall()
    print(f"\n📄 Пагинация (limit={limit}, offset={offset}):")
    for row in results:
        print(f"Name: {row[0]}, Phone: {row[1]}")

def delete_user(identifier):
    cur.execute("CALL delete_contact(%s);", (identifier,))
    conn.commit()
    print(f"❌ Контакт с '{identifier}' удалён.")

def main_menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Поиск по шаблону")
        print("2. Добавить или обновить пользователя")
        print("3. Массовое добавление пользователей")
        print("4. Получить записи с пагинацией")
        print("5. Удалить пользователя")
        print("0. Выйти")

        choice = input("Выбор: ")

        if choice == "1":
            pattern = input("Введите шаблон (имя/номер): ")
            search_by_pattern(pattern)

        elif choice == "2":
            name = input("Имя: ")
            phone = input("Телефон: ")
            insert_or_update_user(name, phone)

        elif choice == "3":
            count = int(input("Сколько пользователей добавить? "))
            users = []
            for _ in range(count):
                name = input("Имя: ")
                phone = input("Телефон: ")
                users.append([name, phone])
            insert_many_users(users)

        elif choice == "4":
            limit = int(input("Лимит: "))
            offset = int(input("Смещение: "))
            get_paginated_contacts(limit, offset)

        elif choice == "5":
            ident = input("Имя или телефон для удаления: ")
            delete_user(ident)

        elif choice == "0":
            print("👋 До свидания!")
            break

        else:
            print("⚠️ Неверный выбор")

# Запуск меню
if __name__ == "__main__":
    main_menu()
    cur.close()
    conn.close()
