"""
Access Property

Given a dictionary and a key name, return the value 
associated with that key.

Notes:
- The key will always exist in the dictionary for this basic challenge.
- The value can be of any type (string, integer, boolean, etc.).
"""

def get_property(obj: dict, key: str):
    return obj[key]

# Examples
print(get_property({"nombre": "Ana", "edad": 25}, "nombre")) # "Ana"
print(get_property({"activo": True}, "activo"))              # True