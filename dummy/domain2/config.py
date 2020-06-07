from dummy.config_base import ConfigBase


class Config(ConfigBase):
    def __init__(self, db_path, debug=True):
        super().__init__(db_path=db_path, debug=debug)
        self.field_to_use_in_queries = "domain2"
