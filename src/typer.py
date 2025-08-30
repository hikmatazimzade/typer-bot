from time import sleep
from random import uniform

from playwright.sync_api import sync_playwright

from src.logger import get_logger

logger = get_logger("src.typer")

WEBSITE_LINK: str = "https://typer.io/play"
CURRENT_WORD_CLASS: str = "Gameboard_current__GLVn7"


def get_current_word(page: sync_playwright) -> str:
    element = page.locator(f'[class*="{CURRENT_WORD_CLASS}"]')
    current_word = element.text_content()
    return current_word


def type(page: sync_playwright) -> None:
    current_word = get_current_word(page)
    logger.info(f"Current Word: {current_word}")

    page.keyboard.type(current_word)
    page.keyboard.press("Space")
    sleep(uniform(0.1, 0.2))


def run():
    with sync_playwright() as playwright:
        chromium = playwright.chromium
        browser = chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)

        page = context.new_page()
        page.goto(WEBSITE_LINK)

        while True:
            try:
                type(page)
            except Exception as error:
                logger.error(f"An error occured while typing: {error}")


if __name__ == "__main__":
    run()