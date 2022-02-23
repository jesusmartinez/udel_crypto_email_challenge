import os

def get_mail_1():
    return read_mail('ch1')
def get_mail_2():
    return read_mail('ch2')
def get_mail_3():
    return read_mail('ch3')
def get_mail_4():
    return read_mail('ch4')
def get_mail_5():
    return read_mail('ch5')

def read_mail(file):
    __location__ = os.path.realpath(     os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, file), 'r') as f:
        txt = f.read()
    f.close()
    return txt
