countries = input().split(", ")
capitals = input().split(", ")

[print(f"{countries} -> {capitals}") for (countries, capitals) in zip(countries, capitals)]