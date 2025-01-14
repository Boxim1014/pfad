import requests
from bs4 import BeautifulSoup

url = 'https://www.dearmoney.com.tw/eightwords/result_eight_words_page'

data = {
    '_Year': 1999,
    '_Month': 11,
    '_Day': 17,
    '_Hour': 13,
    '_sex': 'M',  # 假设 'F' 表示女性
    '_earth': 'N',  # 北半球
    '_method': 'A'  # 子初换日
}

headers = {
    'User-Agent': 'Mozilla/5.0'
}

response = requests.post(url, data=data, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # 根据实际的HTML结构调整选择器
    result_section = soup.find_all('div', class_='alert alert-warning')  # 示例选择器
    for result in result_section:
        if result:
            print("批算结果：")
            print(result.text.strip())
        else:
            print("未找到结果部分。")
else:
    print(f"请求失败，状态码：{response.status_code}")