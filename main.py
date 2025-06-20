from flask import Flask, request, render_template
import os

app = Flask(__name__)

def quiz_counter(): #퀴즈 파일 몇 개 인지 확인
    try:
        count = 0
        while 1:
            with open(os.getcwd() + "\\quiz\\" + "quiz_content" + str(count + 1) + ".txt", "r", encoding="utf-8"):
                pass
            count += 1

    except FileNotFoundError:
        return count

def quiz_reader(num): #퀴즈 내용 가져오기
    return_text = []
    num = int(num)

    if num > quiz_counter() or num <= 0:
        return False
    
    num = str(num)

    with open(os.getcwd() + "\\quiz\\" + "quiz_content" + num + ".txt", "r", encoding="utf-8") as f:
        return_text = f.read().split('\ncut')
    
    return_text[1] = return_text[1].replace('\n', "<br>")
    
    return_text[2] = return_text[2].split('/')

    return return_text
    


@app.route("/")
def home():
    return render_template('quiz_index.html', count = quiz_counter() )

@app.route("/v")
def vd():
    return render_template('help.html')


@app.route("/quiz", methods=['POST']) #methods=['GET', 'POST']
def quiz():
    quiz_number_P = request.form['quiz_number']

    return_quiz = quiz_reader(quiz_number_P)

    if return_quiz == False:
        return render_template('main_quiz_index.html',
                               st = "nopass",
                               quiz_numb = quiz_number_P,
                               quiz_title = "E", 
                               quiz_content = "E", 
                               quiz_choice = "E",
                               quiz_answer = "E"
                               )
    
    mega_temp = ''
    for i in return_quiz[2]:
        mega_temp += i + ' '

    return render_template('main_quiz_index.html',
                               st = "nopass",
                               quiz_numb = quiz_number_P,
                               quiz_title = return_quiz[0], 
                               quiz_content = return_quiz[1], 
                               quiz_choice = mega_temp,
                               quiz_answer = return_quiz[-1]
                               )

@app.route("/quiz_check", methods=['POST'])
def quiz_check():
    temp = quiz_reader( request.form['number'] )

    mega_temp = ''
    for i in temp[2]:
        mega_temp += i + ' '

    if str(request.form['answer']) == str(request.form['real_answer']):
        return render_template('main_quiz_index.html',
                               st = "pass",
                               quiz_numb = request.form['number'],
                               quiz_title = temp[0], 
                               quiz_content = temp[1], 
                               quiz_choice = mega_temp,
                               quiz_answer = temp[-1]
                               )
    
    return render_template('main_quiz_index.html',
                               st = "nonopass",
                               quiz_numb = request.form['number'],
                               quiz_title = temp[0], 
                               quiz_content = temp[1], 
                               quiz_choice = mega_temp,
                               quiz_answer = temp[-1]
                               )
    
    
# <form action = "/quiz_check" method="POST">
# 정답: <input type = "text" name = "answer">
# <input type="hidden" name="real_answer" value = {{quiz_answer}}>
# <input type="hidden" name="number" value = {{quiz_numb}}>
# <input type = "submit" value = "확인">
# </form>


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# <form action = "/quiz_check" method="POST">
#   정답: <input type = "text" name = "answer">
#    <input type="hidden" name="real_answer" value = {{quiz_answer}}>
#    <input type="hidden" name="number" value = {{quiz_numb}}>
#   <input type = "submit" value = "확인">
# </form>