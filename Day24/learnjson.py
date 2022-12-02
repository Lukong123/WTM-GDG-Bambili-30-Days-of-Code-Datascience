import json


def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

ex1 = json.dumps(9 + 5j, default=encode_complex)
print(ex1)

class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)

ex2 = json.dumps(2 + 5j, cls=ComplexEncoder)
print(ex2)
encoder = ComplexEncoder()
print(encoder.encode(3 + 6j))


#decoding

complex_json = json.dumps(4 + 17j, cls=ComplexEncoder)
print(json.loads(complex_json))


def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct

with open("complex_data.json") as complex_data:

    data = complex_data.read()
    z = json.loads(data, object_hook=decode_complex)

print(type(z))

with open("complex_data.json") as complex_data:
    data = complex_data.read()
    numbers = json.loads(data, object_hook=decode_complex)
print(numbers)

