from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def visit(self, url: str):
        with allure.step(f"Открытие страницы {url}"):
            self.driver.get(url)

    def check_current_url(self, url: str) -> bool:
        with allure.step(f"Проверка, что текущий url равен {url}"):
            assert self.driver.current_url == url

    def get_locator(self, locator: tuple, nth: int = 0,):
        self.wait_element_will_visible(locator=locator, timeout=5)
        with allure.step(f"Генерация WebElement по локатору: {locator} с индексом={nth}"):
            return self.driver.find_elements(*locator)[nth]
    
    def click(self, locator: tuple, nth: int = 0):
        element = self.get_locator(locator=locator, nth=nth)
        with allure.step(f"Клик по элементу с локатором {locator} с индексом={nth}"):
            element.click()

    def check_visible(self, locator: str):
        element = self.get_locator(locator=locator)
        with allure.step(f"Проверка, что элемент с локатором: {locator} виден на странице"):
            assert element.is_displayed()

    def check_not_visible(self, locator: str):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(locator)
            )
            with allure.step(f"Элемент с локатором: {locator} не виден на странице"):
                return True
        except TimeoutException:
            with allure.step(f"Ошибка: элемент с локатором: {locator} все еще виден"):
                return False

    def check_have_text(self, locator: str, text: str, nth: int = 0):
        element = self.get_locator(locator=locator, nth=nth)     
        with allure.step(f"Проверка, что элемент с локатором: {locator} с индексом={nth} имеет текст={text}"):
            assert element.text == text

    def wait_element_will_visible(self, locator: tuple, timeout: int):
        with allure.step(f"Ожидание {timeout} секунд пока элемент с локатором {locator} станет видимым"):
            WebDriverWait(self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))
    
    def wait_for_text_to_be_present_in_element(self, locator: tuple, timeout: int, text):
        with allure.step(f"Ожидание {timeout} секунд пока элемент с локатором {locator} получит текст"):
            WebDriverWait(self.driver, timeout=timeout).until(EC.text_to_be_present_in_element(locator, text))

    def wait_element_will_clickable(self, locator: tuple, timeout: int):
        with allure.step(f"Ожидание {timeout} секунд пока элемент с локатором {locator} станет кликабельным"):
            WebDriverWait(self.driver, timeout=timeout).until(EC.element_to_be_clickable(locator))


    def drag_and_drop_on_element(self, locator_one, locator_two):
        draggable = self.get_locator(locator_one)
        droppable = self.get_locator(locator_two)
        with allure.step(f"Перетащить элемент {locator_one} на элемент {locator_two}"):
            js_script = """
            function dragAndDrop(dragElement, dropElement) {
                // Создаем DataTransfer объект для передачи данных
                var dataTransfer = new DataTransfer();
                
                // Событие dragstart
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                dragElement.dispatchEvent(dragStartEvent);
                
                // Событие dragenter
                var dragEnterEvent = new DragEvent('dragenter', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                dropElement.dispatchEvent(dragEnterEvent);
                
                // Событие dragover (обязательно!)
                var dragOverEvent = new DragEvent('dragover', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                dropElement.dispatchEvent(dragOverEvent);
                
                // Событие drop
                var dropEvent = new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                dropElement.dispatchEvent(dropEvent);
                
                // Событие dragend
                var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                dragElement.dispatchEvent(dragEndEvent);
            }
            
            dragAndDrop(arguments[0], arguments[1]);
            """
        
            self.driver.execute_script(js_script, draggable, droppable)

    @allure.step('Получить текущий текст')
    def get_element_text(self, locator):
        text = self.get_locator(locator).text
        return text
    
    def fill(self, locator, text: str):
        with allure.step(f"Заполнение поля с локатором {locator} значением={text}"):
            element = self.get_locator(locator=locator)
            element.send_keys(text)

    def scroll_to_center(self, locator: str):
        with allure.step(f"Скролл к элементу с локатором: {locator} по центру"):
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", locator)

    def click_to(self, locator):
        button = self.get_locator(locator)
        actions = ActionChains(self.driver)
        with allure.step(f"Клик к элементу с локатором: {locator}"):
            actions.move_to_element(button).click().perform()