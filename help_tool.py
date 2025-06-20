def make_quiz_file(num):
    with open("quiz_content" + str(num) + ".txt", "w", encoding="utf-8"):
        pass

# make_quiz_file(1)

# def quiz_reader(num): #퀴즈 내용 가져오기
#     return_text = []

#     num = str(num)

#     with open("quiz_content" + num + ".txt", "r", encoding="utf-8") as f:
#         return_text = f.read().split('\n')

#     return_text[2] = return_text[2].split('/')
#     return_text[3] = return_text[3].split('/')

    
#     return return_text

# print(quiz_reader(1))

make_quiz_file(2)
make_quiz_file(3)
make_quiz_file(4)