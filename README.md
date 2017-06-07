# Making PDF Copies of DRM-protected E-Books
These are actually examples for PyMuPDF scripts - which I do not want to include in the official repository.

There exist cool tools to decrypt DRM-protected material, like https://github.com/apprenticeharper/DeDRM_tools.

Just in case they do not help you, here is an alternative.
It works as follows:

1. Open your e-book application with the book you want to backup
2. Start one of the scripts provided here
3. Choose whether you want to actually start the backup process, or just display an example page image
4. Use the test page display to adjust the screen region such that the displayed book page is properl covered.
5. Once the backup process is started, it will automatically flip through the book and make an image of every page. Each image will become a new PDF page.
6. If end of book is encountered (recognized as two pages in a row which are equal down to the pixel level), a new PDF ``ebook.pdf`` will be saved.

The new PDF will be compressed, but expect something like 10 MB per each 100 pages. Just as if you would create a PDF by scanning material.

After you are done, you may consider using an OCR tool to further process the new PDF content ...