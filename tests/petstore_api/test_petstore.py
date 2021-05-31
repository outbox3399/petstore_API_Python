import json
import pytest
import requests
import csv
import zulu
from datetime import datetime

from src.utilities.generic_utilities import *
from src.utilities.resource_uri import *
from src.utilities.configurations import *
from src.payloads.pet_payload import *
from src.payloads.store_payload import *


@pytest.mark.tcid01
def test_addition_deletetion_of_a_pet(jsonPetResponse=None, getPetResponse=NoneNone):
    getPetstoreUrl = getConfig()['BASEURL']['baseurl'] + ApiResourcesURI.postPet
    header = {'Content-Type': 'application/json'}
    petBody = add_new_pet_to_store("jacky", "available")

    # adding pet to store
    post_pet_details(getPetstoreUrl, header, petBody)
    # getPetResponse = requests.post(getPetstoreUrl, headers=header, json=petBody)
    #jsonPetResponse = json.loads(getPetResponse.text)
    petID = jsonPetResponse['id']
    print("The Pet ID is : ", petID)
    assert getPetResponse.status_code == 200

    # deleting pet with particular ID
    '''deletePetUrl = getConfig()['BASEURL']['baseurl'] + ApiResourcesURI.deletePet + format(str(petID))
    deleteResponse = requests.delete(deletePetUrl, headers=header)
    print("The Pet is successfully deleted with response code 200")
    assert deleteResponse.status_code == 200

    # validate the pet got deleted
    getPetIDUrl = getConfig()['BASEURL']['baseurl'] + ApiResourcesURI.getPetByID + format(str(petID))
    header = {'Content-Type': 'application/json'}
    getPetIDResponse = requests.get(getPetIDUrl, headers=header, )
    print("********** The pet is not available after successful delete with response code 404 **********")
    assert getPetIDResponse.status_code == 404 '''


@pytest.mark.tcid02
def test_get_total_available_pets():
    getPetstoreUrl = getConfig()['BASEURL']['baseurl'] + ApiResourcesURI.postPet
    header = {'Content-Type': 'application/json'}
    petBody = add_new_pet_to_store("jacky", "available")

    # adding pet to store
    getPetResponse = requests.post(getPetstoreUrl, headers=header, json=petBody)
    jsonPetResponse = json.loads(getPetResponse.text)
    print("The added pet is : ", json.dumps(jsonPetResponse, indent=4))
    petID = jsonPetResponse['id']

    # finding the status of the pet added as available
    if jsonPetResponse['id'] == petID and jsonPetResponse['status'] == "available":
        print("********** The status of the pet is AVAILABLE **********")

    # getting count of total available pets
    getStatusUrl = getConfig()['BASEURL']['baseurl'] + ApiResourcesURI.getPetStatus
    header = {'Content-Type': 'application/json'}
    param = {'status': 'available'}
    getPetStatusResponse = requests.get(getStatusUrl, params=param, headers=header, )
    jsonGetPetStatusResponse = json.loads(getPetStatusResponse.text)
    countAfterAdding = 0
    for stats in jsonGetPetStatusResponse:
        if stats['status'] == 'available':
            countAfterAdding += 1
    print("********** The total count after adding a pet is : **********", countAfterAdding)

    # deleting the pet recently added
    deleteRecentPetUrl = getConfig()['BASEURL']['baseurl'] + ApiResourcesURI.deletePet + format(str(petID))
    deleteRecentResponse = requests.delete(deleteRecentPetUrl, headers=header)
    assert deleteRecentResponse.status_code == 200

    # getting count of total available pets after recent deletion
    getPetStatusResponse = requests.get(getStatusUrl, params=param, headers=header, )
    jsonGetPetStatusResponse = json.loads(getPetStatusResponse.text)
    countAfterDeleting = 0
    for stats in jsonGetPetStatusResponse:
        if stats['status'] == 'available':
            countAfterDeleting += 1
    print("********** The total count after deleting a pet is : **********", countAfterDeleting)

    # checking if the total pet count is reduced by 1
    if countAfterDeleting == countAfterAdding - 1:
        print("Total pet count is same as initial count")
    else:
        print("********** Total pet count is not same as initial count **********")
    assert countAfterDeleting == countAfterAdding - 1



