# ScrumMaester

This project is to create a Scrum management system, allowing Scrum masters to better manage coding teams giving better visibility on who is working on what.

## Project Goals

[The deployed version of the site is available here](https://scrummaester-81eb70fbef06.herokuapp.com/)

## Contents

* [User Experience](#user-experience)
    - [User Stories](#user-stories)
* [Design](#design)
    - [Color Scheme](#color-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Wireframe](#wireframe#)
* [Features](#features)
* [Accessibility](#accessibility)
* [Credits](#credits)
* [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
* [Deployment and Local Development](#deployment-and-local-development)
    - [Deployment](#deployment)
    - [Local Development](#local-development)
* [Testing](#testing)
    - [Solved Bugs](#solved-bugs)
    - [Known Bugs](#known-bugs)
* [Credits](#credits)
    - [Code Used](#code-used)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)


## User Experience

### User Stories

**First Time Visitor Goals**

* I want to be able to quickly ascertain the purpose of the site
* I want to be able to register quickly and easily, with no unneccesary complications
* I want the site to be easy to use and responsive to my device
* I want the layout of the site to be intuitive and easy to understand

**Returning Visitor Goals**

* I want to be able to log in quickly and easily
* I want to see content relevant to me on my dashboard
* I want to be able to Create, Update and Delete data easily
* I want to be able to quickly navigate to the information I want to access
* I want the site to be easy to use and responsive to my device

**Frequent Visitor Goals**

* I want to see content relevant to me on my dashboard
* I want to be able to Create, Update and Delete data easily
* I want to be able to quickly navigate to the information I want to access
* I want to be able to filter data in a number of ways to make it easier to follow
* I want the site to be easy to use and responsive to my device


## Design

### Color Scheme

The color palette for this site was mostly chosen by keeping Bootstrap's 'Light' class defaults, as this provided a clean aesthetic that kept out of the way of the rest of the site.

### Typography

Because the user is working with large volumes of mostly text data I wanted a font family that would be easy to read as well as not providing extra distraction from the content.

I decided to keep the Bootstrap default font family which uses Helvetica and Arial. Both are sans-serif fonts, making them clear and easy to read.

### Imagery

Because of the nature of the site, adding extra imagery seemed like an unnecessary distraction.

As a result I decided not to include any external images to keep the interface focused and easy to read.

### Wireframe

Wireframes were created using Affinity Designer.

**Login**

![Login / Register page wireframe](/static/assets/documentation/wireframes/login.jpg)

**Dashboard**

![Dashboard page wireframe](/static/assets/documentation/wireframes/dashboard.jpg)

**New Project**

![New Project page wireframe](/static/assets/documentation/wireframes/new%20project.jpg)

### Features

**Future Implementations**

### Accessibility

I have worked hard to ensure the website is as easy to navigate and as accessible to disabled people as possible. To achieve this I:

- Used semantic HTML elements
- Added Aria tags to all links, buttons and content to ensure Screen Readers are able to comprehend it
- Used a San-Serif font for site navigation, to make it as easy to read as possible
- Ensured contrasting colors were used throughout the site to keep elements easily idenitfiable and readable.

I also tested the site with the Chrome extension [Web Disability Simulator](https://chromewebstore.google.com/detail/web-disability-simulator/olioanlbgbpmdlgjnnampnnlohigkjla) to ensure the user experience was friendly to those with color blindness, parkinsons and dyslexia.

**Yellow-Blue Colorblindness**

![Yellow-Blue Colorblindness](static/assets/documentation/screenshots/yellow-blue-colorblind.png)

**Red-Green Colorblindness**

![Yellow-Blue Colorblindness](static/assets/documentation/screenshots/red-green-colorblind.png)


## Technologies Used

### Languages Used

This site is built using Python, HTML and CSS.

### Frameworks, Libraries & Programs Used

This website is built with Python's [Flask](https://flask.palletsprojects.com/en/stable/) framework. The site data is stored on a [PostgreSQL](https://www.postgresql.org/) database, using [SQLAlchemy](https://www.sqlalchemy.org/) to access the database through Python.

The login and registration forms use [WTForms](https://wtforms.readthedocs.io/en/3.2.x/), and [Bcrypt](https://pypi.org/project/bcrypt/) for password hashing.

I also used [Bootstrap](https://getbootstrap.com/) to provide responsive elements and default classes in HTML.

I used [Visual Studio Code](https://code.visualstudio.com/) for code editing, [pgAdmin](https://www.pgadmin.org/) for database management and [Affinity Designer](https://affinity.serif.com/en-us/designer/) for creating wireframes, mockups and data maps.

## Deployment and Local Development

### Deployment

The site is deployed using Heroku - [The deployed version of the site is available here](https://scrummaester-81eb70fbef06.herokuapp.com/)

**Heroku app setup**

1. From the [Heroku Dashboard](https://dashboard.heroku.com/), click the new button in the top right corner and select create new app.
2. Give your app a name (this must be unique), select the region that is closest to you and then click the create app button bottom left.

**Create the Database**

1. From the [Heroku Dashboard](https://dashboard.heroku.com/), click the name of the web app created in the previous step.
2. Click on the "Resources" tab, then click on the "Find more add-ons" button

![Resources tab](static/assets/documentation/deployment/heroku-db-1.png)

3. Scroll through the list of add-ons until you find "Heroku Postgres".

![Heroku Postgres](static/assets/documentation/deployment/heroku-db-2.png) 

4. By clicking on the "Heroku Postgres" add-on, the following page is displayed. Click on the "Install Heroku Postgres" button

![Install Postgres](static/assets/documentation/deployment/heroku-db-3.png)

5. The next page allows you to select which app to associate the database with. Select the payment plan you wish to use for this app, then click inside the "App to provision to" text box to bring up the drop-down list of apps. Select the app you wish to add the database to.

![Select app](static/assets/documentation/deployment/heroku-db-4.png)

6. Press the "Submit Order Form" button to connect the database to your app.

7. Return to the app page, where you will see "Heroku Postgres" has been added to your app. Click "Heroku Postgres" to open the database and get the Database Connection Parameters.

![Database Added](static/assets/documentation/deployment/heroku-db-5.png)

8. Click the "Settings" tab

![Settings tab](static/assets/documentation/deployment/heroku-db-6.png)

9. Then click "View Credentials"

![View Credentials](static/assets/documentation/deployment/heroku-db-7.png)

10. Make note of these credentials, as you will need them to connect to your database.

11. Open pgAdmin

12. Right click "Servers" in the top left corner, then "Register" / "Server"

![pgAdmin servers tab](static/assets/documentation/deployment/heroku-db-8.png)

13. Name your server

![Create Server](static/assets/documentation/deployment/heroku-db-9.png)

14. Click the "connection" tab, entering the details from step 10. Then click "save"

![Enter credentials](static/assets/documentation/deployment/heroku-db-10.png)


**Restoring the database from backup file**

If you haven't already, download the scrummaester.backup file from the GitHub repo - [BenMilesRocks/3-scrummaester](https://github.com/BenMilesRocks/3-scrummaester).

1. In pgAdmin, navigate to the Heroku database.

2. Open the "Schemas" tab.

3. If a Schema does not currently exist, right click to create a Schema where the data will reside.

4. Right click the Scheme, and select "Restore"

5. Click the folder in the "Filename" section to navigate to the directory where you saved the backup file

![Restore database](static/assets/documentation/deployment/restore-1.png)

6. Click "restore". This should create the tables and populate them with data.

*Please note* The default login for the Super User is Username: user1 , Password: password. This should be changed as soon as possible to prevent security issues.

### Local Development

**How to fork**

To fork the repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, [BenMilesRocks/3-scrummaester](https://github.com/BenMilesRocks/3-scrummaester).
3. Click the Fork button in the top right corner.

**How to clone**

To clone the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [BenMilesRocks/3-scrummaester](https://github.com/BenMilesRocks/3-scrummaester).
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.
6. Install the packages from the requirements.txt file by running the following command in the terminal:

##
        pip3 install -r requirements.txt

## Testing

Please refer to [testing.md](testing.md) for all testing carried out.

### Solved Bugs

| **No.** | **Bug** | **How I Solved The Issue** |
|:--------|:-------:|:--------------------------:|
| 1 | Input forms accept whitespace in fields | Added Regex to prevent whitespace validation |
| 2 | Textarea Regex stops redirect function from working, redirects user back to add_task or update_task instead. | Added logic to test if redirect would point user to present page, if so directs back to dashboard |
| 3 | Register form does not display existing team info, making it confusing and difficult to know if details are entered correctly | Query Select field, pulling all details from the Teams table for ease of use |
| 4 | Flask pages do not allow for data to be passed back to Python and then back to the page itself, preventing the use of logic to filter data according to user needs | Split each query into a seperate 'Include' statement, allowing data to be filtered in multiple ways and displayed correctly |
| 5 | Password hashing does not save correctly, adding extra characters not recognised by Bycrypt | Passed data to Bcrypt encoded as UTF-8, then decrypts the data back to a string when adding it to the database |
| 6 | Deleting foreign keys is not allowed by the database, as it creates NULL fields | Set default behaviour, assigning defaults to user_id = 1 and team_id = 1 |
| 7 | Deleting team_id 1 or user_id 1 would prevent the default foreign keys from working correctly | Added restrictions preventing deletion of user_id 1 and team_id 1 from the database |

### Known Bugs

The outstanding bugs that I am aware of relate to the Register form. I have tried multiple solutions for these issues, but was not yet able to fully resolve them. These would need resolving in a future version.

| **No.** | **Bug** |
|:--------|:-------:|
| 1 | Register form Regex stops form submission, does not properly flash message warning user |
| 2 | Register form Team Select dropdown does not accept Bootstrap styling, making it visually different from the rest of the site |


## Credits

The instructions for creating a database on Heroku uses images taken from documentation on the [QuizFaber](https://docs.quizfaber.com/4.0/eng/pages/IDH_CLOUD_HEROKU_DB.html) site, and this article on [Medium](https://medium.com/analytics-vidhya/how-to-use-pgadmin-to-connect-to-a-heroku-database-c69b7cbfccd8).

For whitespace validation I used code from this article on [Stack Overflow](https://stackoverflow.com/questions/34974942/regex-for-no-whitespace-at-the-beginning-and-end).

### Code used

### Media

### Acknowledgements

I would like to acknowledge the following people

- Jubril Akolade - my Code Institute mentor

- The Code Institute Slack channel Peer Code Review - thank you to everyone who tested the site and offered feedback