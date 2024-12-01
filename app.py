from flask import Flask, render_template

app = Flask(__name__)

@app.route('/adinco')
def home():
    return render_template('adinco.html', active_page='home')

@app.route('/questions')
def questions():
    return render_template('questions.html', active_page='questions')

@app.route('/community')
def community():
    return render_template('community.html', active_page='community')

@app.route('/blog')
def blog():
    return render_template('blog.html', active_page='blog')

@app.route('/ask_question')
def ask_question():
    return render_template('ask_question.html', active_page='ask_question')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')