@pytest.mark.tcid03
def test_adding_multiple_pets():
    zuluTime = zulu.now()
    zuluDateTime = str(zuluTime).replace('+00:00', 'Z')

    # get counts of total available pets before adding
    getStatusUrl = getConfig()['BASEURL']['baseurl'] + ApiResourcesURI.getPetStatus
    header = {'Content-Type': 'application/json'}
    param = {'status': 'available'}
    getPetStatusResponse = requests.get(getStatusUrl, params=param, headers=header, )
    jsonGetPetStatusResponse = json.loads(getPetStatusResponse.text)
    countBeforeAdding = 0
    for stats in jsonGetPetStatusResponse:
        if stats['status'] == 'available':
            countBeforeAdding += 1
    print("********** The total pet count before adding is : **********", countBeforeAdding)
    # print("ALl pets are : ", json.dumps(jsonGetPetStatusResponse, indent=4))

    # adding pet to store
    getPetstoreUrl = getConfig()['BASEURL']['baseurl'] + ApiResourcesURI.postPet
    contHeader = {'Content-Type': 'application/json'}
    with open("F:/All Desktop/petstore/PetStoreAPIAutomation/tests/resources/petstore.csv") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        header = next(csvReader)
        if header is not None:
            name = []
            status = []
            quantity = []
            allPetIDs = []
            for row in csvReader:
                name.append(row[0])
                status.append(row[1])
                quantity.append(row[2])
                for names in name:
                    petBody = add_new_pet_to_store(names, 'available')
                    getPetResponse = requests.post(getPetstoreUrl, headers=contHeader, json=petBody)
                    jsonPetResponse = json.loads(getPetResponse.text)
            # print("The added pet is : ", json.dumps(jsonPetResponse, indent=4))
                petID = jsonPetResponse['id']
                allPetIDs.append(petID)
            print("********** ALl pet id's are : **********", allPetIDs)

    # finding status of the pet added as available
            if jsonPetResponse['id'] == petID and jsonPetResponse['status'] == "available":
                print("********** The status of the pet is AVAILABLE **********")

    # get count of total available pets after adding
    getStatusUrl = getConfig()['BASEURL']['baseurl'] + ApiResourcesURI.getPetStatus
    header = {'Content-Type': 'application/json'}
    param = {'status': 'available'}
    getPetStatusResponse = requests.get(getStatusUrl, params=param, headers=header, )
    jsonGetPetStatusResponse = json.loads(getPetStatusResponse.text)
    countAfterAdding = 0
    for stats in jsonGetPetStatusResponse:
        if stats['status'] == 'available':
            countAfterAdding += 1
    print("********** The total count of pets after adding are : **********", countAfterAdding)

    # delete all the pets recently added
    for dele in allPetIDs:
        deleteAllRecentPetUrl = getConfig()['BASEURL']['baseurl'] + ApiResourcesURI.deletePet + format(str(dele))
        deleteRecentResponse = requests.delete(deleteAllRecentPetUrl, headers=header)
    print("********** All pet id's are deleted successfully with status code 200 **********")
    assert deleteRecentResponse.status_code == 200

    # get count of total available pets after delete
    getStatusUrl = getConfig()['BASEURL']['baseurl'] + ApiResourcesURI.getPetStatus
    header = {'Content-Type': 'application/json'}
    param = {'status': 'available'}
    getPetStatusResponse = requests.get(getStatusUrl, params=param, headers=header, )
    jsonGetPetStatusResponse = json.loads(getPetStatusResponse.text)
    countAfterDeleting = 0
    for stats in jsonGetPetStatusResponse:
        if stats['status'] == 'available':
            countAfterDeleting += 1
    print("Total pets after deleting are: ", countAfterDeleting)
    if countBeforeAdding == countAfterDeleting:
        print("Total pet count is same as initial count")
    else:
        print("********** Total pet count is not same as initial count **********")

    # order a pet
    getPetOrderUrl = getConfig()['BASEURL']['baseurl'] + ApiResourcesURI.postOrderPet
    contentHeader = {'Content-Type': 'application/json'}
    for quan in quantity:
        petOrderBody = palce_order_for_pet(zuluDateTime, quan)
        getPetOrderResponse = requests.post(getPetOrderUrl, headers=contentHeader, json=petOrderBody)
        jsonPetOrderResponse = json.loads(getPetOrderResponse.text)
    print("********** The pet has been ordered successfully with status code 200 **********")
    assert getPetOrderResponse.status_code == 200
    assert jsonPetOrderResponse['status'] == 'placed'

    # get total count of pets with “shipDate” as current date
