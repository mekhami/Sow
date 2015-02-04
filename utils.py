#Simple function for saving a users information in a configfile.
import ConfigParser
import getpass

def set_credentials():
    print '''PyHarvest needs your username and password to authenticate to Harvest. 
    This information will be stored in a config file and is not 
    communicated anywhere other than your file system and Harvest.'''
    username = raw_input("Username: ")
    password = getpass.getpass()
    URI = "https://" + raw_input("What is the subdomain of your Harvest application?: ") + ".harvestapp.com"

    config = ConfigParser.RawConfigParser()
    config.add_section('Harvest')
    config.set('Harvest', 'Username', username)
    config.set('Harvest', 'Password', password)
    config.set('Harvest', 'URI', URI)

    with open('.harvconfig', 'wb') as configfile:
        config.write(configfile)

    return (URI, username, password)
