# CentralServer

## Requirements
- Python > 3.6
- virtualenv
- MQTT broker (for example Mosquitto)

## Installatie
```bash
# Create an isolated environment
virtualenv --no-site-packages -p $(which python3) venv

# Activate isolated environment
source venv/bin/activate

# Install packages
pip3 install setuptools

# Install dependencies
python setup.py develop
```

## Unit tests
Alle logica in dit project kan worden getest met behulp van unit tests. Deze bevinden zich in de `/algorithm_client/test`
map. De test kunnen worden uitgevoerd met het commando
```bash
python -m unittest
```

## MQTT
Om gebruik te maken van een lokale MQTT broker kunnen de volgende instellingen in `development.ini` aangepast worden:
```bash
mqtt.hostname = localhost
mqtt.port = 1883
```