from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def ad():
    ad_text = ["Человечество вырастает из детства.",
               "Человечеству мала одна планета.",
               "Мы сделаем обитаемыми безжизненные пока планеты.",
               "И начнем с Марса!",
               "Присоединяйся!"]
    return '</br></br>'.join(ad_text)


@app.route('/image_mars')
def mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}">
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def bootstrap():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                        <title>Привет, Яндекс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}">
                        <div class="alert alert-dark" role="alert">
                            <h2>Человечество вырастает из детства.</h2>
                        </div>
                        <div class="alert alert-success" role="alert">
                            <h2>Человечеству мала одна планета.</h2>
                        </div>
                        <div class="alert alert-dark" role="alert">
                            <h2>Мы сделаем обитаемыми безжизненные пока планеты.</h2>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <h2>И начнем с Марса!</h2>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <h2>Присоединяйся!</h2>
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
