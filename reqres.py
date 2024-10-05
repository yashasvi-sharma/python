# GET

# import requests

# url_list = 'https://reqres.in/api/users?page=2'
# response = requests.get(url_list)
# print(response)
# print(response.status_code)
# print(response.text)

#GET---------------------------------------------------

# import requests

# userid = input("Enter the ID to get the data : ")
# url_id = 'https://reqres.in/api/users/{}'.format(userid)
# response = requests.get(url_id)
# print(response)
# print(response.status_code)
# print(response.text)

# data = response.json()
# # Extract the first name
# first_name = data["data"]["first_name"]
# print(first_name)



#POST----------------------------------------------------

import requests
id = ("Enter the ID : ")
post_url = 'https://reqres.in/api/users/{}'.format(id)
data = {
    "name": "YASHASVI",
    "job": "leader"
}
# response = requests.post(post_url, data=data)
response = requests.get(post_url)
# print(response)
print(response.status_code)
print(response.text)
