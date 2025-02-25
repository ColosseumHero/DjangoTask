# DjangoTask
Event Manager

This django application aims to implement the functions of adding events (based on the CRUD principle), registering users and deploying to the server using docker.

This assignment implements several basic models in the events application, namely Event and Category. Category extends and structures the created events by type (zoom_events, meet_events ect.), so there is a direct link between these models.

The implementation of REST-Api for the application is described in detail in the api_documentation.txt file in the root of the project. 

To deploy the application on the server, a dockerfile is added to the project root. It contains clear instructions on how to deploy the application in a virtual environment with the required versions of imported modules.

From additional functions, filtering and searching for events and categories in the administrative panel is implemented. Also added a function to send email messages about event creation to a specific registered user. 