from firebase import firebase
firebase = firebase.FirebaseApplication('https://tufhjftf-default-rtdb.firebaseio.com/',None)
data = {
'job': 'Artist',
'city': 'Paris',
'Name': 'Adam'
}
Result = firebase.post('https://tufhjftf-default-rtdb.firebaseio.com/', data)
print(Result)