insurance_plans = [
    {
        "name" : "UnitedHealth",
        "match" : 69,
        "reason" : "Becuase GT aur koi option nahi deta"
    },
    {
        "name" : "Kaiser",
        "match" : 100,
        "reason" : "Sasti hai aur tu gareeb hai"
    },
    {
        "name" : "Anthem",
        "match" : 20,
        "reason" : "There is an extremely valid reason. Trust."
    }
]


diseases = [
    {
        "name" : "malaria",
        "prone" : 0.3
    },
    {
        "name" : "HIV",
        "prone" : 1.0
    },
    {
        "name" : "covid 19",
        "prone" : 0.78
    }
]

def recieve_data(data):
    print(data)
    if data:
        name = data['name']
        age = data['age']
        loc = data['location']
        gender = data['gender']
        history = data['history']
        symptoms = data['symptoms']
        intensity = data['intensity']
    
    print(f"{name} is a {age} year old {gender}, currently living in {loc}. They experience {symptoms[0]}")