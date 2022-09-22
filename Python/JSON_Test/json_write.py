import json

dictionary = {
    "name"      :   "greg",
    "rollno"    :   56,
    "gpa"       :   4.0,
    "phone"     :   "12345678"
}

json_object = json.dumps(dictionary, indent = 4)

with open ("data.json", "w") as outfile:
    outfile.write(json_object)