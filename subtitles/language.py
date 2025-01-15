import requests

def translate(keyword):
    url = "https://translate.kakao.com/translator/translate.json"
    headers = {
        "Origin": "https://translate.kakao.com",
        "Referer": "https://translate.kakao.com/",
        "User-Agent": "Mozilla/5.0",
    }
    data = {
        "queryLanguage": "en",
        "resultLanguage": "kr",
        "q": keyword
    }
    resp = requests.post(url, headers=headers, data=data)
    result = resp.json()
    return result['result']['output'][0][0]