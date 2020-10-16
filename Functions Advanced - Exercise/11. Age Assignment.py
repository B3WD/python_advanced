def age_assignment(*args, **ages):
    res_dict = {}
    names = [name for name in args]
    while names:
        for name in names:
            for key in ages.keys():
                if name[0] == key:
                    res_dict[name] = ages[key]
                    names.remove(name)
    return res_dict


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))