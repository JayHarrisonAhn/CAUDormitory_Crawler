from extract import Notice
import extract
import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('PrivateKey.json')
f = open('DBURL', 'r')
firebase_admin.initialize_app(cred, {
    'databaseURL': f.read(),
    'databaseAuthVariableOverride': {
        'uid': 'crawler'
    }
})
root = db.reference()
notice = Notice()

pushNotices=[]
pushNoticeTitles=[]
snapshot = root.child('Seoul_Bluemir/Notices').get()
for i in range(0,len(notice.IDNumbers)):
    isExisted = 0
    for key in snapshot:
        if key==notice.IDNumbers[i] :
            isExisted = 1
    if isExisted==0:
        pushNotices.append(notice.IDNumbers[i])
        pushNoticeTitles.append(notice.Titles[i])
        print(notice.IDNumbers[i])

snapshot = root.child('Users').get()

for key in snapshot:
    for i in range(0,len(pushNotices)):
        # See documentation on defining a message payload.
        message = firebase_admin.messaging.Message(
            notification=messaging.Notification(
                title=pushNoticeTitles[i],
                body='새로운 공지사항',
            ),
            token=key,
        )
        response = firebase_admin.messaging.send(message)
        print('Successfully sent message:', response)


for i in range(len(notice.IDNumbers)):
    root.child('Seoul_Bluemir/Notices').update({
        notice.IDNumbers[i] : {
            'Title' : (notice.Titles)[i],
            'Date' : (notice.Dates)[i]
        }
    })






