
from flask import Flask,request
import urllib.parse

app = Flask(__name__)


@app.route('/plist', methods=['GET', 'POST'])
def plist():
    app_url=request.args.get("app_url")
    plist_str = """

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>items</key>
<array>
<dict>
<key>assets</key>
<array>
<dict>
<key>kind</key>
<string>software-package</string>
<key>url</key>
<string>%s</string>
</dict>
</array>
<key>metadata</key>
<dict>
<key>bundle-identifier</key>
<string>com.cn.abctest</string>
<key>bundle-version</key>
<string>1.0</string>
<key>kind</key>
<string>software</string>
<key>安装包_二狗</key>
<string>abctest</string>
</dict>
</dict>
</array>
</dict>
</plist>  
""" % urllib.parse.unquote(app_url)
    return plist_str


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='localhost')

