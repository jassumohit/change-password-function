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

1.Case1: Valid Password
2.Case2a: Single Uppercase character and single special character
3.Case2b: Single Lowercase character and single digit
4.Case2c: Exact 18 length character and 50% numbers
5.Case2d: Exact 4 duplicated repeated character in password
6.Case2e: Exact 4 special characters in password
7.Case3: Password length is less then 18
8.Case4: No lowercase character in password
9.Case5: No uppercase character in password
10.Case6: No digit in password
11.Case7: No special characters in password
12.Case8: No whitespace characters in password
13.Case9: Duplicate repeat characters more than 4 times in password
14.Case10: Special Characters more than 4 times in password
15.Case11: Numbers more than 50% of the length of password
16.Case13: Old password is empty
17.Case14: New password not similar to old password or greater then 80% similar
