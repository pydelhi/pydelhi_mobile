from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App
from kivy.factory import Factory




class ScreenQuiz(Screen):
    '''KBC game'''

    Builder.load_string('''
<OptionButton@Button>
    correct: False
    background_color: (1, 1, 1, 1) if self.state == 'normal' else ((0, 1, 0, 1) if self.correct == "True" else (1, 0, 0, 1))
    background_normal: 'atlas://data/default/button'
    background_down: self.background_normal
    on_release: app.screenquiz.correct_answer() if self.correct == 'True' else app.screenquiz.wrong_answer()

<ScreenQuiz>
    name: 'ScreenQuiz'
    AsyncImage
        allow_stretch: True
        #  keep_ratio: False
        source: 'http://www.wisdomforwinning.net/wp-content/uploads/2015/09/11-ridiculous-gifts-for-the-millionaire-who-has-everything.jpg'
    BoxLayout
        orientation: 'vertical'
        Label
            id: lbl_question
            text: 'Your Question Here'
        GridLayout
            cols: 2
            size_hint_y: None
            height: dp(200)
            id: grid_options
       

''')

    def on_enter(self):    
        import json
        data = ''
        with open('data/questions.json') as fl:
            data = json.load(fl)
        questions = data
        self.questions = questions
        self.current_question = -1
        self.load_next_question()

    def load_next_question(self):
        try:
            self.current_question += 1
            allquestions = self.questions['Questions']
            question = allquestions[self.current_question]
            question_text = question.keys()[0]
            qoptions = question[question_text]
            self.display_question(question_text, qoptions)
        except IndexError:
            pass
    
    def display_question(self,question, options):
        self.ids.lbl_question.text = question
        self.ids.grid_options.clear_widgets()
        for option in options.keys():
            ob = Factory.OptionButton(text=option)
            self.ids.grid_options.add_widget(ob)
            ob.correct = options[option]

    def correct_answer(self):
        self.load_next_question()

    def wrong_answer(self):
        print('wrong answer')
