import urllib
import webbrowser
import os 
import time

url = "https://www.codecademy.com/learn/learn-python"
url_1 = "http://www.tutorialspoint.com/python/" 
url_2 = "https://www.codementor.io/community/topic/python"
url_3 = "http://www.pythonchallenge.com/"
url_4 = "https://docs.python.org/3/tutorial/index.html"
url_5 = "https://learnpythonthehardway.org/"
url_6 = "https://www.learnpython.org/"
url_7 = "http://greenteapress.com/thinkpython/html/index.html"
url_8 = "https://docs.python-guide.org/"
url_9 = "https://stackoverflow.com/questions/tagged/python"

chrome_path = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")

os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "open")

time.sleep(2)

webbrowser.get(chrome_path).open(url)
#webbrowser.get(chrome_path).open(url + '/doc')
webbrowser.get(chrome_path).open_new_tab(url_1)
#webbrowser.get(chrome_path).open(url_1 + '/doc')
webbrowser.get(chrome_path).open_new_tab(url_2)
#webbrowser.get(chrome_path).open(url_2 + '/doc')
webbrowser.get(chrome_path).open_new_tab(url_3)
#webbrowser.get(chrome_path).open(url_3 + '/doc')
webbrowser.get(chrome_path).open_new(url_4)
#webbrowser.get(chrome_path).open(url_4 + '/doc')
webbrowser.get(chrome_path).open_new(url_5)
webbrowser.get(chrome_path).open_new(url_6)
webbrowser.get(chrome_path).open_new(url_7)
webbrowser.get(chrome_path).open_new(url_8)
webbrowser.get(chrome_path).open_new(url_9)

