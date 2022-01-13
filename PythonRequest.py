import requests
import json

# POST 方法
url = "https://mattbotapi20220113.herokuapp.com/mattApi"
payload = {"password": 123, "message": "用 python 測試一下"}
header = {"content-type": "application/json"}
response = requests.post(url, data = json.dumps(payload), headers=header, verify=False)
r_json = response.json()
print(r_json)


# GET方法
url = "https://mattbotapi20220113.herokuapp.com/"
response = requests.get(url)
print(response.text)


# 補充在 git bash 使用 CURL

# GET 方法
# curl https://mattbotapi20220113.herokuapp.com/

# POST 方法
# curl https://mattbotapi20220113.herokuapp.com/mattApi -H "Content-Type: application/json" -d '{"password": 123, "message": "curl test"}' -X POST -v 
# curl https://mattbotapi20220113.herokuapp.com/mattApi -H "Content-Type: application/json" -d @test.json -X POST -v 





