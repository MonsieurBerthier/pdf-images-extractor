<p align="center">
  <img src="https://img.shields.io/badge/Version-v1.0-blue.svg" />
  <img src="https://img.shields.io/badge/Python-3.11-blue.svg" />
  <img src="https://img.shields.io/badge/License-GNU%20GPL%20v3-blue.svg" />
</p>
<br>

<p align="center">
  <img src="image.svg" />
</p>


Introduction
============

`pdf-images-extractor` is a very easy to use images extractor for PDF files.

It extracts all images from one or several PDF files and saves them as 
separate image files.


Example
=======

In the following example we will extract images from two PDF files `test1.pdf` and `test2.pdf`: 

```bash
berthier@cogip:~$ ./pdfimex.py ~/Downloads/test1.pdf ~/Downloads/test2.pdf
````

The folder `test1-images` which contains all extracted images from `test1.pdf` has been created in the same
folder as `test1.pdf`:

```bash
berthier@cogip:~$ ll ~/Downloads/test1-images/
total 272
drwxrwxr-x 2 berthier berthier   4096 déc.  21 23:30 ./
drwxr-xr-x 4 berthier berthier   4096 déc.  21 23:30 ../
-rw-rw-r-- 1 berthier berthier 163255 déc.  21 23:30 image_1.jpg
-rw-rw-r-- 1 berthier berthier 105597 déc.  21 23:30 image_2.jpg
````

Same goes for `test2.pdf`:

```bash
berthier@cogip:~$ ll ~/Downloads/test2-images/
total 272
drwxrwxr-x 2 berthier berthier   4096 déc.  21 23:30 ./
drwxr-xr-x 4 berthier berthier   4096 déc.  21 23:30 ../
-rw-rw-r-- 1 berthier berthier 163255 déc.  21 23:30 image_1.jpg
-rw-rw-r-- 1 berthier berthier 105597 déc.  21 23:30 image_2.jpg
````


Dependencies
============

The following dependencies must be satisfied:

```bash
pip install Pillow
pip install PyPDF2
````
