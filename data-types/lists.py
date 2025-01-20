names = ["Ann","Elvis","Mercy","Amos"]

for name in names:
    names.pop(1)
    print(name)


    #Tuples
    t2 = ('a',)
    t3 =tuple("python")
    print(t3)

    (0,1,2) < (0,3,4)

    txt = 'but soft what light in yonder windows breakes'
    words = txt.split()
    t = list()
    for word in words:
        t.append((len(word), word))
        t.sort(reverse=True)
        res = list()
        for length, word in t:
            res.append(word)
            print(res)

          #assigning tuples
            t2= ['have','fun', 'wanjiru']
            x, y ,z = t2
            print(t2)

            #Dictionaries
            #Store data in key value pairs
            age = '',
            occupation = '',
            mydict = {
                'name': 'Ann',
                'age': '25',
                'occupation': 'Software Engineer'

            }
            print(mydict)
            # Check length
            print(len(mydict))

            thisdict = {
               "brand": "Ford",
              "model": "Mustang",
               "year": 1964
            }
            # example of a dictionary comprehension

            mydict2 = dict(name = 'Wanjiru', age= 29, occupation= 'data analyst', country= 'kenya')
            # print(mydict2)
            z=mydict2.get('name')
            x =mydict2.values()
            print(mydict2.keys())
            print(z)
            print(x)

            

