# Furlong Helpdesk

I have the pleasure of introducing my FullStack E-commerce Project. Furlong Helpdesk was developed with Python, Django, postgreSQL and Stripe as main tools.

The purpose of this project is help the clients take the control of how many hours they want to buy whose purpose is the training on SchoolBase app. This hours can be bought by packages or individual hours and once the clients have been bought hours, they can request bookings to Furlong for this training using the hours they bought. 

When a client request a slot of training, it needs to be aproved by the furlong admin of the website and the status of that hour will change on the profile and the calendar. If the slot requested is rejected the hours will be added by the admin to the hours available and can give a reason to the client with a comment. This makes the client having a control of how many training hours has left.  

## Website Link

Furlong Helpdesk can be accessed on: [Furlong Helpdesk](https://furlong-milestone.herokuapp.com/).

**Note for CI Assessors** - You need to create a new account with an username and a password.


## UX

* The main goal was to develop a user-friendly experience on this e-commerce website.
* Not registered users can not access to the main areas such as profile, request a training hour or either the caalendar schedule. However, if they create an account, they will have full access to it.
* All input elements are clearly labeled, and provide placeholders and default values whenever relevant
* All events on the website are complemented by alerts such as when a payment is successful, denied or card details are wrong. 
Even  when the user's Cart is empty.
* When a user is logged in a "Log Out" link is displayed and vice-versa.
* The site should be responsive and work on all browsers.   


## Wireframes

1. [Homepage - Desktop wireframe]()

2. [Homepage - Mobile wireframe]()

3. [Professional Services - Desktop wireframe]()

4. [Professional Services - Mobile wireframe]()

5. [Hours - Desktop Wireframe]()

6. [Hours - Mobile Wireframe]()

7. [Profile - Desktop Wireframe]()

8. [Profile - Mobile Wireframe]()

  
## User stories

1. **"As a Customer, I want to have a control of Professional Services hours bought."** Done, the entire website is focus on the management of this user needs.
2. **"I would like to request training hours when I can, even out of office hours."** With the hours available you can request hours at anytime filling the form for that.
3. **"I want to have full control of my spend of hours and how many I haven't use yet."** On your profile you can check that easily.
4. **"How I can check my hours requested and the days I booked them if I forgot it?"** Easy, you can go to Hours, and see them into the calendar.


## Features

### Existing Features 

* **Base template.**
  - Navbar contains:
      - Site logo for going straight forward to homepage.
      - Home button to go back to homepage.
      - Menu dropdown to enable users to navigate the site, visible in any sito of the website.
      - Login button for existing users to log back in.
      - Register button for new users to register.
        Once the user has logged in, login and register buttons will disappear.
      - Logout button to end user session.
      - Cart button only visible when user is Login.
      - Search bar for users to search for packages avilables and hours requested.
      
  - Footer contains:
      - Social media buttons which currently link homepage of the sites however would link to this websites social.
      - Copyright.

* **Index.**
  
  - Menu from navbar splited in 4 icons which link to the different parts of the site and a little explanation of what is each for.

* **Professional Services page.**
  
  - Here you can find the different packages of hours individually priced by Furlong and with the status of the package (available or Current unavailable). User can only buy the Available packages.

* **Calendar page.**
  
  - Here you can find the bookings (hours requested) displayed into a calendar wher you can see the status of the slot required (Pending, Accepted and Rejected).

* **Profile page.**

  - Users can view all the Professional services packages bought with the total hours available, the hours requested and total hours requested.

* **Contact us.**
  
  - Users can send an email with any enquiry to Furlong through this Contact us for.


## Feature Features

In the future I would like to implement this features:
- When a slot is required, aprove or reject it automatically with the availability of working hours and slots booked already.
- User view for admin site with an admin calendar.
- A live chat feature for users to contact directly with Furlong admins.


## Technologies Used

* Languages:
  - [HTML](https://en.wikipedia.org/wiki/HTML)
  - [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
  - [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  - [Python 3](https://www.python.org/download/releases/3.0/)

* Framework:
  - [Django](https://docs.djangoproject.com/en/2.2/)

* Libraries: 
  - [jQuery](https://jquery.com/)
  - [Bootstrap](https://getbootstrap.com/)
  - [Font Awesome](https://fontawesome.com/)

* Payment API:
  - [Stripe](https://stripe.com/gb)

* Databases:
  - [SQLite](https://www.sqlite.org/docs.html)
  - [PostgreSQL](https://www.postgresql.org/docs/)

* Tools:
  - [Whitenoise](http://whitenoise.evans.io/en/stable/)
  - [Git](https://en.wikipedia.org/wiki/Git)
  - [AWS-Cloud9](https://aws.amazon.com/cloud9/)
  - [Imgur](https://imgur.com/)
  - [Balsamiq](https://balsamiq.com/)

## Testing

### Responsiveness Testing 

##### Devices Tested:

* iPhone X
* iPhone 8
* iPhone 6/7
* iPad Pro
* iPad
* Samsung Galaxy S9

##### Chrome Dev Tools

I used Dev Tools to check if there was an error on my page. 
Then, I changed what was wrong in the dev tools and I would be able to see 
the changes in a live update into my browser.Once I've found the issue I went
back to Cloud9 at AWS and make the changes there. 

### Validation services
* [W3C Validator](https://validator.w3.org/#validate_by_input) - For HTML
* [JIGSAW W3C Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - For CSS
* [Python validator](http://pep8online.com/) - For Python

### Automated tests
* I used few automated tests which can be found with the name test.py files int applications folders.
* [Travis](https://travis-ci.org/) to test my test.py files.[![Build Status](https://travis-ci.org/Debbiepimpo/furlong-helpdesk.svg?branch=master)](https://travis-ci.org/Debbiepimpo/furlong-helpdesk)

### Manual Testing

I have tested the website on:

* Google Chrome
* Apple Safari
* Mozilla Firefox

### Stripe payment testing
 I've being used the below information for testing the payments.
- Card number - 4242424242424242
- CVC - Any 3 digit number.
- Expiry date - Any date in the future.

#### Manual tests in detail

- **Professional Services application**
1. If click on add to cart, number on cart icon will reflected and encrease acordingly.
2. If click on view, page will redirect to a view in depth the Professional service package details.
3. The @login_required was added across the site to only allow registered users access.
 
- **Calendar application**
1. If the admin change status of the slot required, the colour and the status will be reflected into the calendar.

- **Cart application**
1. A user can see all Professional Services added to cart's user logged.
2. Delete button deletes it from the cart if is only one package, Remove button is for decrease the number of packages by one already added to cart.

- **Checkout application**
1. Checked customer data and paymenet forms are correctly validated.
2. Error message will be displayed if the payment details are incorrect.
3. Success message will be provided if payment is successful.
4. Professional Service will be reflected and the total hours available will be incremented at profile page on successful payment.

- **Account application**
    - Registration
        1. Navigate to the registration page.
        2. Enter the email address of an already registered user and a new username.
        3. Ensure that an error message appears, saying that email is already registered.
        4. Enter a unique email address and the username of an already registered user.
        5. Ensure that an error message appears saying that a user with that username already exists.
    
    - Login
        1. Navigate to the login page.
        2. Login as each registered user in turn, entering correct username and password combinations.
        3. Ensure that the users are logged in successfuly.
        4. Attempt to log in as each registered user, entering incorrect username and password combinations.
        5. Ensure that an error message displays.
    
    - Password Reset
        1. Click on the password reset link on the login page.
        2. Ensure that a page appears inviting me to enter my email address.
        3. Enter my email address in the box and click the Reset Password button.
        4. Ensure that a page appears telling me that an email has been sent.
        5. Check my inbox for the email.
        6. Click on the link in the email and ensure that a page appears invting me to enter a new password.
        8. Login with the new password to ensure that it has been changed successfully.


## Deployment

Furlong Helpdesk was developed using Cloud9 on AWS and I've created a new repository on GitHub to keep the project saved and linked it with the Github repository created. This lets me project work against any unexpected error such as delete any essential code that makes the project working.

### Run the project local 

To run this project on your own IDE follow:

  - Make sure you have your own IDE, I used [AWS-Cloud9](https://aws.amazon.com/cloud9/) as IDE.
  - This has to be installed on your machine:
      * [PIP](https://pip.pypa.io/en/stable/installing/)
      * [Python 3](https://www.python.org/downloads/)
      * [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

I followed the [Github Help - Cloning a repository](https://help.github.com/en/articles/cloning-a-repository) instructions for giving a clear explanation of following steps:
  
1. On GitHub, navigate to the main page of the repository [Furlong-Helpdesk](https://github.com/Debbiepimpo/furlong-helpdesk).
2. Under the repository name on GitHub, click Clone or download.
3. In the Clone with HTTPs section, click the icon beside the URL to copy the clone URL for the repository.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 2.
7. Press Enter. Your local clone will be created.
8. Create a virtual environment in which to run the code.
9. Install Django in the virtual environment by entering the following in the CLI: pip install django==1.11.10.
10. Install the packages in requirements.txt by running the following command in the CLI: ``pip install -r requirements.txt``
11. Run the following command in the CLI: ``python manage.py runserver $IP:$PORT``.
12. In your settings.py file add your hostname under 'ALLOWED_HOSTS'.
13. Create a [stripe](https://stripe.com/gb) account and get your API keys.
14. In your local IDE create a file called `env.py`.
15. Inside the env.py file create this essential variables:
    - SECRET_KEY : It is your secret key.
    - STRIPE_PUBLISHABLE : From stripe API credentials is the stripe publishable.
    - STRIPE_SECRET : From stripe API credentials is the stripe secret.
    - DEFAULT_FROM_EMAIL : It is the email will be display on the From line as the email sender.
    - SERVER_EMAIL : It will be the email you want to use as the server email.
    - EMAIL_HOST : It is the host email (`smpt.gmail.com`).
    - EMAIL_HOST_USER : It is the host user.
    - EMAIL_HOST_PASSWORD : It is the password of the email used as host email.
  
16. You can now re-run the runserver command for view the project locally.

  **Note - You may need to collect static if you are having unexpected issues displaying static files with the command:```python3 manage.py collectstatic ```

### Heroku Deployment

For making Furlong Helpdesk work in Heroku, I deployed the app as follows:

1. I create a new app on Heroku and name it Furlong-milestone.
2. Enter the environment variables in the Heroku config vars:

| Key                 | Value                     |
|---------------------|---------------------------|
| DATABASE_URL        | `<postgres_url>`          |
| SECRET_KEY          | `<my_secret_key>`         |
| STRIPE_PUBLISHABLE  | `<my_stripe_publishable>` |
| STRIPE_SECRET       | `<my_stripe_secret>`      |
| DEFAULT_FROM_EMAIL  | `<my_from_email>`         |
| SERVER_EMAIL        | `<my_server_email>`       |
| EMAIL_HOST          | `<my_email_host>`         |
| EMAIL_HOST_USER     | `<my_host_user>`          |
| EMAIL_HOST_PASSWORD | `<my_host_password>`      |


3. Create the `Procfile` file for this project.
4. Create the `requirements.txt` file for this project.
5. Push the app to GitHub.
6. Go to the Deploy tab for the app on Heroku and select GitHub as the deployment method.
7. In the "Manual Deployment" section of this page on Heroku, ensure the master branch is selected and click `Deploy Branch`.
8. Once the Deployment is finished we open the app on Heroku.


## Content
- The images used on Furlong Helpdesk were sourced from Google Images usink keywords and uploading on my personal [Imgur](https://imgur.com/).
- My favicon is [Furlong]() original logo. 
  
## Acknowledgements

* I have being inspired for this project from a combination of projects from Slack group 'Peer-code-review', the idea of Unicorn attractor helped too and the final idea was inspired by Furlong which is the company I'm working while I'm developing te project.
* The Slack community have been great on giving me advice for some features i've implemented on my project.
* The tutors at code institute have also been helpful.
* [W3Schools](https://www.w3schools.com/) - I used as a guide for some doubts while i was developing the project.
* [Stack overflow](https://stackoverflow.com/) - Very good and useful website for implement what you need to use one your backend related with Python and solve little issues while the project was developing.

## Credits

* Big thank you to Code Institute for helping me to gain this Foundation Degree and very helpful with the Tutor portal.
* Also, big thank you to Slack Community whose people makes this community try to help each other with the skills they've learned for coding and can share with other students.
* My partner for helping me, being extremely patient with me during this trip and give me his unconditional support.