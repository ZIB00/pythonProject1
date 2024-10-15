import os

from kivy.core.audio import SoundLoader
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

from kivy.clock import Clock
from kivy.properties import ObjectProperty, BooleanProperty

from kivymd.material_resources import dp
from kivymd.uix.pickers import (
    MDTimePickerDialVertical,
    MDTimePickerInput
)
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarSupportingText

from datetime import datetime

import random


from docutils.nodes import entry

from kivy.properties import StringProperty


vibration_status_value = False
difficulty_status_value = 'Отсутствует'
number_of_exersice_status_value = 0
on_hour_select_status_value = ''
on_minute_select_status_value = ''
on_am_pm_status_value = ''
on_selector_hour_status_value = 1
on_selector_minute_status_value = 1
time_status_value = ''
smart_alarm = False
alarm_status = False
name = 'eeee'
equal = -1

KV1 = '''
MDScreen:
    md_bg_color: self.theme_cls.secondaryContainerColor
    md_bg_color: self.theme_cls.backgroundColor

    MDTopAppBar:
        type: "small"
        size_hint_x: .99
        pos_hint: {"center_x": .5, "center_y": .95}

        MDTopAppBarTitle:
            text: "Будильник"
            pos_hint: {"center_x": .5}

    MDCard:
        style: "elevated"
        pos_hint: {"center_x": .5, "center_y": .7}
        padding: "4dp"
        size_hint: None, None
        size: "250dp", "40dp"
        elevation_level: 2
        id: alarm1
        on_release: app.show_time_picker_vertical(self)

        MDRelativeLayout:

            MDLabel:
                text: "Время пробуждения"
                adaptive_size: True
                color: "white"
                pos: "5dp", "10dp"

    MDLabel:
        style: "elevated"
        pos_hint: {"center_x": .5, "center_y": .6}
        padding: "4dp"
        size_hint: None, None
        size: "250dp", "60dp"
        theme_shadow_offset: "Custom"
        elevation_level: 2
        id: alarm1
        text: "Умный будильник"
        color: "white"

    MDSwitch:
        pos_hint: {'center_x': .7, 'center_y': .6}
        on_active: app.open_menu_smart(self)


    MDLabel:
        style: "elevated"
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: "4dp"
        size_hint: None, None
        size: "250dp", "60dp"
        theme_shadow_offset: "Custom"
        elevation_level: 2
        id: alarm1
        text: "Сложность задач"

    MDDropDownItem:
        pos_hint: {"center_x": .7, "center_y": .5}
        on_release: app.open_menu_difficulty(self)


        MDDropDownItemText:
            id: drop_text1
            text: " "


    MDLabel:
        style: "elevated"
        pos_hint: {"center_x": .5, "center_y": .4}
        padding: "4dp"
        size_hint: None, None
        size: "250dp", "60dp"
        theme_shadow_offset: "Custom"
        elevation_level: 2
        id: alarm1
        text: "Кол-во задач"

    MDDropDownItem:
        pos_hint: {"center_x": .7, "center_y": .4}
        on_release: app.open_menu_number_of_exersice(self)


        MDDropDownItemText:
            id: drop_text
            text: " "


    MDCard:
        style: "elevated"
        pos_hint: {"center_x": .5, "center_y": .2}
        padding: "4dp"
        size_hint: None, None
        size: "320dp", "60dp"
        theme_shadow_offset: "Custom"
        elevation_level: 2
        on_release: app.on_ok_alert_dialog()
        id: alarm1

        MDRelativeLayout:

            MDLabel:
                text: "Заснуть сейчас"
                adaptive_size: True
                color: "white"
                pos: "90dp", "20dp"
                bold: True

<MDScreen>
'''
KV = KV1

KV2 = '''
MDScreen:
    md_bg_color: self.theme_cls.secondaryContainerColor
    md_bg_color: self.theme_cls.backgroundColor
    GridLayout:
        id: calculator
        display: entry
        rows: 8
        padding: 10
        spacing: 10
        size_hint: .6, .7
        pos_hint: {"center_x": .5, "center_y": .35}



        # Where input is displayed
        BoxLayout:
            Button:
                style: "elevated"
                size_hint: .2, .99
                text: "Выключить"
                on_press: app.examination()
        BoxLayout:
            Label:
                text:
        BoxLayout:
            Label:
                id: label1
                text: app.example()
        BoxLayout:
            TextInput:
                id: entry
                font_size: 16
                multiline: False
                mode: "filled"

        # When buttons are pressed update the entry
        BoxLayout:
            spacing: 10
            Button:
                text: "7"
                on_press: entry.text += self.text
            Button:
                text: "8"
                on_press: entry.text += self.text
            Button:
                text: "9"
                on_press: entry.text += self.text

        BoxLayout:
            spacing: 10
            Button:
                text: "4"
                on_press: entry.text += self.text
            Button:
                text: "5"
                on_press: entry.text += self.text
            Button:
                text: "6"
                on_press: entry.text += self.text

        BoxLayout:
            spacing: 10
            Button:
                text: "1"
                on_press: entry.text += self.text
            Button:
                text: "2"
                on_press: entry.text += self.text
            Button:
                text: "3"
                on_press: entry.text += self.text

        # When equals is pressed pass text in the entry
        # to the calculate function
        BoxLayout:
            spacing: 10

            Button:
                text: "C"
                on_press: entry.text = ""
            Button:
                text: "0"
                on_press: entry.text += self.text
            Button:
                id: button1
                text: "="
                on_press: app.arithmetics(entry.text)
                on_release: entry.text = ''




<MDScreen>
'''


