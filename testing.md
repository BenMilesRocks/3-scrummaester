# Scrum Maester -  Testing

![The Scrum Maester site shown on a variety of screen sizes](static/assets/documentation/screenshots/responsive-display.png)

Visit the deployed site: [Scrum Maester](https://scrummaester-81eb70fbef06.herokuapp.com/)

- - -

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [Lighthouse](#lighthouse)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)

Testing was ongoing throughout the entire build. I utilised Chrome developer tools whilst building to pinpoint and troubleshoot any issues as I went along.

During development I made use of Google developer tools to ensure everything was working correctly and to assist with troubleshooting when things were not working as expected.

I have gone through each page using Google Chrome developer tools & Microsoft Edge inspector tool to ensure that each page is responsive on a variety of different screen sizes and devices.

- - -

## AUTOMATED TESTING

### W3C Validator

**HTML Validation**

I used [W3C's HTML validator](https://validator.w3.org/) to check my code.

**CSS Validation**

I used [W3C's Jigsaw Validator](https://jigsaw.w3.org/css-validator/) to test my site's CSS.

- - -

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

- - -

## MANUAL TESTING

### Testing User Stories

**First Time Visitors**

| **Goals** | **How are they achieved?** |
| --- | --- |

**Returning Visitors**

| **Goals** | **How are they achieved?** |
| --- | --- |

**Frequent Visitors**

| **Goals** | **How are they achieved?** |
| --- | --- |

- - -

### Full Testing

Full testing was performed on the following devices:

Desktop:
<ul><li>HP Envy All-in-one 32-a10</li></ul>

Mobile Devices:

<ul>
<li>Samsung Galaxy S20 FE</li>
<li>Samsung A20</li>
</ul>


Each device tested the site using the following browsers:

* Google Chrome
* Microsoft Edge
* Firefox

Additional testing was taken by friends and family on a variety of devices and screen sizes. They reported no issues when using the site.


| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | ---- | --- | --- |
| **Home Page** | --- | --- | --- | --- |
| Login button | Redirect to login.html | Clicked Login button | Redirected to login.html | **PASS** |
| Register button | Redirect to register.html | Clicked Register button | Redirected to register.html | **PASS** |
| Responsive elements | Elements should resize on smaller screens | Resized screen, tested with Chrome Developer tools | Elements resized as expected | **PASS** |
| **Register Page** | --- | --- | --- | --- |
| Input Validation | Page should not accept null values, should display message to warn user | Entered null values on register page | Warning message flashes, asking user to enter details for empty fields | **PASS** |
| Register User | Correctly entered details should create a new user on the database | Entered user details, checked database using PGAdmin | User details created successfully | **PASS** |
| Regex Validation | Whitespace should not be allowed in fields | Entered whitespace in fields, checked database using PGAdmin | User not created in database | **PASS** |
| Log In Nav Bar option | Should redirect to Login.html | Clicked Log In | Redirected to login.html | **PASS** |
| 'Already have an account?' button | Should redirect to Login.html | Clicked 'Already have an account?' button | Redirected to login.html | **PASS** |
- - -