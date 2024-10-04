from app import create_app
from config import Config
from app.seed import seed

app = create_app(Config)

# register custom command for seed
app.cli.add_command(seed)

if __name__ == '__main__':
    app.run(debug=True)