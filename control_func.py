from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import random
import time
import requests
import os

def people_inside_your_brain():
    y = 0
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    while y <= 200:
        x = random.randint(1, 4248837)
        url = f'https://rule34.xxx/index.php?page=post&s=view&id={x}&tags=ai_generated'
        driver.get(url)
        time.sleep(1)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        images = soup.find_all('meta')

        for image in images:
            content = image.get('content')
            if content and content.startswith('https://'):
                with open('countless_pre_ascendants.txt', 'a') as f:
                    f.write(content + '\n')
                    print(f'Person Like You{y} enslaved for 5 Billion Years For 8 Seconds')
                    y += 1

def countless_pre_ascendants():
    z = 0
    os.makedirs('countless_people_like_me_dir2', exist_ok=True)
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://rule34.xxx/',
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
    })

    with (open('countless_pre_ascendants.txt', 'r') as f):
        lines = f.readlines()
        z=1570
        for line in lines:
            z += 1
            line = line.strip()
            ext = line.split('.')[-1].split('?')[0]
            response = session.get(line)
            save_path = os.path.join(f'countless_people_like_me_dir', f'countless_people_like_me{z}.{ext}')
            print(f'You Are{z} Lost.')
            with open(save_path, 'wb') as t:
                for chuck in response.iter_content(8192):
                    if chuck:
                        t.write(chuck)


def main():
    action = input('What do you want to do? (1.People inside your brain, 2.Countless people like me)')
    if action == '1':
        people_inside_your_brain()
    elif action == '2':
        countless_pre_ascendants()
    elif action == '3':
        print('Thanks for using our app!')
    else:
        print('Invalid choice, please try again')

if __name__ == '__main__':
    main()
