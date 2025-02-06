import json

with open("C:/Users/eradi/Desktop/pp2/pp2-labs/lab04/sample-data.json", "r") as f:
    data = json.load(f)

print(f"\nInterface Status \n {"=" * 70}")
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<5}")
print("-" * 70)

for i in data["imdata"]:
    attributes = i["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "")
    
    print(f"{dn:<50} {descr:<20} {speed:<10} {mtu:<5}")
print('\n')