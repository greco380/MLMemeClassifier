#!/usr/bin/env python3
import urllib
from urllib import request
# import urllib.request
import re
from PIL import Image
import requests
from io import BytesIO

from bs4 import BeautifulSoup


def read_write_image(meme_template, pages, path, file):
    # This should work with other urls, i only tested with one
    p = 1
    i = 0
    l = 0
    image_link_pos_in_array = 0

    while p <= int(pages):

        req = urllib.request.Request(
            'https://imgflip.com/meme/' + meme_template + '?page=' + str(p),
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/79.0.3945.130 Safari/537.36 '
            }
        )
        print("\t\t"+ str(req) )

        # Download the entire page
        html = urllib.request.urlopen(req)
        all_html = html.read().decode('utf-8')
        final_image_array = []
        new_different_regex = [x.group() for x in re.finditer(r'i\.imgflip\.com\/[0-9a-zA-Z]{3,6}\.(jpg|png)', all_html)]
        # print(new_different_regex)
        # print(len(new_different_regex))
        # remove duplicates
        for i in new_different_regex:
            if i not in final_image_array:
                final_image_array.append(i)
        # print(final_image_array)
        # print(len(final_image_array))
        for image_link_pos_in_array in final_image_array:
            # download_link = final_image_array[image_link_pos_in_array]
            full_url = "http://" + image_link_pos_in_array

            req_end = urllib.request.Request(
                "http://" + image_link_pos_in_array,
                data=None,
                headers={
                    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 '
                }
            )

            # real_photo_download = urllib.request.urlopen("http://"+image_link_pos_in_array)
            print("image " + str(image_link_pos_in_array) + ":")
            # save it to a new file...

            response = requests.get(full_url)
            img = Image.open(BytesIO(response.content))

            img_file = img.save(path+"/"+file+str(l)+".jpeg", "JPEG")
            print("--------DONE----------\n")
            l += 1
        p += 1





def main():
    meme_template = input("Enter the meme template part of the url from imgflip.com: ")
    pages = input("Scroll to the bottom and input how many pages there are: ")
    path = input("Enter the full file path to where you wan the images to be saved: ")
    file = input("enter the name of what you want the base file to be called: ")
    read_write_image(meme_template, pages, path, file)


if __name__ == '__main__':
    main()
