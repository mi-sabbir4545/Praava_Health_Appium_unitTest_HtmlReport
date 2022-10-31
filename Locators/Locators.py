from appium.webdriver.common.appiumby import AppiumBy


class LogIn:
    # signup
    signup_XPATH = (AppiumBy.ID, "com.praava.patientportal:id/signup_link")
    mobile_ID = (AppiumBy.ID, "com.praava.patientportal:id/mobile")
    username_ID = (AppiumBy.ID, "com.praava.patientportal:id/username")
    password_ID = (AppiumBy.ID, "com.praava.patientportal:id/password")
    repassword_ID = (AppiumBy.ID, "com.praava.patientportal:id/re_password")
    email_ID = (AppiumBy.ID, "com.praava.patientportal:id/emailId")
    login0_ID = (AppiumBy.ID, "com.praava.patientportal:id/login_link")

    # forget password
    forgetpass_ID = (AppiumBy.ID, "com.praava.patientportal:id/forgot_password_link")
    forgetusername_ID = (AppiumBy.ID, "com.praava.patientportal:id/username_f")
    login1_ID = (AppiumBy.ID, "com.praava.patientportal:id/fp_login_link1")

    # forget user name / mobile
    forgetusern_ID = (AppiumBy.ID, "com.praava.patientportal:id/ft_username")
    forgetusermob_ID = (AppiumBy.ID, "com.praava.patientportal:id/forgot_username_mob")
    login2_ID = (AppiumBy.ID, "com.praava.patientportal:id/fu_login")

    # LOGIN
    loginuser_ID = (AppiumBy.ID, "com.praava.patientportal:id/login_user")
    loginpass_ID = (AppiumBy.ID, "com.praava.patientportal:id/login_password")
    login_ID = (AppiumBy.ID, "com.praava.patientportal:id/login_btn")


