from pathlib import Path

from dummy.config_base import ConfigBase


class Config(ConfigBase):
    def __init__(self, debug=True):
        super().__init__(debug=debug)
        self.db_path = Path(__file__).parent.resolve() / "../../www/domain1.db"
        self.field_to_use_in_queries = "domain1"
