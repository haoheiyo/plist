

from flask import Flask, request, render_template, send_from_directory
import urllib.parse

app = Flask(__name__)


@app.route('/plist', methods=['GET', 'POST'])
def plist():
    app_url=request.args.get("app_url")
    with open('templates/ipa.plist','r') as f1:
        data=f1.read()
    with open('templates/ipa_new.plist','w') as f2:
        f2.write(data.replace("app_url",app_url))
    return send_from_directory('templates','ipa_new.plist')


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='localhost')


