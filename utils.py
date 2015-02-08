#Simple function for saving a users information in a configfile.
import ConfigParser
import getpass
import keyring
import os
from harvest import Harvest

config = ConfigParser.RawConfigParser()
config.read(os.path.expanduser('~/.harvconfig'))

def set_credentials():
    global config
    print '''PyHarvest needs your username and password to authenticate to Harvest. 
    Your username will be stored in a config file, and password stored in your system's keyring.
    This information will not be communicated anywhere other than your file system and Harvest.'''
    username = raw_input("Username: ")
    password = getpass.getpass()
    URI = "https://" + raw_input("What is the subdomain of your Harvest application?: ") + ".harvestapp.com"

    config.add_section('Harvest')
    config.set('Harvest', 'Username', username)
    config.set('Harvest', 'URI', URI)
    keyring.set_password("Harvest", username, password)
    print "hello"
    with open(os.path.expanduser('~/.harvconfig'), 'wb') as configfile:
        config.write(configfile)
    print "goodbye"

    return (URI, username, password)

def get_credentials():
    global config
    username = config.get('Harvest', 'Username')
    password = keyring.get_password("Harvest", username)
    URI = config.get('Harvest', 'uri')

    return URI, username, password

def get_timesheet():
    try:
        URI, USERNAME, PASSWORD = get_credentials()
    except:
        URI, USERNAME, PASSWORD = set_credentials()

    harvest = Harvest(URI, USERNAME, PASSWORD)
    return harvest 

def get_int(prompt):
    parsed = False
    while parsed == False:
        try:
            answer = int(raw_input(prompt))
            parsed = True
        except ValueError:
            print 'Invalid value!'

    return answer