class middleLeftBar:
    # Book an appointment
    book_ID = (AppiumBy.ID, "com.praava.patientportal:id/Buttonbookappointment")
    service_ID = (AppiumBy.ID, "com.praava.patientportal:id/dept_spinner")
    familyphysicans_XPATH = (AppiumBy.XPATH, "//android.widget.TextView[@text='Family Physicians']")
    liketosee_ID = (AppiumBy.ID, "com.praava.patientportal:id/doc_spinner")
    taslima_XPATH = (AppiumBy.XPATH, "//android.widget.TextView[@text='Dr. Taslima Akter']")
    backtopreviouspage7_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    backtopreviouspage8_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")

    # book a health check
    # Annual Membership plan
    bookhealth_ID = (AppiumBy.ID, "com.praava.patientportal:id/ButtonbookHealthCheck")
    annualplan_XPATH = (AppiumBy.XPATH, "//android.widget.TextView[@text='Annual Membership Plan']")
    viewdetils_ID = (AppiumBy.ID, "com.praava.patientportal:id/buttonDetails")
    ecg_XPATH = (AppiumBy.XPATH, "//android.widget.TextView[@text='ECG']")
    booked_ID = (AppiumBy.ID, "com.praava.patientportal:id/buttonBook")
    backtopreviouspage9_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")

    # health check
    healthcheck_XPATH = (AppiumBy.XPATH, "//android.widget.TextView[@text='health check']")
    diabetesviewdetails_XPATH = (AppiumBy.XPATH, "(//android.widget.Button[@text='view details'])[4]")
    booked1_XPATH = (AppiumBy.XPATH, "//android.widget.Button[@text='book']")
    backtopreviouspage10_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    backtopreviouspage11_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")

    # signup for a membership plan
    signupmembership_ID = (AppiumBy.ID, "com.praava.patientportal:id/Buttonmembership")
    signupmembershipok_ID = (AppiumBy.ID, "android:id/button1")
    backtopreviouspage12_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")

    # MAP
    map_ID = (AppiumBy.ID, "com.praava.patientportal:id/ButtonMap")
    mapallow_ID = (AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button")
    backtopreviouspage13_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")


class middleRightBar:
    # register
    register_XPATH = (AppiumBy.XPATH, "//android.widget.Button[@text='register']")
    reg_fstname_ID = (AppiumBy.ID, "com.praava.patientportal:id/firstName")
    reg_middlename_ID = (AppiumBy.ID, "com.praava.patientportal:id/middleName")
    reg_lastname_ID = (AppiumBy.ID, "com.praava.patientportal:id/lastName")

    dateofbirth_ID = (AppiumBy.ID, "com.praava.patientportal:id/dob")
    date_ok_ID = (AppiumBy.ID, "android:id/button1")
    email_ID = (AppiumBy.ID, "com.praava.patientportal:id/email")
    selectgender_ID = (AppiumBy.ID, "com.praava.patientportal:id/gender_spinner")
    gendercancel_ID = (AppiumBy.ID, "android:id/button2")
    nationality_ID = (AppiumBy.ID, "com.praava.patientportal:id/nationality")
    selectstatus_ID = (AppiumBy.ID, "com.praava.patientportal:id/marital_spinner")
    statuscancel_ID = (AppiumBy.ID, "android:id/button2")
    selectoccupation_ID = (AppiumBy.ID, "com.praava.patientportal:id/occupation_spinner")
    occupationcancel_ID = (AppiumBy.ID, "android:id/button2")

    phnnmbr_ID = (AppiumBy.ID, "com.praava.patientportal:id/phone")
    address_ID = (AppiumBy.ID, "com.praava.patientportal:id/address")
    city_ID = (AppiumBy.ID, "com.praava.patientportal:id/city")
    state_ID = (AppiumBy.ID, "com.praava.patientportal:id/state")
    country_ID = (AppiumBy.ID, "com.praava.patientportal:id/country")
    postalcode_ID = (AppiumBy.ID, "com.praava.patientportal:id/pinCode")
    emergncycontact_ID = (AppiumBy.ID, "com.praava.patientportal:id/relationship")
    selectrelation_ID = (AppiumBy.ID, "com.praava.patientportal:id/relation_spinner")
    relationcancel_ID = (AppiumBy.ID, "android:id/button2")
    emergncycontact1_ID = (AppiumBy.ID, "com.praava.patientportal:id/emrConNum")
    aboutus_ID = (AppiumBy.ID, "com.praava.patientportal:id/survey_spinner")
    aboutuscancel_ID = (AppiumBy.ID, "android:id/button2")
    radioclick1_ID = (AppiumBy.ID, "com.praava.patientportal:id/emailCheckBox")
    radioclick2_ID = (AppiumBy.ID, "com.praava.patientportal:id/promotionCheckBox")
    backtopreviouspage_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")

    # link your + your family's accounts
    linkfamilysaccount_ID = (AppiumBy.ID, "com.praava.patientportal:id/ButtonExcellence")
    linkfamilysaccountok_ID = (AppiumBy.ID, "android:id/button1")
    addprofile_ID = (AppiumBy.ID, "com.praava.patientportal:id/fab")
    pbhl_ID = (AppiumBy.ID, "com.praava.patientportal:id/et_mrn_num")
    ################driver.back()
    add_ID = (AppiumBy.ID, "com.praava.patientportal:id/lpReg_btn")
    cross_ID = (AppiumBy.ID, "com.praava.patientportal:id/fab")
    backtopreviouspage1_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")

    # how can we serve you better?
    serve_ID = (AppiumBy.ID, "com.praava.patientportal:id/ButtonFeedback")
    addmemberok_ID = (AppiumBy.ID, "android:id/button1")
    backtopreviouspage2_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")

    # contact us
    contactus_ID = (AppiumBy.ID, "com.praava.patientportal:id/ButtonEmergency")
    contactallow_ID = (AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button")
    backtopreviouspage3_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")


class leftTopBar:
    #profile pencil
    navigate0_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    pencil_ID = (AppiumBy.ID, "com.praava.patientportal:id/editProfile")
    pancilallow_ID = (AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button")
    pencil1_ID = (AppiumBy.ID, "com.praava.patientportal:id/profile_fab")
    pencil2_ID = (AppiumBy.ID, "com.praava.patientportal:id/fabeditpro")
    name_ID = (AppiumBy.ID, "com.praava.patientportal:id/et_fname")
    dateofb_ID = (AppiumBy.ID, "com.praava.patientportal:id/et_dob")
    dateofbok_ID = (AppiumBy.ID, "android:id/button1")
    # scrolling
    # changeyear_ID = (AppiumBy.ID, "android:id/date_picker_header_year")
    # selectyear_Xpath = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.DatePicker/android.widget.LinearLayout/android.widget.ScrollView/android.widget.ViewAnimator/android.widget.ListView/android.widget.TextView[3]")
    # ##may month tab
    # changemonth_ID = (AppiumBy.ID, "android:id/next")
    # changedate_Xpath = (AppiumBy.XPATH, "//android.view.View[@content-desc='24 May 1997']")
    # dateselected_ID = (AppiumBy.ID, "android:id/button1")

    male_ID = (AppiumBy.ID, "com.praava.patientportal:id/radioButtonMale")
    mail_ID = (AppiumBy.ID, "com.praava.patientportal:id/et_email")
    address_ID = (AppiumBy.ID, "com.praava.patientportal:id/et_address")
    phone_ID = (AppiumBy.ID, "com.praava.patientportal:id/et_phoneNum")
    cancel_ID = (AppiumBy.ID, "com.praava.patientportal:id/canceledit")
    changepass_ID = (AppiumBy.ID, "com.praava.patientportal:id/fabcngpwd")
    oldpass_ID = (AppiumBy.ID, "com.praava.patientportal:id/et_oldpwd")
    newpass_ID = (AppiumBy.ID, "com.praava.patientportal:id/et_newpwd")
    confirmpass_ID = (AppiumBy.ID, "com.praava.patientportal:id/et_confirmpwd")
    cancelpass_ID = (AppiumBy.ID, "com.praava.patientportal:id/cancelchngpwd")
    backtopreviouspage100_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    navigate_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")

    #My appointments
    myappointmentys_XPATH = (AppiumBy.XPATH, "//android.widget.CheckedTextView[@text='my appointments']")
    pastappoint_XPATH = (AppiumBy.XPATH,
                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.b[2]/android.widget.TextView")
    backtopreviouspage4_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    navigate1_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")

    faqs_XPATH = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.support.v7.widget.LinearLayoutCompat[7]/android.widget.CheckedTextView")
    backtopreviouspage5_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    navigate2_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")

    socialmedia_XPATH = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.support.v7.widget.LinearLayoutCompat[8]/android.widget.CheckedTextView")
    fb_XPATH = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.b[2]/android.widget.ImageView")
    backtopreviouspage6_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    # Logout = driver.find_element(AppiumBy.XPATH, "//android.widget.CheckedTextView[@text='logout']")
    # driver.execute_script("arguments[0].scrollIntoView()", Logout)

    navigate3_XPATH = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    logout_XPATH = (AppiumBy.XPATH, "//android.widget.CheckedTextView[@text='logout']")
