from playwright.sync_api import sync_playwright
from pages import AutomationExercisePage
from data import URL, EMAIL, PASSWORD


def test_login_logout_100_times():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        automation_page = AutomationExercisePage(page)

        for i in range(100):
            print(f"\n========== CICLO {i + 1} ==========")

            automation_page.open_homepage(URL)
            automation_page.go_to_login()

            automation_page.login(EMAIL, PASSWORD)

            if automation_page.is_logged_in():
                print("Login realizado com sucesso.")
            else:
                print("Erro no login.")
                break

            page.wait_for_timeout(1000)

            automation_page.logout()
            print("Logout realizado com sucesso.")

            page.wait_for_timeout(1000)

        browser.close()


if __name__ == "__main__":
    test_login_logout_100_times()
