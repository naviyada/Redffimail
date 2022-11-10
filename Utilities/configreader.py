from configparser import ConfigParser


def ConfigReader(section, Key):
    config = ConfigParser()
    config.read("C:\\training\\BDD\\BDDBehavePOM\\BDDBehavePOM-main\\ConfigurationData\\config.ini")
    return config.get(section, Key)