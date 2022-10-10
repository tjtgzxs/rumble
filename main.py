from upload import upload
import Constant
import configparser
import os
import send
import filetype
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read(Constant.BASE_DIR+"conf.ini")
    video_dir=config.get("DEFAULT","video_path")
    file_res = os.listdir(video_dir)
    limit=config.getint('DEFAULT','limit')
    now=1
    upload = upload()
    upload.login(config.get("DEFAULT", "user_name"), config.get("DEFAULT", 'password'))
    for file in file_res:
        long_file=video_dir+str(file)
        if now>limit:
            send.main("今日已完成任务了")
            break
        type=filetype.guess(long_file).EXTENSION

        if not type in ['mp4','m4v','mkv','webm','mov','avi','wmv','mpg','flv']:
            continue

        result = upload.upload(long_file)

        # del upload
        if result!=-1:
            os.remove(long_file)
            send.main("今日已完成" + str(now) + "/" + str(limit))
            now+=1
        else:
            continue
    upload.close()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
