
import numpy as np
from faker import Faker
import requests
import json
URL = "http://127.0.0.1:8000/student/studentcreate/"

fake = Faker()
ph = fake.numerify('##########')


def postdata(num):
    for i in range(num):
        data = {
            "schoolId": 1,
            "classId": "97680437",
            "name": fake.name(),
            "phone": ph,
            "email": fake.email(),
            "gender": np.random.choice(["Male", "Female"]),
            "dob": fake.date(),
            "address": fake.address(),
            "admissionDate": fake.date(),
            # "profilePhoto": "NULL"
        }
        header = {'content-Type': 'application/json'}
        # print(data)
        json_data = json.dumps(data)

        r = requests.post(url=URL, headers=header, data=json_data)
        data = r.json()
        print(data)


postdata(5)

# def getdata(id=None):
#     data = {}
#     header = {'content-Type': 'application/json'}
#     if id is not None:
#         data = {'id': id}

#     json_data = json.dumps(data)
#     r = requests.get(url=URL, headers=header, data=json_data)
#     data = r.json()
#     print(data)


# getdata(4)


# def postdata():
#     data = {
#         'name': 'taruno',
#         'roll': 575,
#         'city': 'kapodraa'
#         # "schoolId": 3,
#         # "classId": "54607454",
#         # "name": "Somya Rudra",
#         # "phone": "7412369856",
#         # "email": "somya@gmail.com",
#         # "gender": "Male",
#         # "dob": "2022-08-22",
#         # "address": "dvbnm, fghjk, fghjkl-456",
#         # "admissionDate": "2022-08-22"
#     }
#     header = {'content-Type': 'application/json'}
#     print(data)
#     json_data = json.dumps(data)

#     r = requests.post(url=URL, headers=header, data=json_data)
#     data = r.json()
#     print(data)


# postdata()


# def updatedata():
#     data = {
#         'id': 5,
#         'name': 'tarun',
#         # 'roll': 21,
#         'city': 'Mumbaiiii'
#     }
#     header = {'content-Type': 'application/json'}
#     json_data = json.dumps(data)
#     r = requests.put(url=URL, headers=header, data=json_data)
#     data = r.json()
#     print(data)


# # updatedata()


# def deletedata():
#     data = {
#         'id': 3,
#     }
#     header = {'content-Type': 'application/json'}
#     json_data = json.dumps(data)
#     r = requests.delete(url=URL, headers=header, data=json_data)
#     data = r.json()
#     print(data)


# # deletedata()
