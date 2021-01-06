from flask import Flask, render_template, url_for
from forms import SignUpForm
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lozinka'

@app.route('/')
def naslovna():
    return render_template('naslovna.html')

@app.route('/o_nama')
def o_nama():
    return render_template('o_nama.html')

@app.route('/izjava_o_privatnosti')
def izjava_o_privatnosti():
    return render_template('izjava_o_privatnosti.html')

@app.route('/novosti')
def novosti():
    form = SignUpForm()
    return render_template('novosti.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)