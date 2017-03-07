class GameState:

    fen_strings = {
        "standard": "12/12/12/12/12/12/12/12,12,8,w,0,0,1 d,-4,T o/1101/1121/2222/2/f" #seperate pieces w/ comma
    }

    def __init__(self, arg1, init=False):
        self.board = []
        self.rules = {}
        self.pieces = {}
        if init:
            self.deserialize_fen_string(self.fen_strings[arg1])
        else:
            self.deserialize_fen_string(arg1)

    def deserialize_fen_string(self, fen_string):
        split_string = fen_string.split(' ')
        board = split_string[0]
        rules = split_string[1]
        pieces = split_string[2]
        neg_flag = False
        for char in rules:
            if char == "-":
                neg_flag = True
                continue

    def deserialize_rules(self, rule_string):
        rules = rule_string.split(',')
        capture_methods = {
            "d": "displacement",
            "c": "custodial",
            "dC": "delayed_custodial"
        }
        trapping = {
            "T": True,
            "t": False
        }
        self.rules["capture_method"] = capture_methods[rules[0]]
        self.rules["win_condition"] = int(rules[1])
        self.rules["trapping"] = trapping[rules[2]]

    def serialize_rules(self):
        rules = []
        capture_methods = {
            "displacement": "d",
            "custodial": "c",
            "delayed_custodial": "dC"
        }
        trapping = {
            True: "T",
            False: "t"
        }
        rules.append(capture_methods[self.rules["capture_method"]])
        rules.append(str(self.rules["win_condition"]))
        rules.append(trapping[self.rules["trapping"]])
        return ','.join(rules)
