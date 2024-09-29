**Project Calico**

**Overview:**
An overview of what this does is that we have a dynamic web scraper that is fetching current Pitt events directly from Pitt's calender. We have a python script funeling the data into a JSON file. Then it is pushing these events to our Google breadboard workflow that involves 3 specalists, 2 inputs, 1 output, and a few more components. How our workflow is structured is that it takes our JSON file, containing a list of all upcoming events, as well as an input of the user's interest and then the output is a list of specifically curated event ID numbers. This list is sent back to our webpage and displayed for users to see in a welcoming UI. Then users sugget which events of interest to include into their schedule and download a .ICS file that adds the events they picked to their calender.

**Table Of Contents:**
- Quickstart.py:       Our web scraping python script
- Calico.bgl(1).json:  Google Breadboard Workflow
- Website Page:
      - index.html
      - styles.css
      - script.js
- Getstuff.py:         web API to retrieve event data based on user requirements

**Installation:**
You will need to fork this repository to begin, there is a good amount of embedded dependencies. From there, launch the webpage through the html site and it should be ready to interact with your event type requests!

**Usage:**
If you are a Pitt student or faculty, this is a wonderful resource for you to find ongoing events that cater to your interest. If you are not within the Pitt community and just visiting, this can show you some of the unique things the University of Pittsburgh has to offer for visitors and Pittsburgh locals. Take advantage of this resource to simplify weekend planning!

**Contributors**
Alon Leshan - all296@pitt.edu
Aragya Goyal - arg195@pitt.edu
Eden Brunner - edb67@pitt.edu
Josh Krymgold - jpk114@pitt.edu
