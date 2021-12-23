"""
Definitions of the mapping from excel to pandas columns.

Template:

Name = Client(
    incident_mapping = {
        'id': '',
        'location': '',
        'description': '',
        'injury-severity': '',
        'incident-type': ''
    },

    factor_mapping = {
        'id': '',
        'factor-level': '',
        'factor-text': ''
    },

    action_mapping = {
        'id': '',
        'action-id': ''
    }
)
"""

from collections import namedtuple

Client = namedtuple('Client', ['incident_mapping', 
                               'factor_mapping', 
                               'action_mapping'])

Geotec = Client(
    incident_mapping = {
        'id': 'A',
        'location': 'C',
        'description': 'G',
        'injury-severity': 'S',
        'incident-type': 'K'
    },

    factor_mapping = {
        'id': 'A',
        'factor-level': 'B',
        'factor-text': 'C'
    },

    action_mapping = {
        'id': 'J',
        'action-id': 'A'
    }
)

# Border doesn't seem to link actions to incidents, so can't be modelled.
# Removing the numeric predictive model would allow us to predict this client.
Border = Client(
    incident_mapping = {
        'id': 'A',
        'location': 'C',
        'description': 'H',
        'injury-severity': 'K',
        'incident-type': 'E'
    },

    factor_mapping = {
        'id': 'A',
        'factor-level': 'D',
        'factor-text': 'F'
    },

    action_mapping = {
        'id': None,
        'action-id': 'A'
    }
)

# Warak's dataset is insufficient for modelling
Warak = Client(
    incident_mapping = {
        'id': 'A',
        'location': 'D',
        'description': 'H',
        'injury-severity': 'T',
        'incident-type': 'L'
    },

    factor_mapping = {
        'id': 'A',
        'factor-level': 'E',
        'factor-text': 'F'
    },

    action_mapping = {
        'id': 'H',
        'action-id': 'A'
    }
)
