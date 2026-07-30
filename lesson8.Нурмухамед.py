import sqlite3


def run_cinema_view_demo():
    conn = sqlite3.connect('netflix.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Создаем VIEW (виртуальную таблицу со всей статистикой)
    cursor.execute("""
                   CREATE VIEW IF NOT EXISTS movie_analytics AS
                   SELECT m.title                 AS movie_title,
                          m.genre                 AS movie_genre,
                          COUNT(r.id)             AS total_reviews,
                          ROUND(AVG(r.rating), 2) AS avg_rating,
                          MAX(r.rating)           AS max_rating,
                          MIN(r.rating)           AS min_rating
                   FROM movies m
                            LEFT JOIN reviews r ON m.id = r.movie_id
                   GROUP BY m.id;
                   """)
    conn.commit()

    # Теперь обращаемся к VIEW как к обычной таблице
    print("--- ДАННЫЕ ИЗ VIEW (АНАЛИТИКА ПО ФИЛЬМАМ) ---")
    cursor.execute("SELECT * FROM movie_analytics;")

    for title, genre, count, avg_r, max_r, min_r in cursor.fetchall():
        print(f"Фильм: {title} ({genre})")
        print(f"  Всего отзывов: {count}")
        print(f"  Средняя оценка: {avg_r if avg_r else 'Нет'}")
        print(f"  Макс/Мин: {max_r if max_r else '-'}/{min_r if min_r else '-'}")
        print("-" * 40)

    conn.close()


if __name__ == "__main__":
    run_cinema_view_demo()

