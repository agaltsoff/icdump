import base_master
import base_developer
import base_dump as base_dump

def get_base_connect_str(params):
    return '%s /N "%s" /P "%s" /ConfigurationRepositoryF "%s" /ConfigurationRepositoryN "%s" /ConfigurationRepositoryP ""'%(params.location, params.username, params.password, params.depot_location, params.depot_username)

def get_gear(ver):
    return '"C:\\Program Files (x86)\\1cv8\\%s\\bin\\1cv8.exe" DESIGNER /DisableStartupMessages'%(ver)

GEAR= get_gear('8.3.12.1567')

BASE_MASTER= get_base_connect_str(base_master)

BASE_DEVELOPER= get_base_connect_str(base_developer)


