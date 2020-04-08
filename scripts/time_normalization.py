from word2number import w2n    

def get_trivial_floats(self, s):
    try:
        n = float(s)
        return n
    except:
        return None

# Extracting the surface numerical value amoung tokens
def get_surface_floats(self, tokens):
    if tokens[-1] in ["a", "an"]:
        return 1.0
    if tokens[-1] == "several":
        return 4.0
    if tokens[-1] == "many":
        return 10.0
    if tokens[-1] == "some":
        return 3.0
    if tokens[-1] == "few":
        return 3.0
    if tokens[-1] == "tens" or " ".join(tokens[-2:]) == "tens of":
        return 10.0
    if tokens[-1] == "hundreds" or " ".join(tokens[-2:]) == "hundreds of":
        return 100.0
    if tokens[-1] == "thousands" or " ".join(tokens[-2:]) == "thousands of":
        return 1000.0
    if " ".join(tokens[-2:]) in ["a few", "a couple"]:
        return 3.0
    if " ".join(tokens[-3:]) == "a couple of":
        return 2.0
    return None

# Extracting comprehensive numerical values
def quantity(self, tokens):
    try:
        if self.get_trivial_floats(tokens[-1]) is not None:
            return self.get_trivial_floats(tokens[-1])
        if self.get_surface_floats(tokens) is not None:
            return self.get_surface_floats(tokens)
        string_comb = tokens[-1]
        cur = w2n.word_to_num(string_comb)
        for i in range(-2, max(-(len(tokens)) - 1, -6), -1):
            status = True
            try:
                _ = w2n.word_to_num(tokens[i])
            except:
                status = False
            if tokens[i] in ["-", "and"] or status:
                if tokens[i] != "-":
                    string_comb = tokens[i] + " " + string_comb
                update = w2n.word_to_num(string_comb)
                if update is not None:
                    cur = update
            else:
                break
        if cur is not None:
            return float(cur)
    except Exception as e:
        return None   

# Normalizing a temporal expression to the nearest unit
def normalize_timex(self, expression):

    u = expression.split()[1]
    v_input = float(expression.split()[0])

    if u in ["instantaneous", "forever"]:
        return u, str(1)

    convert_map = {
        "seconds": 1.0,
        "minutes": 60.0,
        "hours": 60.0 * 60.0,
        "days": 24.0 * 60.0 * 60.0,
        "weeks": 7.0 * 24.0 * 60.0 * 60.0,
        "months": 30.0 * 24.0 * 60.0 * 60.0,
        "years": 365.0 * 24.0 * 60.0 * 60.0,
        "decades": 10.0 * 365.0 * 24.0 * 60.0 * 60.0,
        "centuries": 100.0 * 365.0 * 24.0 * 60.0 * 60.0,
    }
    seconds = convert_map[u] * float(v_input)
    prev_unit = "seconds"
    for i, v in enumerate(convert_map):
        if seconds / convert_map[v] < 0.5:
            break
        prev_unit = v
    if prev_unit == "seconds" and seconds > 60.0:
        prev_unit = "centuries"

    return prev_unit
