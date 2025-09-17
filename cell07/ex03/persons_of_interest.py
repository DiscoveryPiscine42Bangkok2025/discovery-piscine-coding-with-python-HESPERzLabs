#!/usr/bin/env python3

def famous_births(scientists):
    sorted_scientists = sorted(scientists.items(), key=lambda x: int(x[1]["date_of_birth"]))

    for _, info in sorted_scientists:
        name = info["name"]
        year = info["date_of_birth"]
        print(f"{name} is a great scientist born in {year}.")

if __name__ == "__main__":
    women_scientists = {
        "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
        "cecilia": {"name": "Cecilia Payne", "date_of_birth": "1900"},
        "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
        "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
    }

    famous_births(women_scientists)
