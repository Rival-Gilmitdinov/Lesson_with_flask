import requests


# response = requests.post('http://127.0.0.1:5000/calculate', json={"figure1": 10, "figure2": 15, "sign": "+"})
#response = requests.post('http://127.0.0.1:5000/text_redactor', json={"operation": "upper9", "text": "561653dfgdfgfrivagilya@mail.comfdgfjhiughdg" })
# response = requests.post('http://127.0.0.1:5000/calculate', json={"figure1": "number", "text": "561653dfgdfgfrivagilya@mail.comfdgfjhiughdg" })
response = requests.post('http://127.0.0.1:5000/parser', json={"operation": "email", "text": "dsjkfhksdfmamba@yandex.comeffdf"})
print(response)