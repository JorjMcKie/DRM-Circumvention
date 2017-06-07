from __future__ import print_function
from PIL import Image, ImageGrab
import fitz
import time, sys
import SendKeys as sk
"""
@created: 2017-06-05 18:00:00

@author: (c) 2017 Jorj X. McKie

Create a readable PDF copy of any (potentially DRM protected) pageable content
-------------------------------------------------------------------------------

Dependencies:
-------------
PyMuPDF v1.11.0+, PIL, SendKeys

License:
--------
GNU GPL V3

Description
------------
Page through the display of an e-book and store each page as an image in a new PDF.
The page image is created using ImageGrab of PIL. Paging forward is achieved by
SendKeys.

The PIL module ImageGrab is only available on Mac and Windows. Any other product capable
of scraping defined screen ares would suffice as well (pyscreenshot on Linux? Not tested).

SendKeys is available on Windows with Python 2.7 only.
However, any product capable of sending a "PageDown" or a "next page" to your
E-Book reader would be okay, too. An elegant alternative on WIndows with many
more features is AutoIt, which can be invoked via Python's win32 COM interface,
independantly of the used Python version.

"""
# This is the rectangle copied. To be adjusted until it fits ...!
bbox = (100, 100, 850, 1000)           # the screen area to grab
width = (bbox[2] - bbox[0])/2.         # determines PDF page width
height = (bbox[3] - bbox[1])/2.        # ... and page height

# If you need to test, if your bbox is ok, answer "y"
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
old_samples = None                     # check if image did not change
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
    sk.SendKeys("{PGDN}")              # next page in e-book reader
    time.sleep(2)                      # allow for slow response time
    i += 1

# new PDF now contains page images as if scanned-in.
doc.save("ebook.pdf", deflate=True)     # save our PDF copy with compression
print(i, "pages saved.")
    
