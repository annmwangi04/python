#dictionaries
patient = [174.80]
#height-> 174
#weight -.80

patient ={
    "height":174,
    "weight":80,
    "address":{
        "county": "Nairobi",
        "ward": "Starehe",
        "code": "00200",
    },
    "fruits": ["banana","Pine", "apple"]
}
print(patient["fruits"][1])
print(patient['height'])
print(patient.keys())
print(patient.values())
#returns tuples
print(patient.items())
#remove an entire key value pair like popping akey
print(patient.pop("height"))
#
#student =dict()
student ={}
print(student)
student["maths"] =90
student["phyc"] = 90
print(student)