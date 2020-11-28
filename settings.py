import configparser


def getVal(val, local):
    config = configparser.ConfigParser()
    config.read("storage.ini")
    return config[local][val]

def setVal(val, local, newVal):
    config = configparser.ConfigParser()
    config.read("storage.ini")
    config[local][val] = newVal

    with open('storage.ini', 'w') as configfile:
        config.write(configfile)