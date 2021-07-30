"""
This file calls all of the other python files that will be referenced for the multiapp function
"""

from multiapp import MultiApp
from apps import login

application = MultiApp()

# add the login page as initial nav option
application.add_app('Login', login.app)




# run application
application.run()












