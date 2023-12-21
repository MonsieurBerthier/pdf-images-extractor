#!/usr/bin/python3
# coding: utf-8

import os
import sys

from PIL import Image
from PyPDF2 import PdfReader


class PdfImageExctractor:

    def __init__(self, pdf_path):

        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"unable to find file \"{pdf_path}\"")

        self.images_count = 1
        self.path_pdf = pdf_path
        self.path_images = pdf_path.split(".")[0] + "-images"

        if not os.path.exists(self.path_images):
            os.mkdir(self.path_images)

        pdf_reader = PdfReader(self.path_pdf)
        pdf_page = pdf_reader.pages[0]
        x_objects = pdf_page["/Resources"]["/XObject"].get_object()

        for x_object in x_objects:

            if x_objects[x_object]["/Subtype"] == "/Image":

                size = (x_objects[x_object]["/Width"], x_objects[x_object]["/Height"])
                data = x_objects[x_object].get_data()

                if x_objects[x_object]["/ColorSpace"] == "/DeviceRGB":
                    mode = "RGB"
                else:
                    mode = "P"

                if x_objects[x_object]["/Filter"] == "/FlateDecode":
                    Image.frombytes(mode, size, data).save(self._get_image_path(extension="png"))
                elif x_objects[x_object]["/Filter"] == "/DCTDecode":
                    self._write_jpg(data=data, extension="jpg")
                elif x_objects[x_object]["/Filter"] == "/JPXDecode":
                    self._write_jpg(data=data, extension="jp2")

                self.images_count += 1

    def _get_image_path(self, extension):

        return os.path.join(self.path_images, f"image_{str(self.images_count)}.{extension}")

    def _write_jpg(self, data, extension):

        with open(self._get_image_path(extension=extension), "wb") as file:
            file.write(data)


if __name__ == "__main__":

    for pdf_file in sys.argv[1:]:
        PdfImageExctractor(pdf_path=pdf_file)
