import requests
import pprint
def get_info_by_ip(ip):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}')
        print(response.text)
    except request.exceptions.ConnectionError:
        pprint.pprint('[!]пизда вайфаю!')

def main():
    ip = input('айпи:')

    get_info_by_ip(ip = ip)

if __name__ == '__main__':
    main()
