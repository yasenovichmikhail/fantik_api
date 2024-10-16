from selenium.webdriver.common.by import By


class BasePageLocators:
    PROFILE_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 CustomButton"
                                "_btnSignUp__1ijqK ButtonHeaderProfile_button__756EG']")
    HEADER_LOGO = (By.XPATH, "//a[@class='HeaderLogo_link__w6i5r']")
    HEADER = (By.XPATH, "//div[@class='HeaderTopWrapper_topWrapper__wcGqJ']")
    FOOTER = (By.XPATH, "//nav[@class='FooterNav_container__TNimz']")
    GET_FREE_VIEWS_PANEL = (By.XPATH, "//div[@class='HeaderBottomWrapper_bottomWrapper__w2dKr']")
    HOME_LINK_HEADER = (By.XPATH, "//div//header//ul//li[1]")
    PRICING_LINK_HEADER = (By.XPATH, "//div//header//ul//li[2]")
    FAQ_LINK_HEADER = (By.XPATH, "//div//header//ul//li[3]")
    CONTACT_US_LINK_HEADER = (By.XPATH, "//div//header//ul//li[4]")
    LEARN_LINK_HEADER = (By.XPATH, "//div//header//ul//li[5]")
    HOME_LINK_FOOTER = (By.XPATH, "//div//footer//ul//li[1]")
    PRICING_LINK_FOOTER = (By.XPATH, "//div//footer//ul//li[2]")
    FAQ_LINK_FOOTER = (By.XPATH, "//div//footer//ul//li[3]")
    CONTACT_US_LINK_FOOTER = (By.XPATH, "//div//footer//ul//li[4]")
    LEARN_LINK_FOOTER = (By.XPATH, "//div//footer//ul//li[5]")
    PRIVACY_POLICY_FOOTER_LINK = (By.XPATH, "//button[@class='ButtonTermsPrivacy_btn__12u2U"
                                     " ButtonTermsPrivacy_linkFooter__BtSNv'][1]")
    TERMS_CONDITIONS_LINK = (By.XPATH, "//button[@class='ButtonTermsPrivacy_btn__12u2U"
                                       " ButtonTermsPrivacy_linkFooter__BtSNv'][2]")
    EMAIL_ADDRESS_LINK = (By.XPATH, "//a[@class='ButtonTermsPrivacy_linkFooter__BtSNv'][1]")
    TELEGRAM_LINK = (By.XPATH, "//a[@class='ButtonTermsPrivacy_linkFooter__BtSNv'][2]")
    PRIVACY_POLICY_CONTAINER = (By.XPATH, "//div[@class='ModalBase_container__aKAn0 "
                                          "ModalBase_secondTerms_Policy__bi4Ks']")
    LEARN_CONTAINER = (By.XPATH, "//div[@class='ModalBase_container__aKAn0 "
                                 "ModalBase_colorBlack__FDws8 ModalBase_secondLearn__F77CZ']")


class LoginPageLocators:
    SIGNUP_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s"
                               " CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK']")
    SIGNUP_TAB = (By.XPATH, "//label[@class='AuthorizationTypeItem_label__DBPDq']")
    LOGIN_TAB = (By.XPATH, "//div[@class='AuthorizationTypeItem_item__2IwVY'][2]")
    GOOGLE_AUTH_BUTTON = (By.XPATH, "//button[@class='AuthorizationServices_btnLogin__txbzD "
                                    "AuthorizationServices_iconGoogle__4dy0a']")
    FACEBOOK_AUTH_BUTTON = (By.XPATH, "//button[@class='AuthorizationServices_btnLogin__txbzD "
                                      "AuthorizationServices_iconFacebook__0Fg5_']")
    INPUT_EMAIL = (By.ID, "authorizationEmail")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//button[@class='InputRoot_btnForgot__1AugM']")
    INPUT_PASSWORD = (By.ID, "authorizationPassword")
    SHOW_PASSWORD_ICON = (By.XPATH, "//div[@class='InputRoot_imgPassword__8Xy0k']")
    HIDE_PASSWORD_ICON = (By.XPATH, "//div[@class='InputRoot_imgPassword__8Xy0k InputRoot_imgPasswordVisible__xlKE6']")
    CREATE_MY_ACCOUNT_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorRed__g7yY3 "
                                          "CustomButton_typeAuth__m__ns']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s"
                              " CustomButton_colorAqua__TKZR6 CustomButton_typeAuth__m__ns']")
    CLOSE_LOGIN_PAGE_BUTTON = (By.XPATH, "//button[@class='ButtonClose_btn__rSXPy ButtonClose_btnDefault__3PgA1']")
    REQUIRED_FIELD_WARNING = (By.XPATH, "//span[contains(text(), 'Required')]")
    USER_IS_NOT_FOUND_WARNING = (By.XPATH, "//span[contains(text(), 'User with such email not found')]")
    CREATE_ACCOUNT_DISABLED_BUTTON = (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorRed__g7yY3 "
                                                "CustomButton_typeAuth__m__ns']")
    PRIVACY_POLICY_LINK = (By.XPATH, "//p[@class='AuthorizationDiscription_labelDiscription__EN1Eb']/span[1]")
    TERMS_OF_USE_LINK = (By.XPATH, "//p[@class='AuthorizationDiscription_labelDiscription__EN1Eb']/span[2]")
    PRIVACY_POLICY_HEADER = (By.XPATH, "//article[@class='LayoutTermPrivacy_containerText__g__ZW']//h4")
    TERMS_OF_USE_HEADER = (By.XPATH, "//article[@class='LayoutTermPrivacy_containerText__g__ZW']/h4")