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

## Models and CRUD breakdown
| model     | endpoints                    | create        | retrieve | update | delete | filter                   | text search |
| --------- | ---------------------------- | ------------- | -------- | ------ | ------ | ------------------------ | ----------- |
| users     | users/<br>users/:id/         | yes           | yes      | yes    | no     | no                       | no          |
| profiles  | profiles/<br>profiles/:id/   | yes (signals) | yes      | yes    | no     | following<br>followed    | name        |
| likes     | likes/<br>likes/:id/         | yes           | yes      | no     | yes    | no                       | no          |
| comments  | comments/<br>comments/:id/   | yes           | yes      | yes    | yes    | post                     | no          |
| followers | followers/<br>followers/:id/ | yes           | yes      | no     | yes    | no                       | no          |
| posts     | posts/<br>posts/:id/         | yes           | yes      | yes    | yes    | profile<br>liked<br>feed | title       |
| visiting  | visiting/<int:pk>/'.         | yes           | yes      | yes    | yes    |  visiting               | title       |





## Testing
- Posts app:
    - logged out users can list posts
    - logged in users can create a post
    - logged out users can't create a post
    - logged out users can retrieve a post with a valid id
    - logged out users can't retrieve a post with an invalid id
    - logged in users can update a post they own
    - logged in users can't update a post they don't own


- Comments app:
    - logged out users can list comment
    - logged in users can create a comment
    - logged out users can't create a comment
    - logged out users can retrieve a comment with a valid id
    - logged out users can't retrieve a comment with an invalid id
    - logged in users can update a comment they own
    - logged in users can't update a comment they don't own

- Like app:
    - logged out users can't list a like
    - logged in users can create a like
    - logged out users can't create a like
    - logged out users can retrieve a like with a valid id
    - logged out users can't retrieve a like with an invalid id
    - logged in users can update a like they own
    - logged in users can't update a like they don't own

- Visiting app:
    - logged out users can't list a visit (booking)
    - logged in users can create a visit (booking)
    - logged out users can't create a visit (booking)
    - logged out users can retrieve a visit with a valid id
    - logged out users can't retrieve a visit with an invalid id
    

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


## Deployment steps

* set the following environment variables:
  - CLIENT_ORIGIN
  - CLOUDINARY_URL
  - DATABASE_URL
  - DISABLE_COLLECTSTATIC
   -  SECRET_KEY

* installed the following libraries to handle database connection:
  - psycopg2
  - dj-database-url
* configured dj-rest-auth library for JWTs
* set allowed hosts
* configured CORS:
  - set allowed_origins
* set default renderer to JSON
* added Procfile with release and web commands
* gitignored the env.py file
* generated requirements.txt
* deployed to Heroku