''' display cursor position'''
import pyautogui
print('Press Ctrl-C to quit')
try:
    while True:
        x, y = pyautogui.position()
        position_str = 'X: {} Y: {}'.format(*[str(x).rjust(4) for x in [x, y]])
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
