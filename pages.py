from playwright.sync_api import Page


class AutomationExercisePage:

    def __init__(self, page: Page):
        self.page = page

    # ========== Locators ==========
    LOGIN_MENU = "a[href='/login']"
    EMAIL_INPUT = "input[data-qa='login-email']"
    PASSWORD_INPUT = "input[data-qa='login-password']"
    LOGIN_BUTTON = "button[data-qa='login-button']"
    LOGGED_USER_TEXT = "a:has-text('Logged in as')"
    LOGOUT_BUTTON = "a[href='/logout']"

    # ========== Actions ==========

    def open_homepage(self, url):
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    def go_to_login(self):
        self.page.click(self.LOGIN_MENU)
        self.page.wait_for_selector(self.EMAIL_INPUT)

    def login(self, email, password):
        self.page.fill(self.EMAIL_INPUT, email)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)
        self.page.wait_for_selector(self.LOGGED_USER_TEXT)

    def logout(self):
        self.page.click(self.LOGOUT_BUTTON)
        self.page.wait_for_selector(self.LOGIN_MENU)

    def is_logged_in(self):
        return self.page.locator(self.LOGGED_USER_TEXT).is_visible()
