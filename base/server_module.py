class ServerModule(object):
    @classmethod
    def get_connected_switches(self):
        text = "Server:\nGet switches"
        print "\033[94m%s\033[0m" % text

    @classmethod
    def get_value_from_db(self):
        text = "Get 'value' from DB"
        print "\033[95m%s\033[0m" % text

if __name__ == "__main__":
    ServerModule.get_hubs()
    ServerModule.get_fixtures()
