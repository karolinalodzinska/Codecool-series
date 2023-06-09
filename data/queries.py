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


def get_show_details():
    return data_manager.execute_select('''
    SELECT shows.id,
    shows.title,
    shows.year,
    shows.runtime,
    round(shows.rating, 1) AS rating,
    string_agg(DISTINCT genres.name,',' ORDER BY genres.name) AS genres,
    shows.overview,
    shows.trailer,
    array_to_string((array_agg(DISTINCT actors.name))[1:3], ', ') AS actors
    FROM shows
    LEFT JOIN show_characters ON shows.id = show_characters.show_id
    LEFT JOIN show_genres ON shows.id = show_genres.show_id
    LEFT JOIN genres ON genres.id = show_genres.genre_id
    LEFT JOIN actors ON actors.id = show_characters.actor_id
    GROUP BY shows.id
    ''')


def get_seasons_for_show(id):
    return data_manager.execute_select('''
    SELECT seasons.id,
    seasons.season_number,
    seasons.title,
    seasons.overview
    FROM seasons
    WHERE seasons.show_id = %(id)s
    ORDER BY seasons.season_number;
    ''', variables={"id": id})


def get_actors_list():
    return data_manager.execute_select('''
    SELECT actors.id,
    SUBSTR(actors.name,1, POSITION(' ' IN actors.name)) AS name,
    actors.birthday
    FROM actors
    ORDER BY actors.birthday ASC
    LIMIT 100
    ''')


def get_actor_shows(id):
    return data_manager.execute_select('''
    SELECT shows.title,
    actors.id
    FROM shows
    LEFT JOIN show_characters ON shows.id = show_characters.show_id
    LEFT JOIN actors ON show_characters.actor_id = actors.id
    WHERE actors.id = %(id)s
    ''', variables={"id": id})

