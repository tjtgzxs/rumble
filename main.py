from upload import upload
import Constant
import configparser
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read(Constant.BASE_DIR+"conf.ini")
    video_dir=config.get("DEFAULT","video_path")
    upload=upload(config.getboolean("WEBDRIVE","headless"))
    result=upload.process(config.get("DEFAULT","user_name"),config.get("DEFAULT",'password'),Constant.BASE_DIR+"1.mp4")
    print(result)
    upload.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
