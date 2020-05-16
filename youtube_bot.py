from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import pyautogui
from contact import email, password


class YouTubeBot:
    def __init__(self):
        # Create the browser we will use
        self.driver = webdriver.Chrome()

    def log_on_and_like(self):
        """First, we must log into our Gmail account"""
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
        """CHANGE THIS URL TO THE VIDEOS PAGE OF YOUR DESIRED CHANNEL"""
        self.driver.get('https://www.youtube.com/user/tseries/videos')  #Replace tseries with name of your channel

        """I must first open the 'inspect element' panel in order to 'like' the vid because YouTube hid the name of the xpath"""
        sleep(5)
        keyboard = Controller()
        # Lines 39+40 act as a right click
        keyboard.press(Key.ctrl_l)
        pyautogui.click(500, 200)
        # After right clicking, the inspect element option is 7 options down
        i = 0
        while i < 6:
            keyboard.press(Key.down)
            keyboard.release(Key.down)
            i += 1
        keyboard.press(Key.enter)  #Open up insect element tab in order to like the video
        sleep(3)

        # Goes to playlist of all the videos
        self.driver.find_element_by_xpath(
            '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[1]/div[2]/ytd-channel-sub-menu-renderer/div[1]/div/ytd-button-renderer/a/paper-button/yt-formatted-string').click()
        sleep(4)
        # Likes the first video
        self.driver.find_element_by_xpath(
            '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button/button/yt-icon').click()

        # Put all of the videos in the playlist into an array
        videos = self.driver.find_elements_by_id('playlist-items')
        # For every video in your array (playlist)
        for i in range(1, len(videos)):
            # Select the video
            current = videos[i]
            current.click()
            sleep(3)
            # Like the video
            self.driver.find_element_by_xpath(
                '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button/button/yt-icon').click()


# Calling the functions to run the program
bot = YouTubeBot()
bot.log_on_and_like()

