'''
Creates the main menu for the program, gets the username
and stores for future use and personalization.
'''
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDFlatButton, MDRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.slider import MDSlider
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix import screen,fitimage
from kivy.properties import StringProperty
from kivy.uix.behaviors import DragBehavior
from kivy.uix.stacklayout import StackLayout
import random
import time
from kivy.uix.widget import Widget
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window
from kivy.core.image import Image
from kivy.graphics import BorderImage
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.core.window import Window


class WelcScreen(Screen):
    pass    

class MathScreen(Screen):
    pass

class Add1Screen(Screen):
    pass

class Add2Screen(Screen):
    pass

class Add3Screen(Screen):
    pass

class Sub1Screen(Screen):
    pass

class Sub2Screen(Screen):
    pass

class Mul1Screen(Screen):
    pass

class Mul2Screen(Screen):
    pass

class Div1Screen(Screen):
    pass

class Div2Screen(Screen):
    pass

class Manager(ScreenManager):
    welc_screen = ObjectProperty(None)
    math_screen = ObjectProperty(None)
    add1_screen = ObjectProperty(None)
    add2_screen = ObjectProperty(None)
    add3_screen = ObjectProperty(None)
    sub1_screen = ObjectProperty(None)
    sub2_screen = ObjectProperty(None)
    mul1_screen = ObjectProperty(None)
    mul2_screen = ObjectProperty(None)
    div1_screen = ObjectProperty(None)
    div2_screen = ObjectProperty(None)

# choses two random numbers between 1 and 9 and adds them together
class MyLayoutAdd(Widget):
    num1 = 0
    num2 = 0
    answer = num1 + num2

    def gen_num1(self):
        # generate two random numbers between 1 and 9
        self.num1 = random.randint(1, 9)
        return self.num1

    def gen_num2(self):
        # generate two random numbers between 1 and 9
        self.num2 = random.randint(1, 9)
        return self.num2

    def gen_answer(self):
        # add the two random numbers together
        self.answer = self.num1 + self.num2
        return self.answer

class MyLayoutMul(Widget):
    num1 = 0
    num2 = 0
    answer = num1 * num2

    def gen_num1(self):
        # generate two random numbers between 1 and 9
        self.num1 = random.randint(1, 9)
        return self.num1

    def gen_num2(self):
        # generate two random numbers between 1 and 9
        self.num2 = random.randint(1, 9)
        return self.num2

    def gen_answer(self):
        # add the two random numbers together
        self.answer = self.num1 * self.num2
        return self.answer

