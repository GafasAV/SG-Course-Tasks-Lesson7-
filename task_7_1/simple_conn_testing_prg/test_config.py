from config import Configure


__author__ = "Andrew Gafiychuk"


if __name__ == '__main__':
    cfg = Configure(cfg_file="../config.cfg")

    cfg.show_config()

    config = cfg.getConfiguration()

    print("="*100)
    print("User: {0}".format(config["user"]))
    print("Passowrd: {0}".format(config["password"]))
    print("="*100)

    print("Host: {0}".format(cfg.get_host()))
    print("Port: {0}".format(cfg.get_port()))