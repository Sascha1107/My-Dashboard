import locale
locale.setlocale(locale.LC_ALL, 'de_DE.utf-8')

print(locale.format('%d', 1000000, 1))
