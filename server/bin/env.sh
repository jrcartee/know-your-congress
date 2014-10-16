# Initialize and activate the virtual environment
if [ -d .env ]; then
    echo "Virtual environment found."
else
    echo "Creating virtual environment."
    virtualenv .env
fi

source .env/bin/activate
pip install -r requirements.txt

export DJANGO_SETTINGS_MODULE=knowyourcongress.settings
