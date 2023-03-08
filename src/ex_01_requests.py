import requests


# GET Request 보내기
response =  requests.get('https://www.naver.com')
print(response)
print(dir(response))
print(response.status_code)
if response:
    print('Success!')
else:
    print('An error has occurred.')

print(response.headers)
# print(response.content)
# print(response.text)
response.encoding = 'utf-8'
print(response.text)


response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={
        'Accept': 'application/vnd.github.v3.text-match+json',
        'Sender': 'Professor',
        'Org': 'CJU computer security',
        },
)
json_response = response.json()
repository = json_response['items'][0]
print(repository)


response = requests.get(
    'https://www.cju.ac.kr/site/search/search.jsp',
    params={'query': '기숙사'},
    headers={
        'Sender': 'Professor',
        'Org': 'CJU computer security',
    },
)
print(response.text)
# Response를 통해 내가 보낸 Request 확인하기
print(response.request.headers)
print(response.request.headers['Sender'])