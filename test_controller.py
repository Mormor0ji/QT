from flask import Flask, request, render_template
from test_model import waiting_num

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('test_index.html')


places = ['post', 'coop']

#hej hanna 2
@app.route('/add_place', methods=['POST'])
def add_place():
    place = request.form['place']
    if place in places:
        return render_template('view.html')
    else:
        return render_template('test_index.html')


@app.route('/add_ticket', methods=['POST'])
def add_ticket():
    ticket_num = request.form['ticket_num']
    return render_template('ticket_page.html', variable= ticket_num)


@app.route('/show_ticket')
def show_ticket():
    current_num = '342'
    return render_template('ticket_page.html',cnummer=current_num)


if __name__ == '__main__':
    app.run(debug=True)
