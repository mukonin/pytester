#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Tkinter import *


# In[2]:


from repo import read_repo
from repo import write_repo


# In[3]:


label_font = ("Helvetica", 18)
button_font = ("Helvetica", 16)
question_font = ("Helvetica", 14)
answer_font = ("Helvetica", 14)


# In[36]:


def mapping():
    tests = []
    test1 = {
        "question": "вопрос 1",
        "answer_1": "ответ 1",
        "answer_2": "ответ 2",
        "answer_3": "ответ 3",
        "answer_4": "ответ 4",
        "correct": 2
    }
    test2 = {
        "question": "вопрос 2",
        "answer_1": "ответ 1",
        "answer_2": "ответ 2",
        "answer_3": "ответ 3",
        "answer_4": "ответ 4",
        "correct": 3
    }
    tests.append(test1)
    tests.append(test2)
    write_repo('abc', tests)
    tests = read_repo('abc')
    print tests[0]['question']


# In[62]:


def next_question():
    save_question()
    global question_index
    if question_index < (len(questions) - 1):
        # save current question
        question_index = question_index + 1
        clear_all()
        draw_question()


# In[77]:


def prev_question():
    save_question()
    global question_index
    if question_index > 0:
        # save current question
        question_index = question_index - 1
        clear_all()
        draw_question()


# In[78]:


def add_question():
    save_question()
    global question_index
    new_question = get_empty_question()
    questions.append(new_question)
    question_index = len(questions) - 1
    clear_all()
    draw_question()


# In[81]:


def save_question():
    question = questions[question_index]
    global question_text
    global question_1_text
    global question_2_text
    global question_3_text
    global question_4_text
    question["question"] = question_text.get("1.0", 'end-1c')
    question["answer_1"] = question_1_text.get("1.0", 'end-1c')
    question["answer_2"] = question_2_text.get("1.0", 'end-1c')
    question["answer_3"] = question_3_text.get("1.0", 'end-1c')
    question["answer_4"] = question_4_text.get("1.0", 'end-1c')
    question["correct"] = rb_control.get()


# In[90]:


def del_question():
    global question_index
    del questions[question_index]
    if question_index == len(questions):
        question_index = question_index - 1
    clear_all()
    draw_question()


# In[99]:


def save_all():
    save_question()
    write_repo(password, questions)


# In[7]:


def clear_all():
    for element in elements:
        element.place_forget()
    del elements[:]


# In[8]:


class App(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master


# In[73]:


def draw_pass():
    local_elements = []

    pass_input = Text(height = 1, width = 20, font = question_font)
    pass_input.place(x = 5, y = 5)
    local_elements.append(pass_input)

    pass_button = Button(text = "відкрити", command = lambda: open_repo(pass_input.get("1.0", 'end-1c')), height = 1, width = 10, font = button_font)
    pass_button.place(x = 5, y = 35)
    local_elements.append(pass_button)
    
    elements.extend(local_elements)


# In[93]:


def open_repo(key):
    global password
    password = key
    try:
        questions.extend(read_repo(key))
        clear_all()
        if len(questions) == 0:
            new_question = get_empty_question()
            questions.append(new_question)
        draw_question()
    except IOError:
        pass
        clear_all()
        if len(questions) == 0:
            new_question = get_empty_question()
            questions.append(new_question)
        draw_question()
    except TypeError:
        root.destroy()
        quit()
    except ValueError:
        root.destroy()
        quit()


# In[11]:


def get_empty_question():
    return {
        "question": "",
        "answer_1": "",
        "answer_2": "",
        "answer_3": "",
        "answer_4": "",
        "correct": 1
    }


# In[96]:


def draw_question():
    local_elements = []
    question = questions[question_index]

    question_header = Label(text = "Питання: {}/{}".format(question_index + 1, len(questions)), font = label_font)
    question_header.place(x = 5, y = 0)
    local_elements.append(question_header)
    
    global question_text
    question_text = Text(height = 10, width = 78, wrap = WORD, font = question_font)
    question_text.place(x = 5, y = 30)
    question_text.insert(END, question["question"])
    local_elements.append(question_text)
    
    answer_label = Label(text = "Варіанти відповідей:", font = label_font)
    answer_label.place(x = 5, y = 250)
    local_elements.append(answer_label)
    
    rb_control.set(question["correct"])
    
    answer_1_rb = Radiobutton(variable = rb_control, value = 1)
    answer_1_rb.place(y = 300)
    local_elements.append(answer_1_rb)

    answer_2_rb = Radiobutton(variable = rb_control, value = 2)
    answer_2_rb.place(y = 350)
    local_elements.append(answer_2_rb)

    answer_3_rb = Radiobutton(variable = rb_control, value = 3)
    answer_3_rb.place(y = 400)
    local_elements.append(answer_3_rb)

    answer_4_rb = Radiobutton(variable = rb_control, value = 4)
    answer_4_rb.place(y = 450)
    local_elements.append(answer_4_rb)
    
    global question_1_text
    question_1_text = Text(height = 2, width = 75, wrap = WORD, font = answer_font)
    question_1_text.place(x = 35, y = 285)
    question_1_text.insert(END, question["answer_1"])
    local_elements.append(question_1_text)
    
    global question_2_text
    question_2_text = Text(height = 2, width = 75, wrap = WORD, font = answer_font)
    question_2_text.place(x = 35, y = 335)
    question_2_text.insert(END, question["answer_2"])
    local_elements.append(question_2_text)
    
    global question_3_text
    question_3_text = Text(height = 2, width = 75, wrap = WORD, font = answer_font)
    question_3_text.place(x = 35, y = 385)
    question_3_text.insert(END, question["answer_3"])
    local_elements.append(question_3_text)
    
    global question_4_text
    question_4_text = Text(height = 2, width = 75, wrap = WORD, font = answer_font)
    question_4_text.place(x = 35, y = 435)
    question_4_text.insert(END, question["answer_4"])
    local_elements.append(question_4_text)
    
    prev_button = Button(text = "попередне", command = prev_question, height = 1, width = 10, font = button_font)
    prev_button.place(x = 5, y = 500)
    local_elements.append(prev_button)
    
    next_button = Button(text = "наступне", command = next_question, height = 1, width = 10, font = button_font)
    next_button.place(x = 200, y = 500)
    local_elements.append(next_button)
    
    add_button = Button(text = "додати", command = add_question, height = 1, width = 10, font = button_font)
    add_button.place(x = 5, y = 550)
    local_elements.append(add_button)
    
    del_button = Button(text = "видалити", command = del_question, height = 1, width = 10, font = button_font)
    del_button.place(x = 200, y = 550)
    local_elements.append(del_button)
    
    save_button = Button(text = "зберегти", command = save_all, height = 1, width = 10, font = button_font)
    save_button.place(x = 600, y = 550)
    local_elements.append(save_button)

    elements.extend(local_elements)


# In[102]:


root = Tk()
root.geometry("800x600")
root.wm_title("Тест")

elements = []
questions = []
question_index = 0
password = ''
rb_control = IntVar()

question_text = {}
question_1_text = {}
question_2_text = {}
question_3_text = {}
question_4_text = {}


draw_pass()

root.mainloop()

