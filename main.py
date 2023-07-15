import json
import requests
from bs4 import BeautifulSoup

url = 'https://vidhyadaan.com/ManageSchool.aspx'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://vidhyadaan.com',
    'Referer': 'https://vidhyadaan.com/ManageSchool.aspx',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

req = requests.get(url, headers=headers)
src = req.text

with open('index.html', 'w') as file:
    file.write(src)

with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

data_dict = []
count = 0

for i in range(2, 102):
    index = str(i).zfill(2) # добавляем ведущий ноль для чисел меньше 10
    shool = soup.find('span', id=f'ctl00_ContentPlaceHolder1_AddU_grddept_ctl{index}_lbldptname').text
    shool_adress = soup.find('span', id=f'ctl00_ContentPlaceHolder1_AddU_grddept_ctl{index}_lblDepartmentAddress').text
    District = soup.find('span', id=f'ctl00_ContentPlaceHolder1_AddU_grddept_ctl{index}_lbldistrictname').text
    Block = soup.find('span', id=f'ctl00_ContentPlaceHolder1_AddU_grddept_ctl{index}_lblblockname').text
    School_timing = soup.find('span', id=f'ctl00_ContentPlaceHolder1_AddU_grddept_ctl{index}_lblDepartmentFromTime').text

    data = {
        'Название школы': shool,
        'Адресс школы': shool_adress,
        'Округ': District,
        'Блокировка': Block,
        'Школьное время': School_timing
    }

    print(f'{count}: is done!')
    count += 1

    data_dict.append(data)

    with open('aaaaa.json', 'w', encoding='utf-8') as json_file:
        json.dump(data_dict, json_file, indent=4, ensure_ascii=False)
