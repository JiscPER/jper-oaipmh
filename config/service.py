##################################################
# overrides for the webapp deployment

DEBUG = True
PORT = 5000
SSL = False
THREADED = True

############################################
# important overrides for the ES module

# elasticsearch back-end connection settings
ELASTIC_SEARCH_HOST = "http://localhost:9200"
ELASTIC_SEARCH_INDEX = "db"
ELASTIC_SEARCH_VERSION = "1.4.4"

# Classes from which to retrieve ES mappings to be used in this application
ELASTIC_SEARCH_MAPPINGS = []

############################################
# important overrides for account module

ACCOUNT_ENABLE = False
SECRET_KEY = "super-secret-key"

############################################
## JPER Client information

# Base URL for requests to the JPER API
JPER_BASE_URL = "http://router.jisc.ac.uk/api/v1"

# API key to use for authenticated requests against JPER API
JPER_API_KEY = ""