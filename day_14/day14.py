# STEPS = 10 # for part 1
STEPS = 40
def forceIncrement(dic, key, value = 1):
    try:
        dic[key] += value
    except KeyError:
        dic[key] = value

if __name__ == '__main__':
    # we need to make this more efficient, so we track the pairs that exist and add based on the rules
    with open('input.in') as f:
        initial = f.readline()[: -1]
        f.readline()
        rules = {line.split(' -> ')[0] : line.split(' -> ')[1][:-1] for line in f}
    pair_counter = {}
    counter = {}
    for i, _ in enumerate(initial):
        if i < len(initial) - 1:
            forceIncrement(pair_counter, initial[i: i + 2])
    for value in initial:
        forceIncrement(counter, value)
    current_pair_counter = pair_counter
    current_counter = counter
    for i in range(STEPS):
        mutating_pair_counter = current_pair_counter.copy()
        mutating_counter = current_counter.copy()
        for pair, addition in rules.items():
            try:
                number_of_pairs = current_pair_counter[pair]
                forceIncrement(mutating_counter, addition, number_of_pairs)
                forceIncrement(mutating_pair_counter, pair, -number_of_pairs)
                forceIncrement(mutating_pair_counter, pair[0] + addition, number_of_pairs)
                forceIncrement(mutating_pair_counter, addition + pair[1], number_of_pairs)
            except KeyError:
                pass
        current_pair_counter = mutating_pair_counter
        current_counter = mutating_counter
    print(max(current_counter.values()) - min(current_counter.values()))
