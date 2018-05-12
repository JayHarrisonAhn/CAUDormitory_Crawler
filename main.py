from extract import Notice
import extract
import firebase_admin
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
for i in range(len(notice.IDNumbers)):
    root.child('Seoul_Bluemir/Notices').update({
        notice.IDNumbers[i] : {
            'Title' : (notice.Titles)[i],
            'Date' : (notice.Dates)[i]
        }
    })