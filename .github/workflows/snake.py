import datetime
import os
import requests

def run():
    url = f'https://github.com/{os.environ["GITHUB_REPOSITORY"]}/graphs/contributors?to={datetime.datetime.now().isoformat()}'
    response = requests.get(url)
    print(response.status_code)

if __name__ == '__main__':
    run()
