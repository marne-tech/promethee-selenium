from selenium.webdriver.remote.webdriver import WebDriver

class Base:

    def __init__(self, driver: WebDriver, url: str = None):
        self.driver = driver
        # Import local pour éviter l'import circulaire (car ConsentModal hérite de Base)
        # On évite la récursion infinie : ConsentModal ne doit pas s'initialiser lui-même
        if self.__class__.__name__ != 'ConsentModal':
            try:
                # from .utils.consent import ConsentModal
                # self.consent_modal = ConsentModal(driver)
                pass
            except ImportError:
                pass
        
        if url:
             self.open_url(url)

    def open_url(self, url: str):
        self.driver.get(url)

    def get_title(self) -> str:
        return self.driver.title

    def refresh(self):
        self.driver.refresh()
