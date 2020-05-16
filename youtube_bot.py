from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import pyautogui
from contact import email, password


class YouTubeBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def log_on_and_like(self):
        # Log into your Gmail account first
        # Go to Gmail
        self.driver.get(
            'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        sleep(3)
        # Enter email
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(
            email + Keys.RETURN)
        sleep(2)
        # Enter password
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(
            password + Keys.RETURN)
        sleep(4)

        # Log onto Video
        self.driver.get('https://www.youtube.com/user/tseries/videos')

        # I must first open inspect element panel in order to 'like' the vid because youtube hid the xpath
        sleep(5)
        keyboard = Controller()
        keyboard.press(Key.ctrl_l)
        pyautogui.click(500, 200)
        i = 0
        while i < 6:
            keyboard.press(Key.down)
            keyboard.release(Key.down)
            i += 1
        keyboard.press(Key.enter)
        sleep(3)

        # Goes to playlist of all the videos
        self.driver.find_element_by_xpath(
            '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[1]/div[2]/ytd-channel-sub-menu-renderer/div[1]/div/ytd-button-renderer/a/paper-button/yt-formatted-string').click()
        sleep(4)
        # Likes the first video
        self.driver.find_element_by_xpath(
            '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button/button/yt-icon').click()

        videos = self.driver.find_elements_by_id('playlist-items')
        for i in range(1, len(videos)):
            current = videos[i]
            current.click()
            sleep(3)
            self.driver.find_element_by_xpath(
                '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button/button/yt-icon').click()


bot = YouTubeBot()
bot.log_on_and_like()

