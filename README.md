![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,
 def-api-rec
 - Description
def-api-rec is a RESTful API designed to facilitate user interactions within a social platform. Users can book events, create and comment on posts, manage followers, and like posts. The API ensures that users can only modify their own posts, comments, bookings, and likes.

## Features
 - Booking System: Users can create, update, or delete their 
   bookings.
 - Comments: Users can add comments to posts, edit their  
    comments, or delete them.
 - Posts: Users can create posts with images, titles, and  
    content, as well as edit or delete them.
 - Followers: Users can follow or unfollow other users.
 - Likes: Users can like or unlike posts.
 - Authentication: Ensures that a user can only modify their own 
     resources.
## Endpoints
 - Root: path('', root_route)
 - Admin: path('admin/', admin.site.urls)
 - API Authentication: path('api-auth/', include('rest_framework. 
   urls'))
 - Logout: path('dj-rest-auth/logout/', logout_route)
 - Authentication routes: path('dj-rest-auth/', include(. 
     'dj_rest_auth.urls'))
 - Registration: path('dj-rest-auth/registration/', include. 
    ('dj_rest_auth.registration.urls'))
 - Profiles: path('', include('profiles.urls'))
 - Posts: path('', include('posts.urls'))
 - Comments: path('', include('comments.urls'))
 - Likes: path('', include('likes.urls'))
 - Followers: path('', include('followers.urls'))
 - Visits: path('', include('visiting.urls'))
 - Technologies Used
 - Django
 - Django Rest Framework
 - Django Allauth
 - Django Cloudinary Storage
 - Django CORS Headers
 - Django Filter
 - Django Rest Auth
 - Cloudinary
 - PostgreSQL


## Installation

To install the necessary packages, run:
 requirements.txt


# Authentication
Default user credentials for testing:

- Username: test
- Password: test


# Deployment Guide
- <u>Heroku Authentication:</u> Use the Heroku CLI to log in to your 
   account.
- <u>Project Directory:</u> Navigate to the def-api-rec project's root.
- <u>Git Initialization:</u> If you haven't already, set up a Git repository and commit your project.
- <u>Heroku App Creation:</u> Using the CLI, create a new Heroku app.
You can provide a unique name or let Heroku auto-generate one 
 for you.
- <u>Environment Variables:</u> Configure necessary environment variables for your project (e.g., DJANGO_SECRET_KEY) via the Heroku dashboard or CLI.
- <u>PostgreSQL Integration:</u> Add a PostgreSQL database to your Heroku app. Heroku offers a free-tier database which can be attached via the Heroku dashboard.
- <u>Django Settings:</u> Modify your settings.py to recognize the DATABASE_URL provided by Heroku and use the dj_database_url library to parse it.
- <u>Heroku Deployment:</u> Push your application code to Heroku using Git.
- <u>Database Migration:</u> Migrate your database schema using the Heroku CLI.
- <u>Access Application:</u> Open your app's URL in a browser or use the heroku open command to view it.