import unittest
from unittest import runner


from Tests.LoginWithEmailTest import LoginTest
from Tests.MapTest import LoginTestm
from Tests.MyAppointmentsTest import LoginTestmy
from Tests.LogoutTest import LoginTestl
from Tests.RegisterTest import LoginTestr
from Tests.BookAppoinmentTest import LoginTestbo
from Tests.BookHealthCheckTest import LoginTestb
from Tests.ChangePassTest import LoginTestc
from Tests.EditProfileTest import LoginTeste
from Tests.ForgetUserNameTest import LoginTest3
from Tests.LinkServeContactTest import LoginTestli
from Tests.LoginWithForgetPasswordTest import LoginTest2
from Tests.SocialMediaTest import LoginTests
from Tests.SignupMembershipTest import LoginTestsi
from Tests.LoginWithSignupTest import LoginTest1


login_email = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
login_map = unittest.TestLoader().loadTestsFromTestCase(LoginTestm)
login_MyAppointments = unittest.TestLoader().loadTestsFromTestCase(LoginTestmy)
login_Logout = unittest.TestLoader().loadTestsFromTestCase(LoginTestl)
login_Register = unittest.TestLoader().loadTestsFromTestCase(LoginTestr)

login_BookAppoinment = unittest.TestLoader().loadTestsFromTestCase(LoginTestbo)
login_BookHealthCheck = unittest.TestLoader().loadTestsFromTestCase(LoginTestb)
login_ChangePass = unittest.TestLoader().loadTestsFromTestCase(LoginTestc)
login_EditProfile = unittest.TestLoader().loadTestsFromTestCase(LoginTeste)
login_ForgetUserName= unittest.TestLoader().loadTestsFromTestCase(LoginTest3)

login_LinkServeContact = unittest.TestLoader().loadTestsFromTestCase(LoginTestli)
login_LoginWithForgetPassword = unittest.TestLoader().loadTestsFromTestCase(LoginTest2)
login_SocialMediaTest= unittest.TestLoader().loadTestsFromTestCase(LoginTests)
login_SignupMembership = unittest.TestLoader().loadTestsFromTestCase(LoginTestsi)
login_LoginWithSignupTest= unittest.TestLoader().loadTestsFromTestCase(LoginTest1)

test_suite = unittest.TestSuite([login_email, login_map,  login_MyAppointments, login_Logout, login_Register, login_BookAppoinment, login_BookHealthCheck, login_ChangePass, login_EditProfile, login_ForgetUserName, login_LinkServeContact, login_LoginWithForgetPassword, login_SocialMediaTest, login_SignupMembership, login_LoginWithSignupTest])
# test_suite = unittest.TestSuite([login_email, login_facebook])
# unittest.TextTestRunner().run(test_suite)