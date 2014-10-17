# Initialize the virtual environment if it doesnt exist
if [ -d .env ]; then
    echo "Virtual environment found."
else
    echo "Creating virtual environment."
    virtualenv .env
fi

# Activate the virtual environment
source .env/bin/activate

# Install the required dependencies
pip install -r requirements.txt

export DJANGO_SETTINGS_MODULE=knowyourcongress.settings
