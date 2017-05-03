from config import Configure


__author__ = "Andrew Gafiychuk"


if __name__ == '__main__':
    # Test Singleton also
    cfg2 = Configure(file="../config.cfg")
    print(cfg2._singleton_mark)

    cfg = Configure(file="../config.cfg")
    print(cfg._singleton_mark)
    
    print(cfg2 is cfg) # Must be a True
    
    cfg.show_config()

    config = cfg.getConfiguration()

    print("="*100)
    print("User: {0}".format(config["user"]))
    print("Passowrd: {0}".format(config["password"]))
    print("="*100)

    print("Host: {0}".format(cfg.get_host()))
    print("Port: {0}".format(cfg.get_port()))
