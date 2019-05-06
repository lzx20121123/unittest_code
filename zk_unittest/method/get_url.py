import configparser


def Get_ip(na,u_ip):
    config = configparser.ConfigParser()
    filename = '../zk_unittest/config_file/url.ini'
    config.read(filename)
    u = config.get(na,u_ip)
    return u 
def Get_url(ur):
    
    config = configparser.ConfigParser()
    filename = '../zk_unittest/config_file/url.ini'
    config.read(filename)

    u = config.get('url',ur)
    Url_IP = Get_ip('ip','url_ip')
    return  Url_IP+u



if __name__ == "__main__":
    a = Get_url('loginurl')
    print (a)