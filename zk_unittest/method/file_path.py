import configparser

def Get_filepath(fi_ph):
    config = configparser.ConfigParser()
    filename = '../zk_unittest/config_file/file.ini'
    config.read(filename)
    u = config.get('fi',fi_ph)
    return u 

if __name__ == "__main__":
    url = Get_filepath('zhongduan')
    print(url)