# Meal Planner

This is a Django based app that allows users to plan their meals.

As stated on the home page: Plan your meals. Planning meals has never been easier. Add plans by date for breakfast, lunch, dinner, and even a snack.

See a live demo at <a href="https://stevebrauner.pythonanywhere.com">https://stevebrauner.pythonanywhere.com</a>.

##Install

1. clone repo
2. create virtual exvironment via poetry or requirements.txt
3.  Copy .env.dist to .env and make changes

**Set secret key**
export SECRET_KEY=<your secret key value>

**Set debug to FALSE in production. Use TRUE for development**
export DEBUG=FALSE

## Design Specification

Users will be able to plan their meals.

For user authentication users will need to be able to register, log in, log out, and
delete their account.

Users will need to be able to create, view, edit, and delete plans (based by date)
for breakfast, lunch, dinner, and other meals.

The home page will describe the app and will invite users to register or log in. After
logging in it will display the username welcome and ability to log out.

## Technical Specification

The database will need to track plans by owner (user).

Each plan will have breakfast, lunch, dinner, and other meals.

Each meal will have a title and optional description.
