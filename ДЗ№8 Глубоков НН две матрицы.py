import time
import locale
locale.setlocale(locale.LC_ALL, '')
print(time.strftime('Сегодня: %B %d %Y', time.localtime()))