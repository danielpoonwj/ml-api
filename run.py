from app import flask_app

if __name__ == '__main__':
    flask_app.run(
        host='127.0.0.1',
        port=9090,
        debug=True
    )
