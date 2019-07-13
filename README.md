# =========== Change password function ==============

My script completes the below tasks.

## Requirements
ChangePassword(oldPassword: String, newPassword: String)
### Tasks
1. Code for change password function
2. Implement automate test for the created function, test cases with test data
provide in each case
3. The verify password with system and similar check function should be a mock
which return True/False
####Password requirement
1. At least 18 alphanumeric characters and list of special chars !@#$&*
2. At least 1 Upper case, 1 lower case ,least 1 numeric, 1 special character
3. No duplicate repeat characters more than 4
4. No more than 4 special characters
5. 50 % of password should not be a number
####Change password requirement
1. Old password should match with system
2. New password should be a valid password
3. password is not similar to old password < 80% match.
==================================================

Running the script changepasswordtask.py will ask the user to either enter a new password or to change an existing password.

```
pip install -r requirements.txt
python changepasswordtask.py

```

Running the Test Case script __testPasswordChangeTask.py__ will verify if the Password maches the Strong Password Criteria and outputs the logs to __example.log__. I have attached a sample log file.

```
python testPasswordChangeTask.py

```

