def get_repeating_DNA(sequence):
    lenght_substring = 10
    all_subsequences = {}
    res = []

    for i in range(len(sequence) - lenght_substring + 1):
        if sequence[i:i + 10] not in all_subsequences:
            all_subsequences[sequence[i:i + 10]] = 0
        all_subsequences[sequence[i:i + 10]] += 1

    for sequnce, count in all_subsequences.items():
        if count > 1:
            res.append(sequnce)

    return res


test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)