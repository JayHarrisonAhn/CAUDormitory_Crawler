from extract import Notice
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

notice = Notice()

# Fetch the service account key JSON file contents
cred = credentials.Certificate('caudormitory-42fb0-firebase-adminsdk-qt112-444c69cbfa.json')
# Initialize the app with a custom auth variable, limiting the server's access
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://caudormitory-42fb0.firebaseio.com/',
    'databaseAuthVariableOverride': {
        'uid': 'crawler'
    }
})
root = db.reference()
# Add a new user under /users.



for i in range(len(notice.IDNumbers)):
    root.child('Seoul_Bluemir/Notices').update({
        notice.IDNumbers[i] : {
            'Title' : (notice.Titles)[i],
            'Date' : (notice.Dates)[i]
        }
    })