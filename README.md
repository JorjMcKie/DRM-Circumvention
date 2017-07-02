# Making PDF Copies of DRM-protected E-Books
These are actually examples for PyMuPDF scripts - which I do not want to include in that repository.

There exist cool tools to decrypt DRM-protected material, like https://github.com/apprenticeharper/DeDRM_tools.

Just in case they do not help you, here is an alternative.
It works as follows:

1. Open your e-book application with the book you want to backup and go to the page from where the copy should start.
2. Start one of the scripts provided here
3. Choose whether you want to actually start the backup process, or just display an example page.
4. Use the test page display to adjust the screen region such that the displayed book page is properly covered.
5. Once the backup process is started, it will automatically flip through the book, make an image of every page, and store it as a new PDF page.
6. If end of book is encountered (recognized as two pages in a row which are equal down to the pixel level), a new PDF ``ebook.pdf`` will be saved in the script directory.

The new PDF will be compressed, but expect something like 10 MB per each 100 pages. Just as if you would create a PDF by scanning some material.

After you are done, you may consider using an OCR tool to further process the new PDF content ...

# Dependencies
Apart from PyMuPDF (which does all the PDF work), you need components to

1. take an image of the selected screen area
2. send page forward to your e-book reader

For (1.) you can e.g. use ``Pillow.ImageGrab`` (available on MacOS and Windows). For (2.) you can use `SendKeys` (available on Windows Python 2 only).

I highly recommend `PyAutoGUI` (https://pypi.python.org/pypi/PyAutoGUI/0.9.36) which covers both of the above in the most elegant way. It works on any bitness of Windows, Mac and Linux, Python 2 and Python 3. I have tested it on Windows 32bit and 64bit for Python 2 and 3.
