import csv

import requests


def open_file_read_data(filepath):
    with open(filepath) as fileReader:
        csvReader = csv.reader(fileReader, delimiter=',')
        header = next(csvReader)
        if header is not None:
            name = []
            status = []
            quantity = []
            for row in csvReader:
                name.append(row[0])
                status.append(row[1])
                quantity.append(row[2])
            # print(name)
            # print(status)
            # print(quantity)


def post_pet_details(url, headers=None, json=None):
    getPetResponse = requests.post(url, headers, json)
    jsonPetResponse = json.loads(getPetResponse.text)
    return jsonPetResponse
