import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()

def read_text():
    quotes = open("./Folder/curse.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(txt_data):
    connection = http.request('GET', "https://www.purgomalum.com/service/containsprofanity?text="+txt_data)
    output = connection.read()
    print(output)
    connection.close()


read_text()