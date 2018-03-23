
def callMe1():
    print("My name is {file_name}".format(file_name=__name__))


def callMe11():
    print("I am being called from module1")
	
	
if(__name__ == '__main__'):
    print('I am standalone now')
