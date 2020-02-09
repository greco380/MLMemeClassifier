from PIL import Image
import os
from datetime import datetime

# im = Image.open('/home/greco/Downloads/personalTestA.jpg')
# new_width  = 150
# new_height = 150
# im = im.resize((new_width, new_height), Image.ANTIALIAS)
# im.save('/home/greco/Downloads/personalTestAConvert.jpeg')


# Personal Test
for image_file_name in os.listdir('/home/greco/Documents/Memev2/PersonalTests/'):
        now = datetime.now().strftime('%Y%m%d-%H%M%S-%f')

        im = Image.open('/home/greco/Documents/Memev2/PersonalTests/'+image_file_name)
        new_width = 150
        new_height = 150
        im = im.resize((new_width, new_height), Image.ANTIALIAS)
        im.save('/home/greco/Documents/Memev2/PersonalTestsResize/' + now + '.jpeg')
