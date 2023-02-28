Simple API to a user has oAuth with methods to

1. Create a user
2. Login on the user
3. Logout the user
4. Inactivated the user

Have one model per controller, the model will validate the objects in the request. If invalid will return 400 with an "invalid request" message in the response

The controllers will have the business rules, validate if they have the right sip method, and have a method call to utils method to make interaction in the DB having the return in the controller if have success or unsuccess

Dockerfile has only the parameters to compile the project buildspec is the file to use, only, with the CI/CD using AWS settings is the file to have some business information as config used within the build. utils will be used as an interface to some models, and common methods used at all project

Recommended to run flake8 to minimize issues in the code. To install and run:
1. Open the terminal and run: pip install flake8. If you use another Linux distro, probably have another similar command like yum...
2. Now you have flake, to run in the project directory: flake8 .
3. This command will verify all files in the directory, is recommended to exclude the virtual environment like .venv or venv or similar. The full command example: flake8 . --exclude venv
4. The result has the class and lines with columns to change the code as a recommendation.