class Example(MDApp):

    def build(self):
        global KV
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    equal_text = StringProperty()
    equal = 0

    def update_screen(self):
        Example().stop()
        Example().run()

    def examination(self):
        global number_of_exersice_status_value
        global KV
        global KV1
        global vibration_status_value
        global difficulty_status_value
        global on_hour_select_status_value
        global on_minute_select_status_value
        global on_am_pm_status_value
        global on_selector_hour_status_value
        global on_selector_minute_status_value
        global time_status_value
        global smart_alarm
        global alarm_status
        global equal
        if number_of_exersice_status_value != 'Отсутствует' and int(number_of_exersice_status_value) != 0:
            self.example()
            self.update_screen()
        else:
            self.sound.stop()
            self.check.cancel()
            KV = KV1
            Example().stop()
            Example().run()
            vibration_status_value = False
            difficulty_status_value = 'Отсутствует'
            number_of_exersice_status_value = 0
            on_hour_select_status_value = ''
            on_minute_select_status_value = ''
            on_am_pm_status_value = ''
            on_selector_hour_status_value = 1
            on_selector_minute_status_value = 1
            time_status_value = ''
            smart_alarm = False
            alarm_status = False
            equal = -1



    def example(self):
        global number_of_exersice_status_value
        global KV
        global KV1
        global vibration_status_value
        global difficulty_status_value
        global on_hour_select_status_value
        global on_minute_select_status_value
        global on_am_pm_status_value
        global on_selector_hour_status_value
        global on_selector_minute_status_value
        global time_status_value
        global smart_alarm
        global alarm_status
        global equal
        if number_of_exersice_status_value != 0:
            operation = random.randint(1, 4)
            if operation == 1:
                if difficulty_status_value == 'Легко':
                    first_number = random.randint(1, 50)
                    second_number = random.randint(1, 50)
                    equal = first_number + second_number
                    return f'{first_number} + {second_number}'
                elif difficulty_status_value == 'Средне':
                    first_number = random.randint(50, 200)
                    second_number = random.randint(50, 200)
                    equal = first_number + second_number
                    return f'{first_number} + {second_number}'
                elif difficulty_status_value == 'Сложно':
                    first_number = random.randint(200, 700)
                    second_number = random.randint(200, 700)
                    equal = first_number + second_number
                    return f'{first_number} + {second_number}'
            elif operation == 2:
                if difficulty_status_value == 'Легко':
                    first_number = random.randint(20, 100)
                    second_number = random.randint(10, 50)
                    while first_number - second_number <= 0:
                        first_number = random.randint(20, 100)
                        second_number = random.randint(10, 50)
                    equal = first_number - second_number
                    return f'{first_number} - {second_number}'
                elif difficulty_status_value == 'Средне':
                    first_number = random.randint(117, 333)
                    second_number = random.randint(53, 245)
                    while first_number - second_number <= 0:
                        first_number = random.randint(117, 333)
                        second_number = random.randint(53, 245)
                    equal = first_number - second_number
                    return f'{first_number} - {second_number}'
                elif difficulty_status_value == 'Сложно':
                    first_number = random.randint(451, 974)
                    second_number = random.randint(385, 888)
                    while first_number - second_number <= 0:
                        first_number = random.randint(451, 974)
                        second_number = random.randint(385, 888)
                    equal = first_number - second_number
                    return f'{first_number} - {second_number}'
            elif operation == 3:
                if difficulty_status_value == 'Легко':
                    first_number = random.randint(1, 9)
                    second_number = random.randint(1, 9)
                    equal = first_number * second_number
                    return f'{first_number} * {second_number}'
                elif difficulty_status_value == 'Средне':
                    first_number = random.randint(5, 20)
                    second_number = random.randint(5, 20)
                    equal = first_number * second_number
                    return f'{first_number} * {second_number}'
                elif difficulty_status_value == 'Сложно':
                    first_number = random.randint(13, 40)
                    second_number = random.randint(13, 40)
                    equal = first_number * second_number
                    return f'{first_number} * {second_number}'
            elif operation == 4:
                if difficulty_status_value == 'Легко':
                    first_number = random.randint(10, 30)
                    second_number = random.randint(2, 15)
                    while first_number / second_number != int(first_number / second_number):
                        first_number = random.randint(10, 30)
                        second_number = random.randint(2, 15)
                    equal = int(first_number / second_number)
                    return f'{first_number} / {second_number}'
                elif difficulty_status_value == 'Средне':
                    first_number = random.randint(30, 100)
                    second_number = random.randint(10, 50)
                    while first_number / second_number != int(first_number / second_number):
                        first_number = random.randint(30, 100)
                        second_number = random.randint(10, 50)
                    equal = int(first_number / second_number)
                    return f'{first_number} / {second_number}'
                elif difficulty_status_value == 'Сложно':
                    first_number = random.randint(100, 300)
                    second_number = random.randint(1, 30)
                    while first_number / second_number != int(first_number / second_number):
                        first_number = random.randint(100, 300)
                        second_number = random.randint(1, 30)
                    equal = int(first_number / second_number)
                    return f'{first_number} / {second_number}'
        else:
            return 'Можете выключить'

    def arithmetics(self, text):
        global equal
        global number_of_exersice_status_value
        if str(equal) == text:
            number_of_exersice_status_value -= 1
            self.example()
            self.update_screen()

    def database(self, ):
        with open('info.txt', 'r+') as f1:
            lines = f1.readlines()

    def notification(self, text):
        MDSnackbar(
            MDSnackbarSupportingText(
                text=text,
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

    def on_edit_time_picker_input(self, time_picker_input):
        time_picker_input.dismiss()
        Clock.schedule_once(self.show_time_picker_vertical, 0.2)

    def show_time_picker_input(self, *args):
        time_picker_input = MDTimePickerInput()
        time_picker_input.bind(on_edit=self.on_edit_time_picker_input)
        time_picker_input.bind(on_hour_select=self.on_hour_select)
        time_picker_input.bind(on_minute_select=self.on_minute_select)
        time_picker_input.bind(on_am_pm=self.on_am_pm)
        time_picker_input.bind(on_selector_hour=self.on_selector_hour)
        time_picker_input.bind(on_selector_minute=self.on_selector_minute)
        time_picker_input.bind(on_cancel=self.on_cancel)
        time_picker_input.bind(on_ok=self.on_ok)
        time_picker_input.bind(on_time_input=self.on_time_input)
        time_picker_input.open()

    def on_edit_time_picker_vertical(self, time_picker_vertical):
        time_picker_vertical.dismiss()
        Clock.schedule_once(self.show_time_picker_input, 0.2)

    def show_time_picker_vertical(self, *args):
        time_picker_vertical = MDTimePickerDialVertical()
        time_picker_vertical.bind(on_edit=self.on_edit_time_picker_vertical)
        time_picker_vertical.bind(on_hour_select=self.on_hour_select)
        time_picker_vertical.bind(on_minute_select=self.on_minute_select)
        time_picker_vertical.bind(on_am_pm=self.on_am_pm)
        time_picker_vertical.bind(on_selector_hour=self.on_selector_hour)
        time_picker_vertical.bind(on_selector_minute=self.on_selector_minute)
        time_picker_vertical.bind(on_cancel=self.on_cancel)
        time_picker_vertical.bind(on_ok=self.on_ok)
        time_picker_vertical.bind(on_time_input=self.on_time_input)
        time_picker_vertical.open()

    def on_hour_select(
            self, time_picker_vertical: MDTimePickerDialVertical, mode: str
    ):
        global on_hour_select_status_value
        on_hour_select_status_value = mode
        # self.notification(f"On {mode} select")

    def on_minute_select(
            self, time_picker_vertical: MDTimePickerDialVertical, mode: str
    ):
        global on_minute_select_status_value
        on_minute_select_status_value = mode
        # self.notification(f"On {mode} select")

    def on_am_pm(
            self, time_picker_vertical: MDTimePickerDialVertical, am_pm: str
    ):
        global on_am_pm_status_value
        on_am_pm_status_value = am_pm
        # self.notification(f"{am_pm.upper()} select")

    def on_selector_hour(
            self, time_picker_vertical: MDTimePickerDialVertical, hour: str
    ):
        global on_selector_hour_status_value
        on_selector_hour_status_value = hour
        # self.notification(f"The value of the hour is {hour} select")

    def on_selector_minute(
            self, time_picker_vertical: MDTimePickerDialVertical, minute: str
    ):
        global on_selector_minute_status_value
        on_selector_minute_status_value = minute
        # self.notification(f"The value of the hour is {minute} select")

    def on_cancel(
            self, time_picker_vertical: MDTimePickerDialVertical
    ):
        time_picker_vertical.dismiss()

    def on_ok(
            self, time_picker_vertical: MDTimePickerDialVertical
    ):
        global time_status_value
        time_status_value = time_picker_vertical.time
        self.notification(f"Time is {time_picker_vertical.time}")
        time_picker_vertical.dismiss()

    def on_time_input(
            self,
            time_picker_vertical: MDTimePickerInput,
            type_time: str,
            value: str,
    ):
        global on_selector_minute_status_value
        global on_selector_hour_status_value
        if type_time == 'hour':
            on_selector_hour_status_value = value
        elif type_time == 'minute':
            on_selector_minute_status_value = value
        # self.notification(f"The {type_time} value is set to {value}")

    def open_menu_smart(self, item):
        global smart_alarm
        if smart_alarm:
            smart_alarm = False
            smart_alarm_text = 'выключён'
        else:
            smart_alarm = True
            smart_alarm_text = 'включён'
        self.notification(f"Умный будильник {smart_alarm_text}")

    def menu_callback_vibration(self, text_item):
        self.root.ids.drop_text.text = text_item

    def open_menu_difficulty(self, item):
        global difficulty_status_value
        menu_items = [
            {
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.menu_callback_difficulty(x),
            } for i in ['Отсутствует', 'Легко', 'Средне', 'Сложно']
        ]
        MDDropdownMenu(
            caller=self.root, items=menu_items
        ).open()

    def menu_callback_difficulty(self, text_item):
        global difficulty_status_value
        self.root.ids.drop_text1.text = text_item
        difficulty_status_value = text_item
        # self.notification(text_item)

    def open_menu_number_of_exersice(self, item):
        menu_items = [
            {
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.menu_callback_number_of_exersice(x),
            } for i in [0, 5, 10, 20]
        ]
        MDDropdownMenu(
            caller=self.root, items=menu_items
        ).open()

    def menu_callback_number_of_exersice(self, text_item):
        global number_of_exersice_status_value
        global difficulty_status_value
        self.root.ids.drop_text.text = text_item
        number_of_exersice_status_value = text_item
        # self.notification(f'Выбрано {text_item} задач')

    def on_ok_alert_dialog(self, *args):
        global smart_alarm
        global number_of_exersice_status_value
        global difficulty_status_value
        global time_status_value
        global alarm_status
        global KV
        global KV2
        number_of_exersice_status_value = int(number_of_exersice_status_value)
        if time_status_value == '':
            self.notification("Выберите время пробуждения")
        elif number_of_exersice_status_value == 0 and difficulty_status_value != 'Отсутствует':
            self.notification("У вас не выбрано количество, но выбрана сложность")
        elif number_of_exersice_status_value != 0 and difficulty_status_value == 'Отсутствует':
            self.notification("У вас не выбрана сложность, но выбрано количество")
            print(number_of_exersice_status_value)
        else:
            alarm_status = True
            KV = KV2
            cycle = 0
            if smart_alarm is True:
                alarmtimeinminute = int(str(time_status_value)[:2])*60+int(str(time_status_value)[3:5])
                nowtimeinminute = datetime.now().hour*60 + datetime.now().minute
                if alarmtimeinminute > nowtimeinminute:
                    minutes = alarmtimeinminute - nowtimeinminute
                else:
                    minutes = alarmtimeinminute + (1440 - nowtimeinminute)
                minutes -= 10
                while minutes - 90 > 0:
                    minutes -= 90
                    cycle += 1
                if 0 <= minutes <= 20 or 70 <= minutes <= 90:
                    time_status_value = time_status_value
                else:
                    minutes = 20
                    minutes += cycle*90
                    if alarmtimeinminute > nowtimeinminute:
                        minutes += nowtimeinminute
                    else:
                        minutes = nowtimeinminute + minutes - 1440
                    hour = minutes//60
                    minute = minutes%60
                    if hour < 10:
                        time_status_value = str(f'0{hour}:')
                    else:
                        time_status_value = str(f'{hour}:')
                    if minute < 10:
                        time_status_value += str(f'0{minute}:00')
                    else:
                        time_status_value += str(f'{minute}:00')
            Example().stop()
            Example().run()
            Example().stop()





    playing = BooleanProperty(False)
    sound = ObjectProperty(
        SoundLoader.load(
            os.path.join('alarm-sounds1', 'sound1.wav'),
        )
    )

    def __init__(self, **kwargs):
        self.check = Clock.schedule_interval(self.time_check, 1)
        self.sound.loop = True
        super().__init__(**kwargs)

    def time_check(self, dt):
        """Check whether the alarm time is equal to the current time."""
        print((str(datetime.now().time()))[:8], time_status_value)
        if (str(datetime.now().time()))[:8] == str(time_status_value) and not self.playing and alarm_status is True:
            print('Ваааау')
            self.playing = True
            self.sound.play()


Example().run()