from configparser import ConfigParser

# read configuraton file
def read_config(config_file='config.ini'):
    config = ConfigParser()
    config.read(config_file)
    return config