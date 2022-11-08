from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_most_rated_shows():
    return data_manager.execute_select('''
    SELECT shows.id,
    shows.title,
    shows.year,
    shows.runtime,
    to_char(shows.rating,'999.9') AS rating,
    string_agg(genres.name,',' ORDER BY genres.name) AS genres,
    shows.trailer,
    shows.homepage
    FROM shows
    JOIN show_genres ON shows.id = show_genres.show_id
    JOIN genres ON show_genres.genre_id = genres.id
    GROUP BY shows.id
    ORDER BY shows.rating DESC
    LIMIT 15;
    ''')
