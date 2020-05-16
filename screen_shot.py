#This Class is not used, but I wanted to remember where the Google Auth Code lives on my screen

def screen_shot():
    # coordinate of message notification gotten by sending dozens of messages to phone
    # and then using a notepad to mark where the key is on my screen. Then, trial and error to
    # pinpoint where the code is on my screen to extract to text using OCR
    image = ImageGrab.grab(bbox=(1118, 75, 1185, 90)) # This line is the only important part of this class
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