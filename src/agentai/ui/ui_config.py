from configparser import ConfigParser


class Config:
    def __init__(self, config_file="./src/agentai/ui/ui_config.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_configs(self, config_name):
        return self.config["DEFAULT"].get(config_name).split(", ")
