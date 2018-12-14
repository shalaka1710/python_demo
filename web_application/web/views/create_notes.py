from flask import Blueprint,render_template,request,redirect
import random

bp_craete_notes = Blueprint('__name__', __name__,template_folder='templates')

@bp_craete_notes.route('/notes_view', methods = ['POST','GET'])

def show():
    if request.method == 'POST':
        if request.form.get('createnote'):
            text = request.form.get('note_text')
            with open('../notes/{}.note'.format(number_generation()),'w+') as _file:
                _file.write(text)
            _file.close()
            return redirect('/')
    return render_template('notes_view.html')



def number_generation(length=10):
    final_string =''
    chars = 'abcdefghijklmnopqrstuvwxyz60123456789'
    for i in range (0,length):
        final_string += chars[random.randint(0,len(chars)-1)]
    return final_string