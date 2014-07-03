django-worksheet-creator
========================

My simple app for creating worksheets.

Prerequisites:
==============

sudo apt-get install imagemagick --fix-missing
easy_install pyPDF

#install PIL
sudo apt-get build-dep python-imaging
sudo ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/
sudo ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/
sudo ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/
pip install pillow


Extras:
===============================================
You need to make sure that you add the scopes for google drive to the google_login app

Ensure you change the settings for the media file so that users can create and change files.