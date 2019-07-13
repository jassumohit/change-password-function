import re
import logging
import unittest


class PasswordChangeTask(unittest.TestCase):
    """
    @class: PasswordChangeTask
    class to verify, check and change the password
    """
    # class variable
    systemPasswordList = ['123abc456def789gh$A', 'testingSample**1$$zz', 'MohitJasuja@0987$$11']
    # setting logging basic configuration
    logging.basicConfig(filename='example.log', level=logging.INFO)
    logger = logging

    def verifyPassword(self, oldpassword):
        """
        verify password with system
        :param oldpassword: String for old password
        :return: True --> If password matches
                False --> If password doesn't match
        """
        if not oldpassword.strip():
            raise ValueError("Cannot verify empty string")
        if oldpassword in self.systemPasswordList:
            return True
        else:
            return False

    def similarity(self, oldpass, newpass):
        """
        Function to check similarity between old password and new password
        :param oldpass: String for old password
        :param newpass: String for new password
        :return: True --> If new password is 80% or more similar to old password
                 False --> If new password is less then 80% similar to old password
        """
        threshold = round(len(oldpass) * 0.8)
        count = 0
        for i, j in zip(oldpass, newpass):
            if i == j:
                count += 1
        if count >= threshold:
            return True
        else:
            return False

    def checkDuplicates(self, password):
        """
        Function to check if string has duplicates more than 4
        :param password: String to check duplicates
        :return: True --> If any character in string has more than 4 duplicates
                 False --> If no character is duplicated more than 4 times in string
        """
        d = {}
        for i in password:
            d[i] = d.get(i, 0) + 1
        for i in d:
            if d[i] > 4:
                return True
        return False

    def checkPassword(self, newpassword):
        """
        Function to validate the new password matches the following criteria
        1. At least 18 alphanumeric characters
        2. At least 1 Upper case, 1 lower case ,least 1 numeric, 1 special
           character from list of special chars [!@#$&*]
        3. No duplicated characters more than 4 in new password
        4. Special Character should not be more than 4 in new password
        5. Number of digits should not exceed 50% of the length of new password

        :param newpassword: String that matches the above criteria

        :return: True --> If password is valid
                 ValueError --> If password is invalid
        """
        while True:
            if len(newpassword) < 18:
                self.logger.info("Password Length should be greater than 18")
                flag = -1
                break
            elif not re.search("[a-z]", newpassword):
                self.logger.info("Password should have atleast 1 Lowercase Character")
                flag = -1
                break
            elif not re.search("[A-Z]", newpassword):
                self.logger.info("Password should have atleast 1 Uppercase Character")
                flag = -1
                break
            elif not re.search("[0-9]", newpassword):
                self.logger.info("Password should have atleast 1 digit")
                flag = -1
                break
            elif not re.search("[!@#$&*]", newpassword):
                self.logger.info("Password should have atleast 1 special characters from !@#$&*")
                flag = -1
                break
            elif re.search("\s", newpassword):
                self.logger.info("Password should not contain any whitespace characters")
                flag = -1
                break
            elif self.checkDuplicates(newpassword):
                self.logger.info("Password should not have duplicate repeat characters more than 4 times")
                flag = -1
                break
            elif len(re.sub('[\w]+', '', newpassword)) > 4:
                self.logger.info("Password should not have more then 4 special characters")
                flag = -1
                break
            elif sum(character.isdigit() for character in newpassword) > int(len(newpassword)/2):
                self.logger.info("Password should not contain more than 50% digits of the length")
                flag = -1
                break
            else:
                flag = 0
                break

        if flag == -1:
            raise ValueError("Not a valid Password")

        return True

    def changePassword(self, oldpassword, newpassword):
        """
        Function to change password that verifies below criteria :-
        1. Old password should match with system
        2. New password should be a valid password
        3. New Password should not be similar to 80% of old password
        :param oldpassword: String for old password
        :param newpassword: String for new password
        :return:
                True --> If all the above conditions are passed
        """
        if self.verifyPassword(oldpassword):
            self.logger.info("Old Password matched successfully with system")
        else:
            raise ValueError("Sorry, Password didn't match in the system")
        if self.checkPassword(newpassword):
            self.logger.info("New Password validated successfully")
        if self.similarity(oldpassword, newpassword):
            raise ValueError("New Password should not be similar to old password")

        return True

