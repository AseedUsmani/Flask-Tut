# run.py

import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)
app.config['SECRET_KEY'] = 'any secret string'

if __name__ == '__main__':
    app.run(host='localhost', port=8000)