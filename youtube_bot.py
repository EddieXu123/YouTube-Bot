from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import names
import random
import pytesseract
from PIL import Image
import pyscreenshot as ImageGrab
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from pynput.keyboard import Key, Controller
import pyautogui
from contact import email, password


def screen_shot():
    # coordinate of message notification gotten by sending dozens of messages to phone
    # and then using a notepad to mark where the key is on my screen. Then, trial and error to
    # pinpoint where the code is on my screen to extract to text using OCR
    image = ImageGrab.grab(bbox=(1118, 75, 1185, 90))
    image.save('code4.png')

    # Using our OCR
    im = Image.open('code4.png')
    text = pytesseract.image_to_string(im, lang="eng")
    print(text)

    write_file = open("output1.txt", "w")
    write_file.write(text)
    write_file.close()

    # Extracting the code from the screen shot
    screen = open("output1.txt", "r")
    output = screen.readline()
    code = output[2:8]
    return code

class YouTubeBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def log_on(self):
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
        self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[1]/div[2]/ytd-channel-sub-menu-renderer/div[1]/div/ytd-button-renderer/a/paper-button/yt-formatted-string').click()
        sleep(4)
        # Likes the first video
        self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button/button/yt-icon').click()

        videos = self.driver.find_elements_by_id('playlist-items')
        for i in range(1, len(videos)):
            current = videos[i]
            current.click()
            sleep(3)
            self.driver.find_element_by_xpath(
                '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button/button/yt-icon').click()


"""
    def sign_in(self):
        keyboard = Controller()
        #Select Like, which will bring you to log in
        self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button/button').click()
        #Log in
        self.driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/iron-dropdown/div/ytd-modal-with-title-and-button-renderer/div/ytd-button-renderer/a/paper-button/yt-formatted-string').click()
        # Create account
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/span/span').click()
        # For myself
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/span[1]/div[2]/div').click()
        sleep(2)
        first = names.get_first_name()
        last = names.get_last_name()
        email = first + last + str(random.randint(1000, 100000))
        # Create new Gmail address instead
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[2]/button').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/input').send_keys(email)
        # Random Enter first,last name and password
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/input').send_keys(first)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/input').send_keys(last)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/div/div[1]/input').send_keys("genericpassword")
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/div/div[1]/div/div[1]/input').send_keys("genericpassword" + Keys.RETURN)
        sleep(4)
        # enter phone number
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[2]/div[1]/div/div[1]/input').send_keys(phone_num)
        #keyboard.type(phone_num)
        keyboard.press(Key.enter)
        sleep(5)
        # screenshot g-code and log in
        self.driver.find_element_by_xpath('').send_keys(screen_shot())
"""
bot = YouTubeBot()
bot.log_on()
#bot.sign_in()
