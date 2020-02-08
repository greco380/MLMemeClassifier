#!/usr/bin/env python3
import urllib
from urllib import request
# import urllib.request

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
        print(html.read().decode('utf-8'))

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
