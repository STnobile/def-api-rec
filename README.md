![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

![Api](/documentation/api.png)

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


## User stories

| Category  | as       | I want to                      | so that I can                                     | mapping API feature                          |
| --------- | -------- | ------------------------------ | --------------------------------------------------|--------------------------------------------- |
| auth      | user     | register for an account        | have a personal profile with a picture            | dj-rest-auth<br>Create profile (signals)     |
| auth      | user     | register for an account        | create, like and comment on posts                 | Create post<br>Create comment<br>Create like |
| auth      | user     | register for an account        | follow users                                      | Create follower                              |
| posts     | visitor  | view a list of posts           | browse the most recent uploads                    | List/ Filter posts                           |
| posts     | visitor  | view an individual post        | see user feedback, i.e. likes and read comments   | Retrieve post                                |
| posts     | visitor  | search a list of posts         | find a post by a specific artist or a title       | List/ Filter posts                           |
| posts     | visitor  | scroll through a list of posts | browse the site more comfortably                  | List/ Filter posts                           |
| posts     | user     | edit and delete my post        | correct or hide any mistakes                      | Update property<br>Destroy property          |
| posts     | user     | create a post                  | share my moments with others                      | Create post                                  |
| posts     | user     | view liked posts               | go back often to my favourite  posts              | List/ Filter posts                           |
| posts     | user     | view followed users' posts     | keep up with my favourite users' moments                           | List/ Filter posts                           |
| likes     | user     | like a post                    | express my interest in someone's shared moment                     | Create like                                  |
| likes     | user     | unlike a post                  | express that my interest in someone's shared moment has faded away | Destroy like                                 |
| comments  | user     | create a comment               | share my thoughts on other people's content                        | Create comment                               |
| comments  | user     | edit and delete my comment     | correct or hide any mistakes                                       | Update comment<br>Destroy comment            |
| profiles  | user     | view a profile                 | see a user's recent posts + post, followers, following count data  | Retrieve profile<br>List/ filter posts       |
| profiles  | user     | edit a profile                 | update my profile information                                      | Update profile                               |
| followers | user     | follow a profile               | express my interest in someone's content                           | Create follower                              |
| followers | user     | unfollow a profile | express that my interest in someone's content has faded away and remove their posts from my feed | Destroy follower           |
| visiting  | user     | book a visit       | I can navigate the booking page so that I will be able to book a visit edit it or delete it  | Create Destroy                 |

     
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
| visiting  | visiting/< int:pk >/'         | yes           | yes      | yes    | yes    | visiting                 | title       |

![Agile](/documentation/agile.png)

### Scope (backend)
Our scope for this project is small and aims to cover the basic functionality of what a social media application needs. The project would be further developed upon post-production.

The API will have appropriate apps to fulfil the following tasks:
- CRUD functionality on Posts 
- CRUD functionality on Comments 
- Create, Read and Delete functionality on Likes 
- Create, Read and Delete functionality on Followers 
- Create, Read and Delete functionality on Bookmarks 
- Create functionality on Contact Us form.



### Structure (backend) 
The structure of the API needed to be organized, so we could make sure that all the relationships between the models could be mapped before coding. Below in the section, you can see the relationships between the models with the arrows.

- Post Model
    - owner (User, on_delete=models.CASCADE)
    - title - max length 100 characters
    - content - text field
    - image - image field, default post image if user doesn't add image
    - created_at - datetime field
    - updated_at - datetime field
- Profile Model
    - owner (Foreign Key - from User model)
    - first_name - max length 255 characters
    - last_name - max length 255 characters
    - email - max length 255 characters
    - created_at - datetime field
    - updated_at - datetime field
    - name - max length 250 characters
    - bio - text field
    - image - image field, default post image if user doesn't add image
- Comment Model
    - owner (Foreign Key - from User model)
    - post (Foreign Key - from Post Model)
    - content - text field
    - created_at - datetime field
    - updated_at - datetime field
- Like Model
    - owner (Foreign Key - from User model)
    - post (Foreign Key - from Post Model)
    - created_at - datetime field
- Follower Model
    - owner (Foreign Key - from User model, related_name='following')
    - followed (Foreign Key - from User model, related_name='followed')
    - created_at - datetime field
- Visiting Model
    - owner (Foreign Key - from User model)
    - date ( Model field )
    - tour_section (max length 100)
    - TOUR_SECTION [Museum, Photo Gallery, Underground Wine tanks, Private Garden]
    - time_slot (max length 50 )[10:00 am - 11:30 am,12:00 pm - 1:30 pm, 4:00 pm - 5:30 pm, 6:00 pm - 7:30 pm]
    - max_capacity = default 28
    - num_of_people = default 1
    - current_capacity = default 0
    - created_at - datetime field
    - update_at - datetime field

    ![Api](/documentation/erd.png)


## Features Crud
The API's main features within this app are CRUD based. ie. Create, Read, Update and Destroy. The following list shows what this API can provide through various request/post/put & delete calls.
- Add/Edit/Delete a Post
- Add/Edit/Delete a Comment 
- Add/Delete a Like 
- Add/Delete a Visiting
- Add/Delete a Follow
- Filter posts by title, likes and owner
- Filter posts by owner
- Filter posts by following 
- Filter posts by followers 
- Comments, Contact and Profiles are registered with read-only fields so the admin can only assess and delete any user content that is harmful.
  - The Apps registered in the admin panel are Posts, Comments, Profiles and Visiting. 
   - Admin login panel if you add `/admin` to the root url.
  - Post App logic is that  the admin can Create, Read, Edit or Destroy any post on the platform.
  - Admin Panel, so the admin can have control over the content on the website. For example, if any harmful content is posted, the Admin can remove the content and/or user profile.


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


![Testing](/documentation/test.png)
    
## Project backend Goal 
The goal of the backend API is to create a fully functional API which supplies data for a frontend react app. The admins will be able to post, update and delete posts/comments/likes/bookmarks and follows within the development environment of the API (when debug is set to True). Outside of the development environment, Users will be able to do the same from the frontend react app accessing the API which serves JSON data directly to the frontend.



## Libraries Used 
- Cloudinary - [`pip install cloudinary==1.34.0`](https://pypi.org/project/cloudinary/) - Cloud based image storage
- Django Database Url - [`pip install dj-database-url==0.5.0`](https://pypi.org/project/dj-database-url/0.5.0/) - Supporting cloud based database management
- Django REST Auth - [`pip install dj-rest-auth==2.1.9`](https://pypi.org/project/dj-rest-auth/2.1.9/) - Account authentication for Django REST
- Django v.3.2 - [`pip install Django==3.2.21`](https://pypi.org/project/Django/3.2.21/) - Django Framework
- Django AllAuth - [`pip install django-allauth==0.44.0`](https://pypi.org/project/django-allauth/0.44.0/) - Account authorization 
- Django Cloudinary Storage - [`pip install django-cloudinary-storage==0.3.0`](https://pypi.org/project/django-cloudinary-storage/) - Supporting Cloudinary Image Storage
- Django CORS Headers - [`pip install django-cors-headers==4.2.0`](https://pypi.org/project/django-cors-headers/) - Support Cross Origin Resource Sharing
- Django Filter - [`pip install django-filter==23.3`](https://pypi.org/project/django-filter/) - Filtering database model fields
- Django REST Framework - [`pip install djangorestframework==3.14.0`](https://pypi.org/project/djangorestframework/) - Django REST Framework for backend data management
- Django REST Simple JSON Tokens - [`pip install djangorestframework-simplejwt==5.3.0`](https://pypi.org/project/djangorestframework-simplejwt/) - Encryption and decryption of JSON web tokens.
- Gunicorn - [`pip install gunicorn==21.2.0`](https://pypi.org/project/gunicorn/) - Supporting Deployment to Heroku
- Pillow - [`pip install Pillow==10.0.0`](https://pypi.org/project/Pillow/) - Supporting image processing 
- Psycopg2 - [`pip install psycopg2==2.9.7`](https://pypi.org/project/psycopg2/) - Supporting Deployment to Heroku

## Deployment Guide
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


## Technology 
- [Cloudinary](www.cloudinary.com): For image storage
- [ElephantSQL](www.elephantsql.com): For database storage and management
- [Heroku](https://heroku.com): Heroku hosting platform.

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
 - Set up an account with Heroku, then follow these steps for deployment -
   Create an app
   Name the app
   Connect the app to GitHub and find the repository.
   Configure Variables - These are often the sensitive data variables that are needed to be kept secret from public sight. Head over to the settings tab and under the Config Vars sections, add the config vars appropriate to the app. In this case, it is ALLOWED_HOSTS, CLIENT_ORIGIN, CLOUDINARY_URL and DATABASE_URL, EMAIL_HOST_PASS, EMAIL_HOST_USER and SECRET_KEY. Note: ALLOWED_HOSTS and CLIENT_ORIGIN will be almost identical. ALLOWED_HOSTS will be the url without https:// and CLIENT_ORIGIN will have the full length url including https://, however excluding the final forward slash /
   ![Testing](/documentation/heroku.png)



# Reflection on Project Deployment Challenges and Learning


During the deployment of my recent project, I encountered several significant challenges, particularly in the back-end development. Despite diligent efforts and numerous sessions with my mentor and tutor, a perplexing error persisted, eluding resolution. This setback necessitated a thorough review of the entire project, a step that was both time-consuming and critical.

In the process of revisiting the walkthrough of the project, I was able to identify and rectify major bugs that were impeding progress. However, the back-end of the project continued to present numerous issues. The complexity of these problems was such that they demanded extensive time and attention, often at the cost of other aspects of the project, including the documentation.

One of the most significant challenges was the inability to complete the README file. A comprehensive README is crucial for any project as it serves as the first point of reference for anyone trying to understand or use the project. The lack of a complete README file was a clear indication of how the back-end issues had overshadowed other important elements of the project.

Through this experience, I learned several valuable lessons. Firstly, the importance of a systematic approach to problem-solving in software development became evident. It's not just about finding a solution but understanding the problem deeply. Secondly, effective communication with mentors and tutors is key. Reflecting on my interactions, I realize that asking more targeted questions and perhaps seeking diverse perspectives could have led to quicker resolutions.

Additionally, this experience underscored the importance of time management and prioritization in project development. Balancing the troubleshooting of technical issues with documentation and other project components is crucial. In hindsight, a different approach to prioritizing tasks might have yielded a more balanced outcome.

Overall, while the journey was fraught with challenges, the skills and insights I gained are invaluable. They have not only equipped me to handle similar situations in the future but have also honed my approach to project management and problem-solving in the field of software development.