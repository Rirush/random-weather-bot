#!/usr/bin/python

import os
import sys


def get_env_variable(variable_name):
    if variable_name in os.environ:
        return os.environ[variable_name]
    else:
        print("You must set {} environment variable.".format(variable_name))
        sys.exit(-1)


API_TOKEN = get_env_variable("TELEGRAM_TOKEN")
ADMIN_ID = get_env_variable("ADMIN_ID")