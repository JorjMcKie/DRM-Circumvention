# Making PDF Copies of DRM-protected E-Books
These are actually examples for PyMuPDF scripts - which I do not want to include in that repository.

There exist cool tools to decrypt DRM-protected material, like https://github.com/apprenticeharper/DeDRM_tools.

Just in case they do not help you (or if you have concerns whether those are legal in your environment), here is an alternative, which makes screen copies of each page and stores them one by one as PDF pages. This technique does **not** break DRM protection - it rather is comparabale to photo-copying a traditional paper-based book. If you use this for your own purposes (backup, use on other devices, etc., but no making available to others) you should be safe in most countries (but do check this out yourself - this is not a legal advice!).

It works as follows:

1. Open your e-book application with the book you want to backup and go to the page from where the copy should start.
2. Start one of the scripts provided here - recommendation: `scan_autogui.py`
3. Choose whether you want to actually start the backup process, or to just display an example page.
4. Use the test page display to adjust the screen region such that the displayed book page is properly covered.
5. Once the backup process is started, it will automatically flip through the book, making an image of every page, and storing it as a new PDF page.
6. If end of book is encountered, a new PDF ``ebook.pdf`` will be saved in the script directory. End-of-book condition is recognized as two consecutive pages which are equal down to the pixel level. This test will fail of course, if e.g. there are two blank pages in a row. In such cases, restart the process at the following page again and join the partial PDF documents (e.g. with the PyMuPDF function ``insertPDF()``).

The new PDF will be compressed, but expect an order of magnitude of 10 MB per each 100 pages. Just as if you would creating a PDF by scanning some material.

# Dependencies
Apart from PyMuPDF (which does all the PDF work), you need components to

1. take an image of the selected screen area
2. send "page forward" to your e-book reader

For (1.) you can e.g. use ``Pillow.ImageGrab`` (available on MacOS and Windows). For (2.) you can use `SendKeys` (available on Windows Python 2 only).

I highly recommend `PyAutoGUI` (https://pypi.python.org/pypi/PyAutoGUI/0.9.36) which covers both of the above in the most elegant way. It works on any bitness of Windows, Mac and Linux, Python 2 and Python 3. I have tested it on Windows 32bit and 64bit for Python 2 and 3.
