class RouterModule(object):
    @classmethod
    def set_ip_addr(self, ip_addr):
        text = "Configured %s IP address..." % ip_addr
        print "\033[91m%s\033[0m" % text

    @classmethod
    def add_route(self):
        text = "Add route ..."
        print "\033[92m%s\033[0m" % text

    @classmethod
    def enable_dhcp(self):
        text = "Enable DHCP ..."
        print "\033[93m%s\033[0m" % text

if __name__ == "__main__":
    RouterModule.set_ip_addr("192.168.1.1")
    RouterModule.add_route()
    RouterModule.enable_dhcp()
