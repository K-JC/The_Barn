#  The Barn
The Barn Restaurant is a fictional restaurant and not a real one. 

The link to the live site can be found here, enjoy! - [The Barn]() Enjoy!
![Responsive]()

## Table of Contents  
* [Features](#features)  
* [Testing](#testing)
* [Bugs](#bugs)
* [Validator Testing](#validator-testing)
* [Deployment](#deployment)
* [Credits](#credits)


# User Storys 
# Development Plane
. Stratagy
. Scope
. Structure
. Skeleton
. Surface
. Wireframe

 
# Features
# Testing
# Bugs
## Solved
* When loading up my page to see if my superuser admin had been done correctly It came up with an error telling me that cloudinary-storage had no model. So when scrolling through my settings I noted that both static and media I had used a CAPITAL C instead of lower case c for cloudinary storage. Once I changed this and reloaded my browser the Django admin page loaded fine. 

* When I was trying to link my templates to my webpage, an error occurred telling me that the template I have inputted did not exist. After much going over the content of my files I noticed my folder was named template and should have been named templates. Once I corrected this my restaurant page was up and running. And that my h1 text of TEST was now visible. 

* When coming back to my project and loading up the webpage I was met with an error, that the page was a disallowed host. It advised me to add "8000-kjc-thebarn-kbsjk8ya556.ws-eu97.gitpod.io" to my allowed hosts in my settings file. Once I had done this the page loaded fine with no errors.
This happened a few more times later in my project progression so I repeated the above.
I had also forgotten to add django.contrib.sites to my settings.py file.


* When I wanted to change f_name to first_name on my models so that on my page it would show as first name and not f name. I had an error raised which said first_name does not exist. And after a lot of searching and changing code I realized that I should have migrated this change. I input show migrations and I had quite a few, once I migrated these First name was now showing instead of f name.

* Bookings once made not showing on the users my bookings page. I changed the class to a def and the  detail view for a request. I then defined bookings as I had not done this. once I had defined it so that the guest booking would show up in my booking page. I added {bookings in bookings} once I refreshed the page some of the information was showing. After some rejigging of my code, I noticed that  I had guests as bookings.guest and the other information was written up as just booking. I then changed the booking to bookings and once done, all the information on booking was now showing. A user can now view the bookings they make.

* An error occurred with my path for thankyou page. I had not placed a ‘/’ at the end so once i had entered /’thankyou’/ the page loaded correctly.


* Another bug I came across was for my edit and delete bookings class, so that the user will be able to edit or delete a booking.I was receiving  an error message “Generic detail view BookingEdit must be called with either an object pk or a slug in the URLconf”. I placed a pk after the edit_booking and delete_booking url path in urls.py and a booking.id in my edit and delete urls in my my_booking page. Page wasn't able to load as couldn't find the path. I changed the position of the pk to infront of edit_booking and delete_booking. The pages both loaded fine and once clicked on the edit button this took me to the edit page. I tried the same for the delete page, this worked fine. Then I tested that on the edit page i could change that particular booking's details, changing the time and the date, once confirmed I was then taken back to the my_booking page and the booking had indeed been updated. Again I tested that on the delete page I could delete the chosen booking, once deleted was taken back to the my_booking page where the booking had been removed. 

* The favicon wasn’t loading to the website after going over the code. It was because I had used an incorrect file path in the static folder. Once corrected the favicon was showing. 

## Unsolved Bugs
* When logged in as Teresa I made a booking. I logged out and signed up as a new user Luke. I went to make a booking for Luke and this worked as expected but what was not expected was that Teresa’s booking was also showing up. I have been unable to find a way to fix this bug with the time I had left which was disappointing.

# Future Features
* I would like to add the use of messages, so that when a user edits or deletes their booking a message would come up and disappear after 4 seconds which would say “your booking has been edited” and “your booking has been deleted”.
* I would like to add an additional menu to download.
* I would like to add a confirmation email once a user has booked with the restaurant.

# Validator Testing
* HTML - No errors found, passed on W3C HTML Validator
* CSS - No errors found, passed on W3C CSS Validator
* PEP8 Python Validator - The only error that came up were that my line of code was too long. 
![PEP8](static/css/images/pep-screenshot.png)

# Testing
## Manual Testing 
* Through development of the project in GitPod. All buttons take me to the correct place, all font awesome links take me to the correct social media sites. Booking form works correctly and the chosen fields for the edit booking page work correctly. On the live deployed site on Heroku the website works as expected.

# Technologys Used
## Frameworks, Libraries, Programs & Applications Used
* Django
* PostgreSQL
* Bootstrap
* Cloudinary - I used Cloudinary to store images from this project.
* Font Awesome - I used Icons from Font Awesome for mmy social media links which made it more realisic site.
* Figma - I used Figma in the planning stage to create my sitemap, from this I created my website like I had designed.
* GitHub - My project was stored on Github.
* GitPod - Gitpod was used for writing my code and when I pushed commits from Gitpod they were uploaded to Github where my project was stored.
* Heroku - Where the project was deployed to.
* Google Development Tool - Where I checked the responsiveness of the website and edit any code without the risk of making it a permanent change.
* Elephantsql - I used Elephantsql for my database.

## Languages
* HTML
* CSS
* Python
* Javascript


# Accessibility
* Using Google Development tools, I tested the accessability of the site via the lighthouse option. My website scored 
![LightHouse](static/css/images/lighthouse-score.png)

# Deployment
* Steps to deploy on Heroku, I push any unsaved changes from my work to GitHub.
* From Heroku I click create new app, I then named “the-barn”, I selected my region and then clicked create app.
* Once the page loaded, I went into the settings tab, I went to the config vars section and entered PORT to the key and 8000 to the value (this was added because the mock terminal may fail and the project will not work if not entered). I entered my cloudinary url and then my database url from ElephantSQL. I entered my secret key information into the config vars. 
* I then scrolled down to the build packs section, I clicked add build pack and selected python then clicked saved changes. I then clicked back on the build pack and selected node.js then clicked saved changes again. I made sure that Python was first and then node.js.
* Next, I went to the deployment section and selected my deployment method which is GitHub. I confirmed that I wanted to connect to GitHub. I searched for my repository name which is "the-barn”. I selected this and then connected to link the Heroku app to my repository code.
* I then scrolled down and clicked deploy branch from the deploy a GitHub branch (this showed me the logs being run as my project was being deployed).
* Once completed I then clicked on view to view my deployed project on the terminal. It is loaded with no errors. I then tested my project making sure everything was working as it should and it was.


# Credits
