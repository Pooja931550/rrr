import configparser
import os
from Visitbackend.settings import BASE_DIR


class Configuration:
    config = configparser.ConfigParser(interpolation=None)
    config.read(os.path.join(BASE_DIR, 'app/config/config.ini'))
    # print(">>>>>>>>>>>>>>>>", config.sections())
    env = config.get(config.sections()[0], 'Environment')
    # print(">>>>>>>>>>>>>>>>>>>>>>", env)
    def get_Property(key: str) -> str:
        return Configuration.config.get(Configuration.env, key)
