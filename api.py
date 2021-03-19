import http.client, json
import mimetypes

class Api:
    def __init__(self, f="api_key/key.json") -> None:
        with open(f, "r") as f:
            api = json.loads(f.read())

        self.uid = api[0]['userId']
        self.key = api[0]["x-api-key"]
        self.tid = api[1]['teamId']


    def team_members(self):
        """Return the team members"""
        
        conn = http.client.HTTPSConnection("www.notexponential.com")
        payload = ''
        headers = {
            'x-api-key': self.key,
            'userId': self.uid
        }
        conn.request("GET", "/aip2pgaming/api/index.php?type=team&teamId={}".format(self.tid), payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def create_game(self, team2, size=3, target=3):
        conn = http.client.HTTPSConnection("www.notexponential.com")
        dataList = []
        boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
        dataList.append('--' + boundary)
        dataList.append('Content-Disposition: form-data; name=type;')

        dataList.append('Content-Type: {}'.format('multipart/form-data'))
        dataList.append('')

        dataList.append("game")
        dataList.append('--' + boundary)
        dataList.append('Content-Disposition: form-data; name=teamId1;')

        dataList.append('Content-Type: {}'.format('multipart/form-data'))
        dataList.append('')

        dataList.append(str(self.tid))
        dataList.append('--' + boundary)
        dataList.append('Content-Disposition: form-data; name=teamId2;')

        dataList.append('Content-Type: {}'.format('multipart/form-data'))
        dataList.append('')

        dataList.append(str(team2.tid))
        dataList.append('--' + boundary)
        dataList.append('Content-Disposition: form-data; name=gameType;')

        dataList.append('Content-Type: {}'.format('multipart/form-data'))
        dataList.append('')

        dataList.append("TTT")
        dataList.append('--' + boundary)
        dataList.append('Content-Disposition: form-data; name=boardSize;')

        dataList.append('Content-Type: {}'.format('multipart/form-data'))
        dataList.append('')

        dataList.append(str(size))
        dataList.append('--' + boundary)
        dataList.append('Content-Disposition: form-data; name=target;')

        dataList.append('Content-Type: {}'.format('multipart/form-data'))
        dataList.append('')

        dataList.append(str(target))
        dataList.append('--'+boundary+'--')
        dataList.append('')
        body = '\r\n'.join(dataList)
        payload = body
        headers = {
            'x-api-key': self.key,
            'userId': self.uid,
            'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
        }
        conn.request("POST", "/aip2pgaming/api/index.php", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def get_games(self):
        conn = http.client.HTTPSConnection("www.notexponential.com")
        payload = ''
        headers = {
        'x-api-key': self.key,
        'userId': self.uid
        }
        conn.request("GET", "/aip2pgaming/api/index.php?type=myGames", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8")) 

    def get_open_games(self):
        conn = http.client.HTTPSConnection("www.notexponential.com")
        payload = ''
        headers = {
            'x-api-key': self.key,
            'userId': self.uid
        }
        conn.request("GET", "/aip2pgaming/api/index.php?type=myOpenGames", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def make_move(self, gameId, move):
        conn = http.client.HTTPSConnection("www.notexponential.com")
        dataList = []
        boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
        dataList.append('--' + boundary)
        dataList.append('Content-Disposition: form-data; name=type;')

        dataList.append('Content-Type: {}'.format('multipart/form-data'))
        dataList.append('')

        dataList.append("move")
        dataList.append('--' + boundary)
        dataList.append('Content-Disposition: form-data; name=gameId;')

        dataList.append('Content-Type: {}'.format('multipart/form-data'))
        dataList.append('')

        dataList.append(gameId)
        dataList.append('--' + boundary)
        dataList.append('Content-Disposition: form-data; name=teamId;')

        dataList.append('Content-Type: {}'.format('multipart/form-data'))
        dataList.append('')

        dataList.append(self.tid)
        dataList.append('--' + boundary)
        dataList.append('Content-Disposition: form-data; name=move;')

        dataList.append('Content-Type: {}'.format('multipart/form-data'))
        dataList.append('')

        dataList.append("{},{}".format(move[0], move[1]))
        dataList.append('--'+boundary+'--')
        dataList.append('')
        body = '\r\n'.join(dataList)
        payload = body
        headers = {
        'x-api-key': self.key,
        'userId': self.uid,
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
        }
        conn.request("POST", "/aip2pgaming/api/index.php", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def get_moves(self, gameId, count):
        conn = http.client.HTTPSConnection("www.notexponential.com")
        boundary = ''
        payload = ''
        headers = {
        'x-api-key': self.key,
        'userId': self.uid,
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
        }
        conn.request("GET", "/aip2pgaming/api/index.php?type=moves&gameId={}&count={}".format(gameId, count), payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def get_board_string(self, gameId):
        conn = http.client.HTTPSConnection("www.notexponential.com")
        payload = ''
        headers = {
            'x-api-key': self.key,
            'userId': self.uid
        }
        conn.request("GET", "/aip2pgaming/api/index.php?type=boardString&gameId={}".format(gameId), payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def get_board_map(self, gameId):
        conn = http.client.HTTPSConnection("www.notexponential.com")
        payload = ''
        headers = {
            'x-api-key': self.key,
            'userId': self.uid
        }
        conn.request("GET", "/aip2pgaming/api/index.php?type=boardMap&gameId={}".format(gameId), payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
