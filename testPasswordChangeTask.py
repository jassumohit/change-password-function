from changepasswordtask import PasswordChangeTask
import unittest
import logging


class TestPasswordChangeTask(PasswordChangeTask):
    """
    @class TestPasswordChangeTask
    class to test password change functionality
    """

    def setUp(self):
        """
        Method to set basic configuration for logging
        """
        logging.basicConfig(filename='example.log', level=logging.INFO)
        self.logger = logging

    def test_all_positivepassword(self):
        """
        Test Case to run all possible positive passwords with varying conditions
        """
        self.logger.info("Case1: Valid Password")
        self.assertTrue(self.changePassword("123abc456def789gh$A", "Aaa9876576ddpoo@123$mnbvcx"),
                        "Failed to verify and change password")
        self.logger.info("Case1: verified successfully\n")

        self.logger.info("Case2: Boundary level Passwords")

        self.logger.info("Case2a: Single Uppercase character and single special character")
        self.assertTrue(self.changePassword("123abc456def789gh$A", "Azxcvbnmsdfghjkl@12346"),
                        "Failed to verify and change password")
        self.logger.info("Case2a: Single Uppercase character and single special character verified successfully\n")

        self.logger.info("Case2b: Single Lowercase character and single digit")
        self.assertTrue(self.changePassword("123abc456def789gh$A", "aSDFGHJKLZXCVB1ZXCM@&QWERT"),
                        "Failed to verify and change password")
        self.logger.info("Case2b: Single Lowercase character and single digit verified successfully\n")

        self.logger.info("Case2c: Exact 18 length character and 50% numbers")
        self.assertTrue(self.changePassword("123abc456def789gh$A", "AsdfgZxc@123456789"),
                        "Failed to verify and change password")
        self.logger.info("Case2c: Exact 18 length character and 50% numbers verified successfully\n")

        self.logger.info("Case2d: Exact 4 duplicated repeated character in password")
        self.assertTrue(self.changePassword("123abc456def789gh$A", "MMMMnbvccxz@@@1234poio"),
                        "Failed to verify and change password")
        self.logger.info("Case2d: Exact 4 duplicated repeated character in password verified successfully\n")

        self.logger.info("Case2e: Exact 4 special characters in password")
        self.assertTrue(self.changePassword("123abc456def789gh$A", "QWERTasdfg$@&%0987123zxc"),
                        "Failed to verify and change password")
        self.logger.info("Case2e: Exact 4 special characters in password verified successfully\n")

    def test_negativepassword(self):
        """
        Method to test all negative cases for new password
        """

        self.logger.info("Case3: Password length is less then 18")
        try:
            self.changePassword("123abc456def789gh$A", "Tasdfg$0987123zxc")
            self.logger.exception("Failed to verify length of password\n")
        except ValueError as e:
            self.logger.info(format(e))
            self.logger.info("Successfully handled exception when password length is less then 18\n")

        self.logger.info("Case4: No lowercase character in password")
        try:
            self.changePassword("123abc456def789gh$A", "QWERTYUIOP2345@@$$ZXC")
            self.logger.exception("Failed to verify lowercase character in password\n")
        except ValueError as e:
            self.logger.info(format(e))
            self.logger.info("Successfully handled exception when no lowercase character in password\n")

        self.logger.info("Case5: No uppercase character in password")
        try:
            self.changePassword("123abc456def789gh$A", "zxcvbnmasdfg12345$as")
            self.logger.exception("Failed to verify uppercase character in password\n")
        except ValueError as e:
            self.logger.info(format(e))
            self.logger.info("Successfully handled exception when no uppercase character in password\n")

        self.logger.info("Case6: No digit in password")
        try:
            self.changePassword("123abc456def789gh$A", "ZXCVqwertyui$&asx*asdfghjk")
            self.logger.exception("Failed to verify digits in password\n")
        except ValueError as e:
            self.logger.info(format(e))
            self.logger.info("Successfully handled exception when no digits in password\n")

        self.logger.info("Case7: No special characters in password")
        try:
            self.changePassword("123abc456def789gh$A", "QWERTasdfgh123456ZXCV")
            self.logger.exception("Failed to verify length of password\n")
        except ValueError as e:
            self.logger.info(format(e))
            self.logger.info("Successfully handled exception when no special characters in password\n")

        self.logger.info("Case8: No whitespace characters in password")
        try:
            self.changePassword("123abc456def789gh$A", "ZXCVwert\t zxc  vb1223@$")
            self.logger.exception("Failed to verify whitespace characters password\n")
        except ValueError as e:
            self.logger.info(format(e))
            self.logger.info("Successfully handled exception when whitespace characters in password\n")

        self.logger.info("Case9: Duplicate repeat characters more than 4 times in password")
        try:
            self.changePassword("123abc456def789gh$A", "PPPPPdfcasvgbhsdnw@1234$")
            self.logger.exception("Failed to verify duplicate repeat characters more than 4 times in password\n")
        except ValueError as e:
            self.logger.info(format(e))
            self.logger.info("Successfully handled exception when duplicate repeat characters more than 4\
            times in password\n")

        self.logger.info("Case10: Special Characters more than 4 times in password")
        try:
            self.changePassword("123abc456def789gh$A", "PPdfcas@$$%@12vgbhsdnw@1234$")
            self.logger.exception("Failed to verify Special Characters more than 4 times in password\n")
        except ValueError as e:
            self.logger.info(format(e))
            self.logger.info("Successfully handled exception when Special Characters more than 4 times in password\n")

        self.logger.info("Case11: Numbers more than 50% of the length of password")
        try:
            self.changePassword("123abc456def789gh$A", "ASdfgzxc@1234567890")
            self.logger.exception("Failed to verify Numbers more than 50% of the length in password\n")
        except ValueError as e:
            self.logger.info(format(e))
            self.logger.info("Successfully handled exception when Numbers more than 50% of the length in password\n")

        self.logger.info("Case12: Old password doesn't match the system")
        try:
            self.changePassword("123abc45xcvbn@quwe", "PPdfcas@$$%@12vgbhsdnw@1234$")
            self.logger.exception("Failed to verify old password with system\n")
        except ValueError as e:
            self.logger.info(format(e))
            self.logger.info("Successfully handled exception when old password doesn't match in the system\n")

        self.logger.info("Case13: Old password is empty")
        try:
            self.changePassword("", "PPdfcas@$$%@12vgbhsdnw@1234$")
            self.logger.exception("Failed to verify empty old password\n")
        except ValueError as e:
            self.logger.info(format(e))
            self.logger.info("Successfully handled exception when old password doesn't match in the system\n")

        self.logger.info("Case14: New password not similar to old password or greater then 80% similar")
        try:
            self.changePassword("123abc456def789gh$A", "123abc45f345gh$A")
            self.logger.exception("Failed to verify similar new password to old password\n")
        except ValueError as e:
            self.logger.info(format(e))
            self.logger.info("Successfully handled exception when new password is similar to old password\n")

    def tearDown(self):
        """
        Cleanup and remove objects created in test case
        """
        self.logger.shutdown()


if __name__ == "__main__":
    unittest.main()

