from __future__ import print_function
from PIL import Image, ImageGrab
import fitz
import time, sys
import win32com.client
"""
@created: 2017-06-05 18:00:00

@author: (c) 2017 Jorj X. McKie

Create a readable PDF copy of any (potentially DRM protected) pageable content
-------------------------------------------------------------------------------

Dependencies:
-------------
PyMuPDF v1.11.0+, PIL, SendKeys, AutoIt (external tool, separately installed),
operating system Windows (because of AutoIt).
Python version 2 (or 3 once the 'raw_input' function is replaced).

License:
--------
GNU GPL V3+

Description
------------
Page through the display of an e-book and store each page as a full page image
in a new PDF. The page image is created using ImageGrab of PIL.

The PIL module ImageGrab curently is only available on Mac and Windows.
However, any other product capable of scraping defined screen areas
would suffice as well (pyscreenshot on Linux? Not tested).

We also need a way to automatically page down our e-book reader.
This version uses AutoIt to do this in an elegant way, which also works
independantly of the used Python version. An alternative version of this script
uses the Python module SendKey instead.

"""
aut = win32com.client.Dispatch("AutoItX3.Control")    # AutoIt COM interface
# This is the rectangle copied. To be adjusted until it fits ...!
bbox = (70, 100, 850, 1008)            # the screen area to grab
width = (bbox[2] - bbox[0])/2.         # determines PDF page width
height = (bbox[3] - bbox[1])/2.        # ... and page height

# If you need to test your bbox image, answer "y"
answer = raw_input("need test picture? y/n ")
if answer == "y":
    print("you have 5 seconds to activate the e-book window ...")
    time.sleep(5)
    print("grabbing picture now")
    img = ImageGrab.grab(bbox = bbox)
    img.show()
    raise SystemExit

print("you have 5 seconds to activate the e-book window ...")
time.sleep(5)    
print("starting process now")
print("Don't touch! The e-book window needs focus all the time!")

doc = fitz.open()                      # new empty PDF
old_samples = None                     # used to check end of e-book
i = 0
while 1:
    img = ImageGrab.grab(bbox = bbox)  # get the displayed e-book page
    samples = img.tobytes()            # copy for PyMuPDF
    if samples == old_samples:         # if no change: must be end of book
        print("end of book encountered ... finishing")
        break
    old_samples = samples              # store this page image
    pix = fitz.Pixmap(fitz.csRGB, img.size[0], img.size[1], samples, 0)
    doc.insertPage(-1, width = width, height = height)     # new PDF page
    page = doc[-1]                     # load it as a page object
    page.insertImage(page.rect, pixmap = pix)    # insert screen print as image
    aut.send("{PGDN}")                 # next page in e-book reader
    time.sleep(2)                      # allow for slow response time
    i += 1

# new PDF now contains page images as if scanned-in.
doc.save("ebook.pdf", deflate=True)     # save our PDF copy with compression
print(i, "pages saved.")
    
