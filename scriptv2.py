# imported the requests library
import curl as curl
import requests

image_url = "https://i.kym-cdn.com/photos/images/newsfeed/001/717/430/c6c.jpg"

# URL of the image to be downloaded is defined as image_url 
r = requests.get(image_url)  # create HTTP response object 

# send a HTTP request to the server and save 
# the HTTP response in a response object called r 
with open("python_logo.png", 'wb') as f:
    # Saving received content as a png file in 
    # binary format 
    # curl - O "image_url"
    # write the contents of the response (r.content) 
    # to a new file in binary mode.
    with open(r'/home/greco/Documents/Memev2/kids.txt', 'w') as f:
        f.write(r.content)

