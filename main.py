from flask import Flask, render_template, url_for, request
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/shows/')
@app.route('/shows/most-rated')
def most_rated():
    page_number = request.args.get('page', default=1, type=int)
    shows = queries.get_most_rated_shows(page_number)
    shows_quantity_dictionary = queries.count_shows_element()
    shows_quantity = list(shows_quantity_dictionary[0].items())[0][1]
    max_pagination = math.ceil(shows_quantity/15)
    return render_template('most-rated.html', shows=shows, page_number=page_number, shows_quantity=shows_quantity,
                           max_pagination=max_pagination)


@app.route('/show/<int:id>')
def show_details(id):
    shows = queries.get_show_details()
    seasons = queries.get_seasons_for_show(id)
    return render_template('show-details.html', id=id, shows=shows, seasons=seasons)


@app.template_filter('convert_runtime')
def convert_runtime(runtime):
    if runtime < 60:
        return f'{runtime}min'
    elif runtime % 60 == 0:
        return f'{runtime//60}h'
    else:
        hours = f'{runtime//60}h'
        minutes = f'{runtime % 60}min'
        return hours + minutes


@app.route('/actors')
def actors():
    actor_list = queries.get_actors_list()
    return render_template('list_actors.html', actor_list=actor_list)


@app.route('/actors/<int:id>')
def actor_shows(id):
    actor_list = queries.get_actor_shows(id)
    return {"actor_list": actor_list}


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
