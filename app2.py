from sites.app import create_app
from sites.domain2.config import Config

if __name__ == "__main__":
    app = create_app(Config)
    app.run()
