import requests


def get_urls():
    print('Fetching the urls...')
    source_url = 'https://raw.githubusercontent.com/abdelhai/devblogs/master/dataset'
    return requests.get(source_url).text.split('\n')


def url_resp(url):
    """Receives a url returns True in case of 200 or 301 response codes"""
    res = None
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        res = requests.head(url, timeout=3, headers=headers)
    except:
        pass

    if res:
        code = res.status_code
        print('*' + str(code) + '*')
        if code == 200 or code == 301:

            print(url)
            print('#ok#')
            return True
        else:
            print('#bad#')


good_urls = [url for url in get_urls() if url_resp(url)]

with open('dataset', 'w') as dataset:
    for url in good_urls:
        dataset.write(url + '\n')