class MyLayoutSub(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # make sure we aren't overriding any important functionality
        self.num1 = 0
        self.num2 = 0

    def gen_num1(self):
        # generate two random numbers between 1 and 9
        self.num1 = random.randint(1, 9)
        return self.num1

    def gen_num2(self):
        print(self.num1)
        not_yet = True
        # generate two random numbers between 1 and 9
        self.num2 = random.randint(1, 9)
        # make sure that the second number is smaller than the first
        while (not_yet):
            if self.num2 <= self.num1:
                not_yet = False
                return self.num2
            else:
                self.num2 = random.randint(1, 9)
    
    def gen_answer(self):
        # add the two random numbers together
        self.answer = self.num1 - self.num2
        while self.answer >= 0:
            self.answer = self.num1 - self.num2
        return self.answer
    
class MyLayoutDiv(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # make sure we aren't overriding any important functionality
        self.num1 = 0
        self.num2 = 0

    def gen_num1(self):
        # generate two random numbers between 1 and 9
        self.num1 = random.randint(1, 9)
        return self.num1

    def gen_num2(self):
        print(self.num1)
        not_yet = True
        # generate two random numbers between 1 and 9
        self.num2 = random.randint(1, 9)
        # make sure that the second number is smaller than the first
        while (not_yet):
            if self.num1 % self.num2 == 0:
                not_yet = False
                return self.num2
            else:
                self.num2 = random.randint(1, 9)

    def gen_answer(self):
        # add the two random numbers together
        self.answer = self.num1 / self.num2
        return self.answer

class PlusMin(BoxLayout):
     count = 0
     my_text = StringProperty('1')
#     add_or_sub = 0 # 0 = add, 1 = subtract  
#     def on_button_pos_click(self):
#         self.count += 1
#         self.my_text = str(self.count)
#     def on_button_neg_click(self):
#         self.count -= 1
#         self.my_text = str(self.count)

class HTCApp(MDApp):

    # add_click
    count = [0,0]
    dialog = None

    # sub_click
    sub_count = [0,0]

    # div_click
    div_count = [0,0]
    
    # mul_slider
    mul_slider = [0,0]

    # sub number 1
    sub_num1 = [0]
    
    def build(self):
        # Handles primary themes
        self.title = 'Ocean Adding'
        Window.clearcolor = (1, 1, 1, 1)
        #self.theme_cls.theme_style = "Light"
        #self.theme_cls.primary_palette = "Indigo"
        Window.size = (450, 750)
        return Manager()
    
    def on_start(self) -> None:
        with open('user.txt','r') as file:
            name = file.read().strip()
        with open('points.txt','r') as file:
            points = file.read().strip()
        self.root.ids.welc_screen.ids.name_label.text = f'Welcome back to Ocean Adding\n{name}!\nYou have {points} points!\n\n'
    
    def wipe_points(self):
            # add points!
            with open('points.txt','r') as file:
                line = file.read().strip()
            old_points = int(line)
            new_points = 0
            with open('points.txt','w') as file:
                file.write(str(new_points))
            self.root.ids.math_screen.ids.pearls.text = str(new_points)
        
    def get_name(self):
        # get a reference to the AddWindow Screen
        welcscreen_instance = self.root.get_screen('welcome')
        name = welcscreen_instance.ids["juicer"].text
        
        with open('user.txt','r') as file:
            this_name = file.read().strip()
        if name != '':
            with open("user.txt", mode="w") as file:
                file.writelines(f"{name}")
            self.wipe_points()
            
        with open('user.txt','r') as file:
            this_name = file.read().strip()
        self.root.ids.math_screen.ids.display_name.text = f'Select the type of math\n you would like to practice {this_name}!'
            
        with open('points.txt','r') as file:
            points = file.read().strip()
        self.root.ids.math_screen.ids.pearls.text = str(points)
            
    def load_addition(self):
        '''Creates addition grid'''
        test = MyLayoutAdd()
        n1 = test.gen_num1()
        n2 = test.gen_num2()
        ans = n1+n2
        combined = f'{str(n1)}+{str(n2)}'
        self.root.ids.add1_screen.ids.addatext.text = str(combined)
        answer_box = 'adda'+str(random.randint(1,9))
        
        # choose a random cell to place the answer
        random_cell = random.randint(1,9)
        self.root.ids.add1_screen.ids['adda'+str(random_cell)].text = str(ans)

        # list of numbers to randomly fill the grid
        num_list = []
        for i in range(0, 19):
            num_list.append(i)
        random.shuffle(num_list)
        
        # fill the grid with random numbers, that are not the answer
        for i in range(1,10):
            if i != random_cell:
                self.root.ids.add1_screen.ids['adda'+str(i)].text = str(num_list[i])
                
    def load_multiplication(self):
        '''Creates addition grid'''
        test = MyLayoutMul()
        n1 = test.gen_num1()
        n2 = test.gen_num2()
        ans = n1*n2
        combined = f'{str(n1)}*{str(n2)}'
        self.root.ids.mul1_screen.ids.mulatext.text = str(combined)
        answer_box = 'mula'+str(random.randint(1,9))
        
        # choose a random cell to place the answer
        random_cell = random.randint(1,9)
        self.root.ids.mul1_screen.ids['mula'+str(random_cell)].text = str(ans)

        # list of numbers to randomly fill the grid
        num_list = []
        for i in range(0, 100):
            num_list.append(i)
        random.shuffle(num_list)
        
        # fill the grid with random numbers, that are not the answer
        for i in range(1,10):
            if i != random_cell:
                self.root.ids.mul1_screen.ids['mula'+str(i)].text = str(num_list[i])

    def load_division(self):
        '''Creates addition grid'''
        test = MyLayoutDiv()
        n1 = test.gen_num1()
        n2 = test.gen_num2()
        ans = int(n1 / n2)
        combined = f'{str(n1)}/{str(n2)}'
        self.root.ids.div1_screen.ids.divatext.text = str(combined)
        #answer_box = 'suba'+str(random.randint(1,9))
        
        # choose a random cell to place the answer
        random_cell = random.randint(1,9)
        self.root.ids.div1_screen.ids['diva'+str(random_cell)].text = str(ans)

        # list of numbers to randomly fill the grid
        num_list = []
        for i in range(0, 19):
            num_list.append(i)
        random.shuffle(num_list)
        
        # fill the grid with random numbers, that are not the answer
        for i in range(1,10):
            if i != random_cell:
                self.root.ids.div1_screen.ids['diva'+str(i)].text = str(num_list[i])
                
    def load_subtraction(self,sub_num1):
        '''Creates addition grid'''
        test = MyLayoutSub()
        n1 = test.gen_num1()
        sub_num1[0] = n1
        n2 = test.gen_num2()
        ans = n1 - n2
        combined = f'{str(n1)}-{str(n2)}'
        self.root.ids.sub1_screen.ids.subatext.text = str(combined)
        #answer_box = 'suba'+str(random.randint(1,9))
        
        # choose a random cell to place the answer
        random_cell = random.randint(1,9)
        self.root.ids.sub1_screen.ids['suba'+str(random_cell)].text = str(ans)

        # list of numbers to randomly fill the grid
        num_list = []
        for i in range(0, 19):
            num_list.append(i)
        random.shuffle(num_list)
        
        # fill the grid with random numbers, that are not the answer
        for i in range(1,10):
            if i != random_cell:
                self.root.ids.sub1_screen.ids['suba'+str(i)].text = str(num_list[i])
                
    def random_game(self,mode):
        '''Selects game from math menu. Must be passed
        mode to work properly'''
        self.root.transition.direction = 'left'
        rand_num = random.randint(1,2)   # amount of games per category
        if rand_num == 1:
            if mode == 'add':
                self.root.current = 'add1'
                self.load_addition()
            elif mode == 'sub':
                self.load_subtraction(self.sub_num1)
                self.root.current = 'sub1'
            elif mode == 'mul':
                self.root.current = 'mul1'
                self.load_multiplication()
            elif mode == 'div':
                self.root.current = 'div1'
                self.load_division()
        elif rand_num == 2:
            if mode == 'add':
                self.rando_add_clicker()
                self.root.current = 'add2'
            elif mode == 'sub':
                self.rando_sub_clicker()
                self.root.current = 'sub2'
            elif mode == 'mul':
                self.rando_mul_slider()
                self.root.current = 'mul2'
            elif mode == 'div':
                self.root.current = 'div2'
                self.rando_div_clicker()
            elif mode == 'wda':
                self.root.current = 'add3'
                
    def check_answer(self,cell):
        # actual answer
        add1screen_instance = self.root.get_screen('add1')
        #sub1screen_instance = self.root.get_screen('sub1')
        raw_answer_add = add1screen_instance.ids["addatext"].text
        #raw_answer_sub = sub1screen_instance.ids["subatext"].text
        answer_add = str(int(raw_answer_add[0]) + int(raw_answer_add[2]))
        #answer_sub = str(int(raw_answer_sub[0]) - int(raw_answer_sub[2]))
        
        # cells value
        raw_cell_answer = add1screen_instance.ids[cell].text
        if (raw_cell_answer == answer_add):
            
            # add points!
            with open('points.txt','r') as file:
                line = file.read().strip()
            old_points = int(line)
            new_points = old_points + 5
            with open('points.txt','w') as file:
                file.write(str(new_points))
            self.root.ids.math_screen.ids.pearls.text = str(new_points)

            self.dialog = MDDialog(
                    text = 'Great job! You solved it!',
                    title = 'TREASURE: +5 PEARLS',
                    buttons =[
                        MDRectangleFlatButton(
                        text = 'BACK', on_release = self.close_dialog
                        )
                    ]
                )
            self.dialog.open()
            self.root.transition.direction = 'right'
            self.root.current = 'math'
        else:
            self.dialog = MDDialog(
            text="Almost! Try again :)",
            radius=[20, 7, 20, 7],
            )
            self.dialog.open()

    def check_mul(self,cell):
        # actual answer
        mul1screen_instance = self.root.get_screen('mul1')
        
        raw_answer_mul = mul1screen_instance.ids["mulatext"].text
       
        answer_mul = str(int(raw_answer_mul[0]) * int(raw_answer_mul[2]))
    
        
        # cells value
        raw_cell_answer = mul1screen_instance.ids[cell].text
        if (raw_cell_answer == answer_mul):
            
            # add points!
            with open('points.txt','r') as file:
                line = file.read().strip()
            old_points = int(line)
            new_points = old_points + 5
            with open('points.txt','w') as file:
                file.write(str(new_points))
            self.root.ids.math_screen.ids.pearls.text = str(new_points)

            self.dialog = MDDialog(
                    text = 'Great job! You solved it!',
                    title = 'TREASURE: +5 PEARLS',
                    buttons =[
                        MDRectangleFlatButton(
                        text = 'BACK', on_release = self.close_dialog
                        )
                    ]
                )
            self.dialog.open()
            self.root.transition.direction = 'right'
            self.root.current = 'math'
        else:
            self.dialog = MDDialog(
            text="Almost! Try again :)",
            radius=[20, 7, 20, 7],
            )
            self.dialog.open()
        

    def check_answer_sub(self,cell):
        # actual answer
        sub1screen_instance = self.root.get_screen('sub1')
        raw_answer_sub = sub1screen_instance.ids["subatext"].text
        print(raw_answer_sub)
        answer_sub = str(int(raw_answer_sub[0]) - int(raw_answer_sub[2]))
        print(answer_sub)
        
        # cells value
        raw_cell_answer = sub1screen_instance.ids[cell].text
        if (raw_cell_answer == answer_sub):
            
            # add points!
            with open('points.txt','r') as file:
                line = file.read().strip()
            old_points = int(line)
            new_points = old_points + 5
            with open('points.txt','w') as file:
                file.write(str(new_points))
            self.root.ids.math_screen.ids.pearls.text = str(new_points)
                
            self.dialog = MDDialog(
                    text = 'Great job! You solved it!',
                    title = 'TREASURE: +5 PEARLS',
                    buttons =[
                        MDRectangleFlatButton(
                        text = 'BACK', on_release = self.close_dialog
                        )
                    ]
                )
            self.dialog.open()
            self.root.transition.direction = 'right'
            self.root.current = 'math'
        else:
            self.dialog = MDDialog(
            text="Almost! Try again :)",
            radius=[20, 7, 20, 7],
            )
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def check_answer_div(self,cell):
        # actual answer
        div1screen_instance = self.root.get_screen('div1')
        raw_answer_div = div1screen_instance.ids["divatext"].text
        print(raw_answer_div)
        answer_div = str(int(raw_answer_div[0]) // int(raw_answer_div[2]))
        print(answer_div)
        
        # cells value
        raw_cell_answer = div1screen_instance.ids[cell].text
        if (raw_cell_answer == answer_div):
            
            # add points!
            with open('points.txt','r') as file:
                line = file.read().strip()
            old_points = int(line)
            new_points = old_points + 5
            with open('points.txt','w') as file:
                file.write(str(new_points))
            self.root.ids.math_screen.ids.pearls.text = str(new_points)
                
            self.dialog = MDDialog(
                    text = 'Great job! You solved it!',
                    title = 'TREASURE: +5 PEARLS',
                    buttons =[
                        MDRectangleFlatButton(
                        text = 'BACK', on_release = self.close_dialog
                        )
                    ]
                )
            self.dialog.open()
            self.root.transition.direction = 'right'
            self.root.current = 'math'
        else:
            self.dialog = MDDialog(
            text="Almost! Try again :)",
            radius=[20, 7, 20, 7],
            )
            self.dialog.open()

    def rando_add_clicker(self):
        self.count[0] = 0
        self.root.ids.add2_screen.ids.add_click_total.text = str(self.count[0])
    # randomize the numbers
        test = MyLayoutAdd()
        n1 = test.gen_num1()
        n2 = test.gen_num2()
        self.count[1] = n1+n2
        combined = f'{str(n1)}+{str(n2)}'
        self.root.ids.add2_screen.ids.add_click_equation.text = str(combined)
    
    def add_clicker(self,num):
        # add the number to the count
        if self.count[0] + num < 0:
            self.count[0] = 0
        else:
            self.count[0] += num
        self.root.ids.add2_screen.ids.add_click_total.text = str(self.count[0])

    def add_clicker_check(self):
        # actual answer
        add2screen_instance = self.root.get_screen('add2')
        raw_answer = add2screen_instance.ids["add_click_equation"].text
        ans = str(int(raw_answer[0]) + int(raw_answer[2]))
        total = add2screen_instance.ids.add_click_total.text
        if (str(total) == ans):
            
            # add points!
            with open('points.txt','r') as file:
                line = file.read().strip()
            old_points = int(line)
            new_points = old_points + 5
            with open('points.txt','w') as file:
                file.write(str(new_points))
            self.root.ids.math_screen.ids.pearls.text = str(new_points)
            
            self.dialog = MDDialog(
                    text = 'Great job! You solved it!',
                    title = 'TREASURE: +5 PEARLS',
                    buttons =[
                        MDRectangleFlatButton(
                        text = 'BACK', on_release = self.close_dialog
                        )
                    ]
                )
            self.dialog.open()
            self.root.transition.direction = 'right'
            self.root.current = 'math'
        else:
            self.dialog = MDDialog(
            text="Almost! Try again :)",
            radius=[20, 7, 20, 7],
            )
            self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
    
    def rando_sub_clicker(self):
        self.sub_count[0] = 0
        self.root.ids.sub2_screen.ids.sub_click_total.text = str(self.count[0])
        print(self.count[0])
    # randomize the numbers
        test = MyLayoutSub()
        n1 = test.gen_num1()
        n2 = test.gen_num2()
        self.sub_count[1] = n1-n2
        combined = f'{str(n1)}-{str(n2)}'
        self.root.ids.sub2_screen.ids.sub_click_equation.text = str(combined)
    
    def sub_clicker(self,num):
        # add the number to the count
        if self.sub_count[0] - num < 0:
            self.sub_count[0] = 0
        else:
            self.sub_count[0] -= num
        self.root.ids.sub2_screen.ids.sub_click_total.text = str(self.sub_count[0])

    def sub_clicker_check(self):
        # actual answer
        sub2screen_instance = self.root.get_screen('sub2')
        raw_answer = sub2screen_instance.ids["sub_click_equation"].text
        print(raw_answer[0])
        print(raw_answer[2])
        ans = str(int(raw_answer[0]) - int(raw_answer[2]))
        total = sub2screen_instance.ids.sub_click_total.text
        if (str(total) == ans):
            
            # add points!
            with open('points.txt','r') as file:
                line = file.read().strip()
            old_points = int(line)
            new_points = old_points + 5
            with open('points.txt','w') as file:
                file.write(str(new_points))
            self.root.ids.math_screen.ids.pearls.text = str(new_points)
            
            self.dialog = MDDialog(
                    text = 'Great job! You solved it!',
                    title = 'TREASURE: +5 PEARLS',
                    buttons =[
                        MDRectangleFlatButton(
                        text = 'BACK', on_release = self.close_dialog
                        )
                    ]
                )
            self.dialog.open()
            self.root.transition.direction = 'right'
            self.root.current = 'math'
        else:
            self.dialog = MDDialog(
            text="Almost! Try again :)",
            radius=[20, 7, 20, 7],
            )
            self.dialog.open()

    def rando_div_clicker(self):
        self.div_count[0] = 0
        self.root.ids.div2_screen.ids.div_click_total.text = str(self.count[0])
        print(self.count[0])
    # randomize the numbers
        test = MyLayoutDiv()
        n1 = test.gen_num1()
        n2 = test.gen_num2()
        self.div_count[1] = n1/n2
        combined = f'{str(n1)}/{str(n2)}'
        self.root.ids.div2_screen.ids.div_click_equation.text = str(combined)
    
    def div_clicker(self,num):
        # add the number to the count
        if self.div_count[0] - num < 0:
            self.div_count[0] = 0
        else:
            self.div_count[0] -= num
        self.root.ids.div2_screen.ids.div_click_total.text = str(self.div_count[0])

    def div_clicker_check(self):
        # actual answer
        div2screen_instance = self.root.get_screen('div2')
        raw_answer = div2screen_instance.ids["div_click_equation"].text
        ans = str(int(raw_answer[0]) // int(raw_answer[2]))
        total = div2screen_instance.ids.div_click_total.text
        if (str(total) == ans):
            
            # add points!
            with open('points.txt','r') as file:
                line = file.read().strip()
            old_points = int(line)
            new_points = old_points + 5
            with open('points.txt','w') as file:
                file.write(str(new_points))
            self.root.ids.math_screen.ids.pearls.text = str(new_points)
            
            self.dialog = MDDialog(
                    text = 'Great job! You solved it!',
                    title = 'TREASURE: +5 PEARLS',
                    buttons =[
                        MDRectangleFlatButton(
                        text = 'BACK', on_release = self.close_dialog
                        )
                    ]
                )
            self.dialog.open()
            self.root.transition.direction = 'right'
            self.root.current = 'math'
        else:
            self.dialog = MDDialog(
            text="Almost! Try again :)",
            radius=[20, 7, 20, 7],
            )
            self.dialog.open()

    def rando_mul_slider(self):
        self.root.ids.mul2_screen.ids.slider_display.text = "0"
        # randomize the numbers
        test = MyLayoutMul()
        n1 = test.gen_num1()
        n2 = test.gen_num2()
        combined = f'{str(n1)}*{str(n2)}'
        self.root.ids.mul2_screen.ids.multiplication_equation.text = str(combined)


    def mul2_check(self):
        mul2_instance = self.root.get_screen('mul2')
        mul_value = mul2_instance.ids["slider_display"].text
        raw_answer = mul2_instance.ids["multiplication_equation"].text
        ans = str(int(raw_answer[0]) * int(raw_answer[2]))
        if mul_value == ans:
            with open('points.txt','r') as file:
                line = file.read().strip()
            old_points = int(line)
            new_points = old_points + 5
            with open('points.txt','w') as file:
                file.write(str(new_points))
            self.root.ids.math_screen.ids.pearls.text = str(new_points)
            
            self.dialog = MDDialog(
                    text = 'Great job! You solved it!',
                    title = 'TREASURE: +5 PEARLS',
                    buttons =[
                        MDRectangleFlatButton(
                        text = 'BACK', on_release = self.close_dialog
                        )
                    ]
                )
            self.dialog.open()
            self.root.transition.direction = 'right'
            self.root.current = 'math'
        else:
            self.dialog = MDDialog(
            text="Almost! Try again :)",
            radius=[20, 7, 20, 7],
            )
            self.dialog.open()


    def add_(self,num):
        # add the number to the count
        if self.count[0] + num < 0:
            self.count[0] = 0
        else:
            self.count[0] += num
        self.root.ids.add2_screen.ids.add.slider_display.text = str(int(self.value))

    def add_clicker_check(self):
        # actual answer
        add2screen_instance = self.root.get_screen('add2')
        raw_answer = add2screen_instance.ids["add_click_equation"].text
        ans = str(int(raw_answer[0]) + int(raw_answer[2]))
        total = add2screen_instance.ids.add_click_total.text
        if (str(total) == ans):
            
            # add points!
            with open('points.txt','r') as file:
                line = file.read().strip()
            old_points = int(line)
            new_points = old_points + 5
            with open('points.txt','w') as file:
                file.write(str(new_points))
            self.root.ids.math_screen.ids.pearls.text = str(new_points)
            
            self.dialog = MDDialog(
                    text = 'Great job! You solved it!',
                    title = 'TREASURE: +5 PEARLS',
                    buttons =[
                        MDRectangleFlatButton(
                        text = 'BACK', on_release = self.close_dialog
                        )
                    ]
                )
            self.dialog.open()
            self.root.transition.direction = 'right'
            self.root.current = 'math'
        else:
            self.dialog = MDDialog(
            text="Almost! Try again :)",
            radius=[20, 7, 20, 7],
            )
            self.dialog.open()
            
            
if __name__ == '__main__':
    HTCApp().run()
