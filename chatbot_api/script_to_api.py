# import requests

# url = "http://localhost:8000/chatbot/bot-responses/"

# response = requests.get(url)

# # print(response.json())

# data  = response.json()
# dict_list = []
# for each in data:
#     # splitted_words = each[2].split(",")
#     eacha = dict(each)
#     dict_list.append(eacha)

# for each in dict_list:
#     print(each.get("user_input"))
user_input='abc, def, ghi, jkl'
result_list = [item.strip() for item in user_input.split(',')]
print(result_list)