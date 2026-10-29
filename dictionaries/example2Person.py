# representing data: a person
person = {
    "name": "John",
    "age":45
}
print(person)
person["weight"] = 167.9
person["height"] = 6
print(person)
person["age"]+= 1
print(person)

person.pop("height")
person.pop("weight")
print(person)