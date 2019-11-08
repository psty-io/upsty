from flask import Flask, request, redirect, make_response
from uuid import uuid4
import boto3, os, json


app = Flask(__name__)
with open('config.json', 'r+') as jsonf:
    conf = json.load(jsonf)
    app.config['AWS_ACCESS'] = conf['AWS_ACCESS_KEY']
    app.config['AWS_SECRET_KEY'] = conf['AWS_SECRET_KEY']
    app.config['S3_UPLOAD_DIR'] = conf['S3_UPLOAD_DIR'] 
    app.config['S3_BUCKET_NAME'] = conf['S3_BUCKET_NAME']
    app.config['BASE_URL'] = conf['BASE_URL']
    app.config['AWS_ENDPOINT_URL'] = conf['AWS_ENDPOINT_URL']

boto3s = boto3.session.Session()
client = boto3s.client('s3', region_name='sfo2', endpoint_url=app.config['AWS_ENDPOINT_URL'],
                       aws_access_key_id=app.config['AWS_ACCESS'], aws_secret_access_key=app.config['AWS_SECRET_KEY'])

@app.errorhandler(500)
def error(e):
    return '''
  __  ____       ____  __ 
 / / / / /  ____/ __ \\/ / 
/ /_/ / _ \\/___/ /_/ / _ \\
\\____/_//_/    \\____/_//_/
                          
Something went wrong!'''

def upload_file(filename):
    try:
        client.upload_file('tmp/{filename}'.format(filename=filename), app.config['S3_BUCKET_NAME'], '{}/{}'.format(app.config['S3_UPLOAD_DIR'], filename), ExtraArgs={'ACL':'public-read'})
        return True, 'Success'
    except Exception as e:
        return False, e
    
def gen_uid():
    uid_base = str(uuid4()).split('-')[0]
    return str(uid_base[0:3])

@app.route('/')
def redir():
    headers = {'content-type': 'text'}
    text = """
upsty - A psty.io Service For Uploading Files

Usage:
============================================================

curl --upload-file <filepath> https://up.psty.io/<filename>

============================================================

filepath = Path to file. ex: ./script.sh

filename = Name to download as. ex: ./test.sh

============================================================

Command Line:
============================================================

upsty <filepath> <filename>

============================================================
"""
    resp = make_response(text, 200, headers)
    return resp

@app.route('/<filename>', methods=['PUT'])
def upload(filename):
    file = request.data
    uid = gen_uid()
    with open('tmp/{uid}_{filename}'.format(uid=uid, filename=filename), 'wb') as sfile:
        sfile.write(file)
    result, msg = upload_file(str(uid + '_' + filename))
    os.remove('tmp/{uid}_{filename}'.format(uid=uid, filename=filename))
    if result:
        return '''
   ____                       
  / __/_ _____________ ___ ___
 _\\ \\/ // / __/ __/ -_|_-<(_-<
/___/\\_,_/\\__/\\__/\\__/___/___/
                              
File Available At: {base_url}/{uid}/{filename}'''.format(base_url=app.config['BASE_URL'], uid=uid, filename=filename)
    else:
        return '''
  __  ____       ____  __ 
 / / / / /  ____/ __ \\/ / 
/ /_/ / _ \\/___/ /_/ / _ \\
\\____/_//_/    \\____/_//_/
                          
Something went wrong when trying to upload your file!
Error: {msg}'''.format(msg=msg)
    
@app.route('/<uid>/<filename>', methods=['GET'])
def send(uid, filename):
    url = client.generate_presigned_url(ClientMethod="get_object",
                                        Params={'Bucket': 'mbcdn',
                                                'Key': 'psty/{uid}_{filename}'.format(uid=uid, filename=filename),
                                                'ResponseContentDisposition': 'attachment; filename = {filename}'.format(filename=filename)}, ExpiresIn=30)
    return redirect(url, 302)