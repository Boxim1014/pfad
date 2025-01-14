from bs4 import BeautifulSoup
import requests

url = 'https://www.dearmoney.com.tw/eightwords/result_eight_words_page'

data = {
    '_Year': 1999,
    '_Month': 11,
    '_Day': 17,
    '_Hour': 13,
    '_sex': 'M',
    '_earth': 'N',
    '_method': 'A'
}

headers = {
    'User-Agent': 'Mozilla/5.0'
}

response = requests.post(url, data=data, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找 <font> 标签，颜色为 #111111
    font_elements = soup.find_all('font', color='#111111')
    for element in font_elements:
        print(element.get_text(strip=True))

    # 查找 <div> 标签，类名为 'row m-0 justify-content-center mt-5 mb-3'
    div_elements = soup.find_all('div', class_='row m-0 justify-content-center mt-5 mb-3')
    for element in div_elements:
        text = element.get_text(strip=True)
        if "◎開運方法" in text:
            # 提取并打印“◎開運方法行業選擇：”后面的文字
            index = text.find("◎開運方法")
            result = text[index + len("◎開運方法"):]
            print("開運方法", result)

else:
    print(f"请求失败，状态码：{response.status_code}")