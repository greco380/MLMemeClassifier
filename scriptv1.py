import urllib

from pip. vendor.distlib.compat import raw_input

u = raw_input(
    "Enter the image URL: ")  # http://behindwoods.com/tamil-actress/sneha/sneha-stills-photos-pictures-247.jpg
i = int(raw_input("how many image do you want download: "))
print("Donloading started")

while i > 0:
    i = i - 1
    URL = u + str(i) + ".jpg"
    IMAGE = URL.rsplit('/', 1)[1]
    urllib.urlretrieve(URL, IMAGE)
    print("Downloading image", i)

