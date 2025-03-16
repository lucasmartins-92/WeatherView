# WEATHER VIEW
#### Video Demo:  <URL HERE>
#### Description:
"Weather View" is a simple program that allows users to view current weather information from anywhere in the world, thanks to the Google Maps Geocoding API. The project is based on Python Flask, HTML, CSS, JavaScript and SQLite. The inspiration for this project came to me when I was planning a trip to several European countries, and I noticed that a relevant issue at every stop was the weather and its impact on route choice and luggage planning.

The tool's main mechanism converts the user's text search into latitude and longitude coordinates and retrieves the formal name of the location, using the Google Maps Geocoding API. This API was chosen because Google Maps is the most popular and powerful tool for users to carry out this type of work, as well as allowing fuzzy searching, which made everything much easier for me.

Latitude and longitude are used to search for weather-related information using the Weather Forecast API from the open-meteo.com website. Once again with practicality and ease in mind, this API was chosen because it is free to use and provides data in a simple way, with fields written out in full and values that are easy to understand and customize.

Once the information has been gathered, the user is presented with a page with the desired result: current temperature, maximum and minimum temperatures for the day, and weather conditions (such as rain, fog, snow, etc.). From there, the user can return to the index and perform another search.

The tool's greatest complexity, however, comes from the account creation system. Based on SQLite, it allows the registered and logged-in user to view their search history and also save searches for easy future access. Saved searches can also be deleted easily with a single click. The search history list also allows the user to save any of them with a single click. The system supports multiple users, each with their own history and saved searches.

The account system consists of three tables: users, saved, and history. "history" records not only the latitude, longitude and name of the location searched, but also the day and time the search was made, so that the user can view queries organized by the most recent. "saved", in turn, records a unique hash for each stored location. This is done to prevent duplicate searches from being recorded.

Needless to say, this system requires several presentation alternatives for each of the tool's public pages, since logged-in users have access to many more tools than logged-out visitors. This was possible thanks to Flask, Jinja, Javascript and pure Python resources, performing check functions and passing variables back and forth to check whether the user already has an account and, if so, whether their list of saved searches contains any items, as well as whether the search performed is already on this list.

Through different implementations of GET and POST methods, the system seeks to avoid redundancies by reducing the number of functions needed to perform the same operations. Each page is linked to related functions, and the code has been optimized with various checks during execution to reduce the load on the server and the user's browser. It was also essential to use Jinja tools to dynamically reduce or extend the code executed, since logged-out users don't see many resources that would cause unnecessary load.

The basic structure of each page was organized in HTML with dynamic modules provided with Jinja. A little Javascript was needed to modulate the behavior of certain input elements, in particular to prevent users from saving searches with an empty name field. The APIs were accessed with Python, and the basic functions of each page were built with Flask to handle the necessary functions and variables.

In general, I tended to use Flask and Jinja even when Javascript was a viable option for the situation, as I was more familiar with Pythonian syntax and operation. Even so, it became clear during development that almost all the operations performed could be approached from many angles and solved with various tools. 