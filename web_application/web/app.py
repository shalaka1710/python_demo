from flask import Flask
from web.views.index import bp as index_bp
from web.views.create_notes import bp_craete_notes as c_bp

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(c_bp)

'''@app.route('/')
def home():
    return "Hello World" '''