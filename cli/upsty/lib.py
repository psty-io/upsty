import requests

def upload_file(filepath, filename):
    with open(filepath, 'rb') as file:
        res = requests.put('https://up.psty.io/{}'.format(filename), data=file)
        file.close()
        return res.content