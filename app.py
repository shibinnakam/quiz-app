from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Quiz questions
questions = [
    {
        'question': "What is the capital of France?",
        'options': ["Paris", "London", "Berlin", "Madrid"],
        'correct_answer': 0
    },
    {
        'question': "Which planet is known as the Red Planet?",
        'options': ["Earth", "Mars", "Jupiter", "Venus"],
        'correct_answer': 1
    },
    {
        'question': "Who developed the theory of relativity?",
        'options': ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Galileo Galilei"],
        'correct_answer': 1
    },
    {
        'question': "What is the largest mammal on Earth?",
        'options': ["Elephant", "Blue Whale", "Giraffe", "Shark"],
        'correct_answer': 1
    },
    {
        'question': "What is the square root of 16?",
        'options': ["2", "3", "4", "5"],
        'correct_answer': 2
    }
]

# Score variable
score = 0
current_question_index = 0

@app.route('/', methods=['GET', 'POST'])
def home():
    global score, current_question_index
    if request.method == 'POST':
        answer = int(request.form.get('answer'))
        correct_answer = questions[current_question_index]['correct_answer']
        if answer == correct_answer:
            score += 1

        current_question_index += 1
        if current_question_index >= len(questions):
            return redirect(url_for('result'))

    question = questions[current_question_index]
    return render_template('index.html', question=question, score=score, current_question_index=current_question_index)

@app.route('/result')
def result():
    return render_template('result.html', score=score,total_questions=len(questions))

@app.route('/reset', methods=['POST'])
def reset():
    global score, current_question_index
    score = 0
    current_question_index = 0
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)