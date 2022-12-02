import json


data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

# when writting to disk like above we use dump and below we use dumps

json_string = json.dumps(data)
print(json_string)


# encoding and decoding afterwards it might not be same stuff

blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
print(encoded_hand)
decoded_hand = json.loads(encoded_hand)
print(decoded_hand)
blackjack_hand == decoded_hand
print(type(blackjack_hand))
print(type(decoded_hand))
print(blackjack_hand == tuple(decoded_hand))

json_string1 = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string1)