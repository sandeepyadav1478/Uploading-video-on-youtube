import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

client_secret = 'client_secrets.json'
api_name = 'youtube'
api_version = 'V3'
scopes = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(client_secret,api_name,api_version,scopes)

#upload_date_time=datetime.datetime(2020,12,25,12,30,0).isoformat() + '.000Z'

request_body = {
	'snippet':{
		'categoryI':19,
		'title': 'Uploading_test',
		'description':'Description_test',
		'tags':['Travel','video_test','Travel Tips']	
	},
	'status': {
	'privacyStatus':'public',
	#'publishAt': upload_date_time,
	'selfDeclaredMadeForKids' : False,
	},
	'notifySubscribers':False
}

mediafile=MediaFileUpload('hello.mp4')

response_upload = service.videos().insert(
	part = 'snippet,status',
	body=request_body,
	media_body=mediafile
).execute()
print(response_upload['status'])

service.thumbnails().set(
	videoId = response_upload.get('id'),
 	media_body = MediaFileUpload('hello_th.jpg') 	
).execute()