import requests as req
import json
url = 'http://localhost:8000/fullchain/'
liver = {'uid': 'uidsaf',
		'livername': 'name',
		'production': 'production',
		'gender': 'gender'}
data = {
		'liver':str(liver),
		'title': 'title',
		'startdatetime': 'datetime',
		'stream_url' : 'url',
		'onair': True, #True=放送中,False=リマインド
		'audience': 122222
		}

#res = req.post(url, data)
res = req.get(url).json()
#res[0]['liver'] = json.load(res[0]['liver'])
#onedata = res[0]['liver']
#d = eval(onedata)
print(res)

