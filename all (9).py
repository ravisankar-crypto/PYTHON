student={
    "name":"ravi",
    "marks":{
        "phyton": 14,
        "dsa": 14,
        "math": 16
    }
}
print(student["marks"]["math"])
print(student)
print(len(student))
print(len(list(student)))
print(list(student.keys()))
print(list(student.values()))
print(student.items())
print(student.get("name"))
student.update({"coa":13})
new_dict = {"name": "sankar","age": 19}
student.update(new_dict)
print(student)

