#!/usr/bin/env python3
import urllib
from urllib import request
# import urllib.request
import re

from bs4 import BeautifulSoup

# import urllib.request
# req = urllib.request.Request(
#     url,
#     data=None,
#     headers={
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
#     }
# )
#
# f = urllib.request.urlopen(req)
# print(f.read().decode('utf-8'))


def read_write_image(meme_template, pages, path, file):
    # This should work with other urls, i only tested with one
    p = 1
    i = 0



    while p <= int(pages):

        req = urllib.request.Request(
            'https://imgflip.com/meme/' + meme_template + '?page=' + str(p),
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/79.0.3945.130 Safari/537.36 '
            }
        )

        # Download the entire page
        html = urllib.request.urlopen(req)
        all_html = html.read().decode('utf-8')
        array_of_url = []
        final_image_array = []
        working_image = 1
        # new_way = re.finditer(r'i.imgflip.com\/.*\.((jpg)|(png))', all_html)
        # new_way = [x.group() for x in re.finditer(r'i.imgflip.com\/[^jpg]*\.((jpg)|(png))', all_html)]
        new_different_regex = [x.group() for x in re.finditer(r'i\.imgflip\.com\/[0-9a-zA-Z]{3,6}\.(jpg|png)', all_html)]
        print(new_different_regex)
        print(len(new_different_regex))
        for i in new_different_regex:
            if i not in final_image_array:
                final_image_array.append(i)
        # remove duplicates
        print(final_image_array)
        print(len(final_image_array))




        # while working_image is not None:
        #
        #     working_image = re.search('i.imgflip.com\/.*\.((jpg)|(png))', all_html)
        #     img_link = str(working_image).split("'")
        #     if img_link[1] == ' alt=':
        #         rest_html = str(all_html)
        #         all_html = rest_html[1]
        #         final_section = img_link[0]
        #         final_section = final_section.split('"')
        #         real_final_link = final_section[1]
        #         array_of_url.append(real_final_link)
        #         working_image = rest_html
        #         print("The link that needs to be downloaded is:\n" + real_final_link)
        #     else:
        #         rest_html = str(all_html).split(img_link[1])
        #         all_html = rest_html[1]
        #
        # # OK: so this is the exact link that needs to be downloaded now I need
        # # to find this link for all of the images on this page
        # # then go until that link is None
        #         real_final_link = img_link[1]
        #         array_of_url.append(real_final_link)
        #         print("The link that needs to be downloaded is:\n" + real_final_link)
        # print(array_of_url)

        # Turn the page into a bs object
        soup = BeautifulSoup(html, 'html.parser')

        # Get _just_ the photo_gallery div
        id_path = soup.find(id='base-left')
        # the problem is that class already has an assigned function in python
        # path2 = soup.find(class_='base-unit clearfix')
        # path3 = soup.find(class="base-img-wrap-wrap")
        # path4 = soup.find(class="base-img-wrap")

        # Loop through all item divs in the photo_gallery div
        for image in id_path.findAllNext(src_='item'):

            # Within each item div, get the photo div
            photo = image.find(class_='base-img')
            # Within that photo div, get the img tag which has `class = ""`
            # There's probably some method to find an img tag
            img = photo.find(class_='')
            # Get the data-src value from the image tag - this contains a thumbnail link
            # for the image. To get the full size image, change 'masonry' to 'original'
            # There's probably a way to download images from URL to file with urllib
            real_photo_link = img.get('data-src')
            if real_photo_link is None:
                print('No Image\n-------------\n')
                pass
            else:
                real_photo_link = real_photo_link.replace('masonry', 'original')
                real_photo_link = urllib.request.urlopen(real_photo_link)
                print("image " + str(i) + ":")
                # print(real_photo_link)
                # save it to a new file...
                output = open(path+'/'+file+str(i)+'.jpg', 'wb')
                image_file = output.write(real_photo_link.read())
                print("--------DONE----------\n")
                i += 1
        p += 1


def main():
    # meme_template = input("Enter the meme template part of the url from knowyourmeme.com: ")
    # pages = input("Scroll to the bottom and input how many pages there are: ")
    # path = input("Enter the full file path to where you wan the images to be saved: ")
    # file = input("enter the name of what you want the base file to be called: ")
    read_write_image(meme_template='Spongebob-Ight-Imma-Head-Out', pages='96', path='/home/greco/Documents/Memev2/SpongebobImmaHeadOut', file='sbiho')


if __name__ == '__main__':
    main()
