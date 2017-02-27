# Dental Clinic - Stream 3 - Full Stack Development

Dental Clinic is my Stream 3 project for my full stack web developer training with the [Code Institute](https://www.codeinstitute.net/). 

## Deployment 

See deployment at [https://dentist-project.herokuapp.com/](https://dentist-project.herokuapp.com/)

## About 

Dental Clinic is a fictitious website for a Dental Clinic which has decided to offer its patients a 15% discount on it's bi-annual visit costs by allowing the patient to pay those costs in monthly installments of €9.75.

The user can add up to a total of 10 family members to his/her account, set up a Stripe subscription, and set up appointments for those family members.

There is also a blog and discussion forum that includes poll functionality. Although part of our training including learning how to allow the user post their own blog posts, a design decision was taken to not include this functionality.

To navigate the site and see all the functionality, it is advised to set up a dummy account with at least 2 family members, using a fake email address and the Stripe dummy credit card number 4242 4242 4242 4242. Other fields can be any valid numbers: CVV - 3 digits, and expiry dates a future month.

## Technologies

The application was built using the following framework/languages:

- Django
- Python
- HTML
- CSS 
- Javascript
- JQuery

## Design

- A paid Bootstrap theme from MOJO themes was used. This theme didn't include a forum, so I used the [template No. 4 from Tutorialzine here](http://tutorialzine.com/2015/06/12-time-saving-bootstrap-examples/).

- All images were sourced from [Pixabay](https://pixabay.com/), a free royalty-free images site.

This was my first time slicing up a theme for use in a Django project, and it was a very rewarding experience. It opened my eyes that I can create a great looking website without having the strongest design skills and without employing the services of a designer.

## Models

The project has 3 models:

- User - all the user account info, excluding full name, which is passed to:
- Family - since the user can add family members to his/her account, I created a separate model for family members. This is effectively a Patient model, with User as foreign key. The user passes his/her and family members' full names to the database, and then these patients are used to create:
- Appointment - each patient can create appointments, with Family member as a OneToOneField so each patient can only have one appointment.

## Challenges Faced

As this was my first solo Django Project, I faced a huge number of challenges, and on quite a few occasions spent more than an hour figuring out a single line of code. Challenges and accomplishments included:

- Learning my way around Django's Model-View-Template structure and figuring out all the different settings and URLs.

- Learning how to use the Bootstrap theme within the Django template layout. In particular it was challenging to create the blog and forum pages.

- Expanding the User model we had learned in the user model to include `number_family` (number of family members). This choice field in the Membership form dynamically affects the rest of the form (extra fields appear for additional family member names and the price at the top of the form changes based on this selection). The `accounts.views.register` function was expanded to create a dynamic number of Family table records based on the number of family members selected.

- Working with 3 models with foreign key relationships and accessing that data both in forms and templates - in particular this was a challenge because to obey the rules of normalisation I stored the patient names one layer down from the User in the Family table. Thus I had to write functions such as ```get_user_appointments```, which started with the User Id and then went through the Family table to get the appointments from the Appointment table which corresponded to the User ID.

- The same issue occurred when trying to display the user's full name in the templates. Since the username had been set as the user's email address for login purposes, the email address was displaying all over the website as the username. This was wrong, as it is clearly bad practice to have an email address showing when a user makes forum posts. Therefore I had to write a template tag (```get_full_name``` in ```account_extras```) to display the user's full name on the website instead of the email address.

- Deployment to Heroku. I decided to deploy my project early so that I could make changes right up to the submission deadline without having to worry about deployment going wrong. This was a great decision and taught me a lot about updating the live version of the site. In hindsight, I would have created a second Heroku instance for deployment of my testing site, as there was a regrettable 4am deployment of a completely non-working version of the site, which required the reversal of the last Github commit and the loss of a minor amount of code.

## Testing 

Some Unit Testing was performed, but this is definitely the weakest part of the project. At first I didn't get the importance of testing, as I was testing everything manually, but as the website grew it became clear that I needed it and in future projects the tests should be written at the same time as the rest of the code.

## Outstanding Issues

I ran out of time as the submission deadline approached, and the following are outstanding issues:

- The appointments date picker can pick dates from the past and weekend dates when the surgery is closed.
- The last post in the forum is showing as 'John Doe' rather than picking the last poster.
- The 'recent news' section in the blog should link to recent blog posts
- After separating my settings file I had an error retrieving static files, which I resolved by moving the static files into the settings directory. I'm not sure which settings to fix to move it back out of there.
- I don't have a satisfactory level of unit testing coverage (Appointments App not covered yet).
- 2 appointments can be created at the same time.
- I couldn't save the Stripe keys as environment variables.
- Users can't currently reschedule appointments.





