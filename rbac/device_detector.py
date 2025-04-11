import json

def get_role(android_id):
    with open("roles.json") as file:
        role_map = json.load(file)
    return role_map.get(android_id, "guest")

if __name__ == "__main__":
    test_id = "bc3d21ef44d9"
    print(f"Role for {test_id}: {get_role(test_id)}")
