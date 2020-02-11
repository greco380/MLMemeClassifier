from PIL import Image
import os
from datetime import datetime


def eighty_percent(dir_path):
    list_of_files = os.listdir(dir_path)
    number_files = len(list_of_files)
    test_set = number_files * 0.8  # eighty percent
    rounded = round(test_set, 0)
    num_of_files = int(rounded)
    return num_of_files


def rescale(find_path, test_save_path, validate_sava_path, eighty):
    i = 0
    for image_file_name in os.listdir(find_path):
        if i < eighty:
            now = datetime.now().strftime('%Y%m%d-%H%M%S-%f')
            im = Image.open(find_path + image_file_name)
            new_width = 150
            new_height = 150
            print("Test Resizing")
            im = im.resize((new_width, new_height), Image.ANTIALIAS)
            im.save(test_save_path + now + '.png')
            print("--------------------Done------------------------")
            i += 1
        else:
            now = datetime.now().strftime('%Y%m%d-%H%M%S-%f')
            im = Image.open(find_path + image_file_name)
            new_width = 150
            new_height = 150
            print("Validate Resizing")
            im = im.resize((new_width, new_height), Image.ANTIALIAS)
            im.save(validate_sava_path + now + '.png')
            print("--------------------Done------------------------")
            i += 1


def main():
    # Local file test
    eighty_of_data = eighty_percent("/home/greco/Documents/MemesScriptTest/Memes3.0/")
    rescale(find_path="/home/greco/Documents/MemesScriptTest/Memes3.0/",
            test_save_path="/home/greco/Documents/MemesScriptTest/Memes3.0T/",
            validate_sava_path="/home/greco/Documents/MemesScriptTest/Memes3.0V/",
            eighty=eighty_of_data)
    #########################################################################################
    # Distracted BF
    eighty_of_data = eighty_percent("/users/u27/greco/memes/distractedBoyfriend/")
    rescale(find_path="/users/u27/greco/memes/distractedBoyfriend/",
            test_save_path="/users/u27/greco/memes/AllData/Train/TrainDisBf/",
            validate_sava_path="/users/u27/greco/memes/AllData/Validate/ValDisBf/",
            eighty=eighty_of_data)
    # Spongebob
    eighty_of_data = eighty_percent("/users/u27/greco/memes/Spongebob/")
    rescale(find_path="/users/u27/greco/memes/Spongebob/",
            test_save_path="/users/u27/greco/memes/AllData/Train/TrainSponge/",
            validate_sava_path="/users/u27/greco/memes/AllData/Validate/ValSponge/",
            eighty=eighty_of_data)
    # Two Buttons
    eighty_of_data = eighty_percent("/users/u27/greco/memes/twoButtons/")
    rescale(find_path="/users/u27/greco/memes/twoButtons/",
            test_save_path="/users/u27/greco/memes/AllData/Train/TrainTwoBt/",
            validate_sava_path="/users/u27/greco/memes/AllData/Validate/ValTwoBT/",
            eighty=eighty_of_data)

    # Bad Luck Brian
    eighty_of_data = eighty_percent("/users/u27/greco/memes/badLuckBrian/")
    rescale(find_path="/users/u27/greco/memes/badLuckBrian/",
            test_save_path="/users/u27/greco/memes/AllData/Train/TrainBadLBri/",
            validate_sava_path="/users/u27/greco/memes/AllData/Validate/ValBadLBri/",
            eighty=eighty_of_data)
    # Hide the Pain Harold
    eighty_of_data = eighty_percent("/users/u27/greco/memes/hideThePainHarold/")
    rescale(find_path="/users/u27/greco/memes/hideThePainHarold/",
            test_save_path="/users/u27/greco/memes/AllData/Train/TrainHideTPain/",
            validate_sava_path="/users/u27/greco/memes/AllData/Validate/ValHideTPain/",
            eighty=eighty_of_data)




if __name__ == '__main__':
    main()
