import urllib
import webbrowser
import os #alteration
import time



print("         _             _     _      _        _                  _        ")
print("        /\ \     _    /\ \ /_/\    /\ \     /\_\               / /\      ")
print("       /  \ \   /\_\ /  \ \\ \ \   \ \_\   / / /         _    / /  \     ")
print("      / /\ \ \_/ / // /\ \ \\ \ \__/ / /   \ \ \__      /\_\ / / /\ \__  ")
print("     / / /\ \___/ // / /\ \_\\ \__ \/_/     \ \___\    / / // / /\ \___\ ")
print("    / / /  \/____// /_/_ \/_/ \/_/\__/\      \__  /   / / / \ \ \ \/___/ ")
print("   / / /    / / // /____/\     _/\/__\ \     / / /   / / /   \ \ \       ")
print("  / / /    / / // /\____\/    / _/_/\ \ \   / / /   / / /_    \ \ \      ")
print(" / / /    / / // / /______   / / /   \ \ \ / / /___/ / //_/\__/ / /      ")
print("/ / /    / / // / /_______\ / / /    /_/ // / /____\/ / \ \/___/ /       ")
print("\/_/     \/_/ \/__________/ \/_/     \_\/ \/_________/   \_____\/        ")
                                                                         
print("SEARCH TOPICS: Python, Cyber, News, Misc")


myUrlDB = {
    "https://www.csis.org/programs/cybersecurity-and-governance/technology-policy-program/other-projects-cybersecurity": [ "cyber", "news"],
    "http://www.enterthecore.net": ["misc"],
    "https://www.soylentnews.org/": ["news"],
    "https://blog.erratasec.com/": ["cyber", "news"],
    "https://threatpost.com/": ["cyber", "news"],
    "https://securityboulevard.com/": ["cyber", "news"],
    "https://nakedsecurity.sophos.com/": ["cyber", "news"],
    "https://securityweekly.com/": ["cyber", "news"],
    "https://blogs.akamai.com/": ["cyber", "news"],
    "https://securityledger.com/": ["cyber", "news"],
    "https://www.grahamcluley.com/": ["cyber", "news"],
    "https://threatmap.checkpoint.com/ThreatPortal/livemap.html": ["cyber", "news"],
    "https://www.fireeye.com/cyber-map/threat-map.html": ["cyber", "news"],
    "https://www.codecademy.com/learn/learn-python": ["python"],
    "http://www.tutorialspoint.com/python/": ["python"],
    "https://www.codementor.io/community/topic/python": ["python"],
    "http://www.pythonchallenge.com/": ["python"],
    "https://docs.python.org/3/tutorial/index.html": ["python"],
    "https://learnpythonthehardway.org/": ["python"],
    "https://www.learnpython.org/": ["python"],
    "http://greenteapress.com/thinkpython/html/index.html": ["python"],
    "https://docs.python-guide.org/": ["python"],
    "https://stackoverflow.com/questions/tagged/python": ["python"],
    "https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Payloads": ["misc"],
    "https://www.hackerone.com/": ["misc"],
    "https://projecteuler.net/": ["misc"],
    "https://machinelearningmastery.com/machine-learning-in-python-step-by-step/": ["misc"],
    "https://www.reddit.com/r/Python/": ["misc"],
    "https://www.reddit.com/r/cybersecurity/": ["misc"],
    }       


    
    
chrome_path = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")

os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "open")

time.sleep(2)


browser = webbrowser.get(chrome_path)
tagName = input()
myUrls = []

for url in myUrlDB.keys():
    if tagName in myUrlDB[url]:
        myUrls.append(url)



for url in myUrls:
    browser.open(url)



