from firebase import firebase
firebase = firebase.FirebaseApplication('https://tufhjftf-default-rtdb.firebaseio.com/' , None)
Result = firebase.delete('https://tufhjftf-default-rtdb.firebaseio.com/','Vishnu' )
print('Record Deleted')