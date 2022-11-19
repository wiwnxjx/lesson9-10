import requests
response = requests.get('https://uk.wikipedia.org/')
print(type(response.text))
#БІТОК
parse_list = []
response = requests.get('https://coinmarketcap.com/')
response_text = response.text
response_parse = response_text.split('<span>')
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split('</span>'):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                parse_list.append(parse_elem_2)
                print(parse_elem_2)
print("Курс бітка", parse_list[0])

