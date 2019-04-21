from app import app
import os
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import flash
from flask import session
from flask import send_from_directory
from app.forms import TranslateForm


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.png', mimetype='image/vnd.microsoft.icon')


@app.route("/index")
@app.route('/')
def index():
    return render_template('index.html',
                           title='Main page')


@app.route('/translator', methods=['GET', 'POST'])
def translator():
    translate_form = TranslateForm()
    if translate_form.validate_on_submit():
        pass
        return redirect(url_for('translator'))

    if request.method == 'GET':
        translate_form.input_text.data = session.pop('text', "Input text")
    return render_template('translate.html',
                           title="translate",
                           translate_form=translate_form)


@app.route('/about')
def about():
    return render_template('about.html',
                           title='About')
