# Change password function

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

Script __changepasswordtask.py__ has all the functions for verifying old password with system, validating new password with above defined password requirement and checking similarity between old and new passwords.

1. For verifying old password with system, making use of list of password strings stored in class variable and comparing against old password passed through testcase.
2. For validating new password, passing the new password and validating against the requirements.
3. For similarity check, passing old and new passwords and comparing them.

Now lets install the requirements for running the above scripts.
```
pip install -r requirements.txt
```
Lets run the testcase script

```
python testPasswordChangeTask.py
```

Running the Test Case script __testPasswordChangeTask.py__ will verify if the old password matches the mock system passwords and new password matches the strong password criteria, also a similarity check for old and new passwords and outputs the logs to __example.log__. I have attached a sample log file.

Following cases are covered in test script :-

__Case1:__ Valid Password  
__Case2a:__ Single Uppercase character and single special character  
__Case2b:__ Single Lowercase character and single digit  
__Case2c:__ Exact 18 length character and 50% numbers  
__Case2d:__ Exact 4 duplicated repeated character in password  
__Case2e:__ Exact 4 special characters in password  
__Case3:__ Password length is less then 18  
__Case4:__ No lowercase character in password  
__Case5:__ No uppercase character in password  
__Case6:__ No digit in password  
__Case7:__ No special characters in password  
__Case8:__ No whitespace characters in password  
__Case9:__ Duplicate repeat characters more than 4 times in password  
__Case10:__ Special Characters more than 4 times in password  
__Case11:__ Numbers more than 50% of the length of password  
__Case12:__ Old password doesn't match the system  
__Case13:__ Old password is empty  
__Case14:__ New password not similar to old password or greater then 80% similar  
