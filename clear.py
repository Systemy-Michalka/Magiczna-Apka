import os

"""
Jak laguje Wam linux to możliwe, że nie gina wszystkie procesy
Odpalcie sobie wtedy ten skrypt i nie przejmujcie się jak Wam jakieś wyjątki wyrzuca
"""

os.system('killall -9 socat')
os.system('killall -9 python')
