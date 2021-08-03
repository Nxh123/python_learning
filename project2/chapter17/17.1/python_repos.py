import requests

#执行API调用并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')
#将API响应赋给一个变量
response_dict = r.json()

#处理结果
print(response_dict.keys())