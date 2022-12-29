import pynput.mouse as mouse
from pynput.mouse import Button
import pynput.keyboard as keyboard
from pynput.keyboard import Key
import logging, coloredlogs
import pyfiglet
from sys import exit
import time

logging.basicConfig(level=logging.DEBUG, format='%(message)s',)

coloredlogs.install(level=('DEBUG'), fmt='%(message)s')

class autoclicker:

    key = None

    start = Key.f9
    pause = Key.f10
    stop = Key.f11

    def menu(self):
        figlet = pyfiglet.figlet_format('AUTOCLICKER')
        logging.warning(f'{figlet}')
        logging.debug('Start program:f9')
        logging.debug('Pause program:f10')
        logging.debug('Close Program:f11')


    def on_press(self, key):
        self.key = key

    def start_listening(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        self.menu()

        msg_db = 0

        while True:

            while True:

                if self.key == self.stop:
                    exit()

                elif self.key == self.pause:
                    while not self.key == self.start and not self.key == self.stop:
                        time.sleep(0.01)
                    
                    if self.key == self.start:
                        logging.error('Autoclier: ON')

                elif self.key == self.start:
                    while not self.key == self.pause and not self.key == self.stop:
                        controll = mouse.Controller()
                        time.sleep(0.001)
                        controll.click(button=Button.left)
                    if self.key == self.pause:
                        logging.error('Autoclicker: OFF')


if __name__ == '__main__':
    click = autoclicker()
    click.start_listening()















