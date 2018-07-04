students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

print "Student Names Listing - Part 1"
for i in students :
    print i["first_name"]," ",i["last_name"]


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'},
     {'first_name' : "Edward", 'last_name': "Solo Esq."}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print users['Students'][1]['first_name'],users['Students'][1]['last_name'], \
'eddie '
print

def StudentNames():
    print
    print "Students"
    for i in range( 0, len(users['Students'])):
        # print users['Students'][i]['first_name'],users['Students'][i]['last_name']
        fn = users['Students'][i]['first_name']
        ln = users['Students'][i]['last_name']
        name = fn+ ' '+ln
        size = len(fn) + len(ln)
        print i+1," - ",name,' - ',size

    print
    print "Instructors"
    for i in range( 0, len(users["Instructors"])):
        # print users['Students'][i]['first_name'],users['Students'][i]['last_name']
        fn = users['Instructors'][i]['first_name']
        ln = users['Instructors'][i]['last_name']
        name = fn+ ' '+ln
        size = len(fn) + len(ln)
        print i+1," - ",name,' - ',size


StudentNames()
