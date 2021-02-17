from firebase import firebase
import firebase_admin
from firebase_admin import credentials, firestore, db, _sseclient
# import RPi.GPIO as GPIO
# import time
json = '/Users/William/Desktop/Light/light-d7c0b-aef8206d738e.json'
cred = credentials.Certificate(json)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://light-d7c0b.firebaseio.com/'
})
ref = db.reference()
light1 = ref.child('light1')

def listener(message):
    return (message)

#print((_sseclient.Event().data('data')))
print(dir(light1))
light1.set(True) #Setting light1 to False
#print("--------------------------------------------------------------------------")
#print (light1.listen(listener("")))
