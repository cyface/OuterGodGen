import yaml

with open("data/attributes.yaml", 'r') as f:
    data = yaml.load(f)
    print(data)
    print(data["Attributes"][0])
    print(data["Attributes"][0][0]["Type"])