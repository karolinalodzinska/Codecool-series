from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_most_rated_shows(page_number):
    return data_manager.execute_select('''
    SELECT shows.id,
    shows.title,
    shows.year,
    shows.runtime,
    round(shows.rating, 1) AS rating,
    string_agg(genres.name,',' ORDER BY genres.name) AS genres,
    shows.trailer,
    shows.homepage
    FROM shows
    LEFT JOIN show_genres ON shows.id = show_genres.show_id
    LEFT JOIN genres ON show_genres.genre_id = genres.id
    GROUP BY shows.id
    ORDER BY shows.rating DESC
    LIMIT 15
    OFFSET ((%(page_number)s -1) * 15);
    ''', variables={"page_number": page_number})


def count_shows_element():
    return data_manager.execute_select('SELECT count(id) FROM shows;')
