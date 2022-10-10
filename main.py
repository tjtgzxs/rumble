from upload import upload
import Constant
import configparser
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    upload=upload()
    result=upload.process("tjtgjohnson","1990lljxk",Constant.BASE_DIR+"1.mp4")
    print(result)
    upload.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
