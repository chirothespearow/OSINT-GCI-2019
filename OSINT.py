import requests
import urllib.request
import time
from bs4 import BeautifulSoup
user=input('Please enter username:')
insta_url = 'https://www.instagram.com/'+user+'/'
reddit_url= 'https://github.com/'+user
twitter_url='https://twitter.com/'+user

def checker(a,url):
    response = requests.get(url)
    html_page = response.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    if a==1:
        if "Sorry, this page isn't available." in text:
            print('This user is not on Instagram.')
        else:
            print('User present on Instagram')
    elif a==2:
        if 'Not Found' in text:
            print('User is not on Github')
        else:
            print('User present on Github')
    elif a==3:
        if 'Sorry, that page doesn’t exist!' in text:
            print('User is not on Twitter')
        else:
            print('User present on Twitter')

checker(1,insta_url)
checker(2,reddit_url)
checker(3,twitter_url)
    
        
