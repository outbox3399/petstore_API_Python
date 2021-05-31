import configparser

def getConfig():
    config = configparser.ConfigParser()
    config.read('F:/All Desktop/petstore/PetStoreAPIAutomation/src/utilities/properties.ini')
    return config


