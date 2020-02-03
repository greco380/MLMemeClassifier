import urllib.request
from bs4 import BeautifulSoup

url = 'https://knowyourmeme.com/memes/steven-crowders-change-my-mind-campus-sign/photos'

html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, 'html.parser')



def find_and_create_file():
    while True:
        i = 0
        f = 2
        # open file
        # read html to find image url
        # same image as cmm + i.jpg
        # save to file path: run/media/greco/000D-300F/OrganizedMemes/changeMyMind
        # close file
        f.close()
        i += 1

def main():
    find_and_create_file()


if __name__ == '__main__':
    main()
