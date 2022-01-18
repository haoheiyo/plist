
from flask import Flask, request, render_template, send_from_directory,Response
import urllib.parse

app = Flask(__name__)


@app.route('/plist', methods=['GET', 'POST'])
def plist():
    app_url=urllib.parse.unquote(request.args.get("app_url"))
    ts=app_url.split("/")[-1].split(".")[0]
    with open('static/ipa.plist','r') as f1:
        data=f1.read()
    with open('static/ipa_%s.plist'%ts,'w') as f2:
        f2.write(data.replace("app_url",app_url))
    return "https://360cec.b7.cm/static/ipa_%s.plist"%ts


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='localhost')

