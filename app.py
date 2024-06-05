
import pyautogui as pa
import time

time.sleep(3)

pa.press('win')

pa.PAUSE = 2
pa.write('chrome')

pa.PAUSE = 2
pa.press('enter')

pa.PAUSE = 2
pa.write("youtube.com")

pa.PAUSE = 2
pa.press('ENTER')

pa.PAUSE = 2
pa.click(x=543, y=119)

pa.PAUSE = 2
pa.write("Mashle Opening 2")

pa.PAUSE = 2
pa.press('ENTER')

pa.PAUSE = 2
pa.scroll(-500)

pa.PAUSE = 2
pa.click(x=629, y=251)