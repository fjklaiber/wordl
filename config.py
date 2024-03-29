
class Config:
    def __init__(self):
        self.exact = dict()
        self.other = dict()
        self.missing = set()

    def add_to_config(self, config):
        for exact in config["exact"].keys():
            self.exact[exact] = config["exact"][exact]
        for other in config["other"].keys():
            self.other[other] = config["other"][other]
        for missing in config["not"].keys():
            self.missing.add(missing)

    def configuration(self):
        config = dict()
        config['not'] = self.missing
        config['other'] = self.other
        config['exact'] = self.exact
        return config

