def exec_until_command(command):
    command_lines = []
    while True:
        input_ = input().split("-")
        if command in input_:
            return command_lines
        else:
            command_lines.append(input_)


heroes = input().split(", ")
inv = {hero:[0] for hero in heroes}

commands = exec_until_command("End")

for (hero, item, price) in commands:
    if item not in inv[hero]:
        inv[hero].append(item)
        inv[hero][0] += int(price)

for hero, items in inv.items():
    print(f"{hero} -> Items: {len(items) - 1}, Cost: {items[0]}")