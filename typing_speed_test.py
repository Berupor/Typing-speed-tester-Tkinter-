import tkinter as tk
from tkinter import IntVar, Radiobutton
import webbrowser
from random import choice, shuffle
from PIL import Image, ImageTk


class TypingSpeed:
    def __init__(self):
        self.typed_symbols = 0
        self.words = []
        self.is_work = False
        self.string = 'None'
        self.symbol = window.bind("<Key>", self.handle_keypress)

    def generate_list(self):
        self.words = []
        with open('words.txt', 'r') as file:
            data = file.read()
            data_list = data.split('\n')
            shuffle(data_list)
        for _ in data_list:
            while len(self.words) < 1:
                self.words.append(choice(data_list))
        self.string = ' '.join([str(item) for item in self.words])
        lbl_text_for_typing['text'] = self.string

    def handle_keypress(self, event):
        """ Register typed letters and show message"""
        if event.char == self.string[0] and len(self.string) > 0 and self.is_work:
            self.string = self.string[1:]
            self.typed_symbols += 1
            lbl_typing_status['text'] = ''  # Clear residual text message.
            lbl_text_for_typing['text'] = self.string
        elif event.char != self.string[0] and self.is_work:
            lbl_typing_status['fg'] = 'red'
            lbl_typing_status['text'] = f'{event.char} is Wrong symbol'
        if len(self.string) == 0:
            self.generate_list()

    def timer(self):
        if self.is_work:
            lbl_countdown['text'] -= 1
            if lbl_countdown['text'] > 0:
                lbl_countdown.after(1000, self.timer)
        if lbl_countdown['text'] == 0:
            wpm = self.typed_symbols / 5 / 1
            self.is_work = False
            lbl_typing_status['fg'] = 'green'
            if wpm <= 20:
                grade = 'You typing like my grandma'
            elif 20 < wpm < 50:
                grade = 'Congratulations! You are above average'
            elif wpm >= 50:
                grade = 'You can now be professional typist'
            lbl_typing_status['text'] = f'Your speed: {round(wpm, 1)} WPM. {grade}!'

    def start(self):
        self.is_work = True
        self.timer()
        lbl_countdown['text'] = 60
        self.generate_list()
        btn_start['state'] = 'disabled'

    def clear(self):
        self.is_work = False
        self.words = []
        lbl_typing_status['text'] = ''
        lbl_text_for_typing['text'] = ''
        btn_start['state'] = 'normal'


window = tk.Tk(className='Speed test')
window.geometry("2000x1000")

ts = TypingSpeed()
theme_color = IntVar()


def callback(url):
    webbrowser.open_new(url)


def theme_changer():
    global clock_img
    color = theme_color.get()
    if color == 0:
        main_color = '#FEFBE7'
        text_color = 'black'
        second_color = '#FAF4B7'
        third_color = '#DAE5D0'
    else:
        main_color = '#333F44'
        text_color = 'white'
        second_color = '#37AA9C'
        third_color = '#94F3E4'

    window.configure(bg=main_color)

    frm_head['bg'] = third_color
    frm_buttons['bg'] = main_color
    frm_for_typing['bg'] = second_color

    lbl_head['bg'] = third_color
    lbl_countdown['bg'] = main_color
    lbl_countdown['fg'] = text_color
    lbl_text_for_typing['bg'] = second_color
    lbl_text_for_typing['fg'] = text_color
    lbl_text_to_user['bg'] = second_color
    lbl_typing_status['bg'] = second_color
    lbl_link_1['bg'] = main_color
    lbl_link_2['bg'] = main_color
    lbl_link_1['fg'] = '#639CD9'
    lbl_link_2['fg'] = '#639CD9'

    btn_start['highlightbackground'] = main_color
    btn_clear['highlightbackground'] = main_color
    btn_start['fg'] = text_color
    btn_clear['fg'] = text_color

    rbtn_dark['fg'] = text_color
    rbtn_light['fg'] = text_color
    rbtn_dark['bg'] = main_color
    rbtn_light['bg'] = main_color


image = Image.open('timer.png')
clock_img = ImageTk.PhotoImage(image)

window.configure(bg='#FEFBE7')

window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

frm_head = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=5,
    bg='#DAE5D0',
)
frm_head.pack(pady=(0, 200))
lbl_head = tk.Label(master=frm_head, text="Speed test", font=("Montserrat", 25, 'bold'), bg='#DAE5D0', height=2,
                    width=50)
lbl_head.pack()

frm_buttons = tk.Frame(
    master=window,
    relief=tk.FLAT,
    bg='#FEFBE7',
)
frm_buttons.pack()
btn_start = tk.Button(master=frm_buttons, text='Start', highlightbackground='#FEFBE7',
                      width=5, height=2, command=ts.start)
btn_start.pack(side=tk.LEFT, padx=100, pady=30)
btn_clear = tk.Button(master=frm_buttons, text='Clear', highlightbackground='#FEFBE7',
                      width=5, height=2, command=ts.clear)
btn_clear.pack(side=tk.RIGHT, padx=100, pady=30)

lbl_countdown = tk.Label(master=frm_buttons, text=60, image=clock_img,
                         compound='center', fg='black', font=("Montserrat", 25, 'bold'), bg='#FEFBE7')
lbl_countdown.pack(pady=(0, 10))

frm_for_typing = tk.Frame(master=window, bg='#FAF4B7')
frm_for_typing.pack(fill=tk.X)

frm_for_typing.pack()
lbl_text_to_user = tk.Label(master=frm_for_typing, text='Type it:', font=("Montserrat", 15, 'bold'), bg='#FAF4B7')
lbl_text_to_user.pack(side=tk.TOP, pady=(20, 0))

lbl_typing_status = tk.Label(master=frm_for_typing, text='',
                             font=("Montserrat", 20, 'bold'), bg='#FAF4B7', fg='#FAF4B7')
lbl_typing_status.pack(side=tk.BOTTOM, pady=(0, 50))

lbl_text_for_typing = tk.Label(master=frm_for_typing, text="Click on Start!", height=15, bg='#FAF4B7',
                               fg='black', font=("Montserrat", 18))
lbl_text_for_typing.pack()

lbl_link_1 = tk.Label(master=window, text='Telegram', font=("Montserrat", 25, 'bold'), fg='#639CD9',
                      cursor='hand2', bg='#FEFBE7')
lbl_link_1.pack(side=tk.LEFT, padx=100, pady=30)
lbl_link_1.bind('<Button-1>', lambda e: callback('https://t.me/lackinspiration'))

lbl_link_2 = tk.Label(master=window, text='Kitties', font=("Montserrat", 25, 'bold'), fg='#639CD9',
                      cursor='hand2', bg='#FEFBE7')
lbl_link_2.pack(side=tk.RIGHT, padx=100, pady=30)
lbl_link_2.bind('<Button-1>', lambda e: callback(
    'https://images.unsplash.com/photo-1618813576954-a0958e55e403?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8a2l0 \
    dGllc3xlbnwwfHwwfHw%3D&w=1000&q=80'))

rbtn_light = Radiobutton(master=window, text="Light", command=theme_changer,
                         bg='#FEFBE7', fg='black',
                         variable=theme_color, value=0)
rbtn_light.pack(padx=(0, 500), pady=30, side=tk.RIGHT)
rbtn_dark = Radiobutton(master=window, text='Dark', command=theme_changer,
                        bg='#FEFBE7', fg='black',
                        variable=theme_color, value=1)
rbtn_dark.pack(padx=(500, 0), pady=30, side=tk.LEFT)

window.mainloop()