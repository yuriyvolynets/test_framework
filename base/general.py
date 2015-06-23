class General(object):
    @classmethod
    def stub_1(self):
        text = "General stub 1"
        print "\033[94m%s\033[0m" % text

    @classmethod
    def stub_2(self):
        text = "General stub 2"
        print "\033[95m%s\033[0m" % text

if __name__ == "__main__":
    General.stub_1()
    General.stub_2()
