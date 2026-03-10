# podbooking_refactor
Temporary repo for learning and blueprint skeleton for ultimate restructuring of [podbooking main repo](https://github.com/Telsak/podbooking).

# What is podbooking
A solution for a local, self-hosted booking system that was replacing an older php system that ran into issues with LDAP authentication libraries.
It's basically a flask app with an SQLite database and it's served by gunicorn inside a docker container that's hosted behind a generic nginx reverse proxy.

# Plan
- Force myself to build a really simple blueprint structure for a small test project initially
  (right now the /podbooking code is a big mess, a giant .py file that's 1548 lines long with almost everything under the sun in it)
- Get basic testing into the initial code, just to get things running and getting into the habit of writing tests directly
======= ^ ABOVE IS MANDATORY TO BE DONE BEFORE MOVING ON
- Identify the categories of code that's used, and how it can be classified according to the blueprint structure ([digitalocean blog](https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy#the-target-application-structure))
- Build it more modular (like, right now a lot of stuff is hardcoded and/or specific only for our specific usecase at University West) so it can be used by others for similar purposes (booking a resource in a location with user authentication and booking rules)
- Figure out how to handle skillbooking (very specific cisco academy usecase for us locally), maybe make it optional? Module? Plugin??
- Multiple ways of authenticating users, LDAP, ????, etc..
- Cleanup of the routes logic, right now there are a lot of weird hacks all over (string manipulation anyone?)
- Separate html out from python code string variables, see above ^

# Minimum outcome
I'll have played around with basic blueprinting and testing, and hopefully also hooked it up to some neat github actions :)

# ETA
Soon™
