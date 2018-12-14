from flask import Blueprint,render_template
import glob

''' glob listing file inside directory'''
bp = Blueprint('__name', __name__,template_folder='templates')

@bp.route('/')
def show():
        return render_template('index.html',notes=fetch_notes())

def fetch_notes():
        final_notes = []
        notes = glob.glob('../notes/*.note')
        for note in notes:
                with open(note) as _file:
                        final_notes.append(_file.read())
                _file.close()
        return final_notes
