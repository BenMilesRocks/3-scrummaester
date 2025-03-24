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

The site is deployed using GitHub Pages - [Ben Miles Rocks](https://benmilesrocks.github.io/1---Ben-Miles-Rocks/)

To Deploy the site using GitHub Pages:

1. Login (or signup) to Github.
2. Go to the repository for this project, [BenMilesRocks/3-scrummaester](https://github.com/BenMilesRocks/3-scrummaester).
3. Click the settings button.
4. Select pages in the left hand navigation menu.
5. From the source dropdown select main branch and press save.
6. The site has now been deployed, please note that this process may take a few minutes before the site goes live.

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

### Code used

### Media

### Acknowledgements

I would like to acknowledge the following people

- Jubril Akolade - my Code Institute mentor

- The Code Institute Slack channel Peer Code Review - thank you to everyone who tested the site and offered feedback