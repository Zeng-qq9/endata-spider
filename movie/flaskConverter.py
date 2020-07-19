from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/getPage')
def getPage():
    year = request.args.get('year')
    MethodName = request.args.get('MethodName')
    movieId = request.args.get('movieId')
    return sendReq(year, MethodName, movieId)


def sendReq(year, MethodName, movieId):
    url = "http://www.endata.com.cn/API/GetData.ashx"
    d = {'year': year, 'MethodName': MethodName, "movieId": movieId}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    r = requests.post(url, data=d, headers=headers)
    return r.text


if __name__ == '__main__':
    app.run("127.0.0.1", 2345)
