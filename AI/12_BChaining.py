knowledge_base = {
    "rule1": {"if": ["A", "B"], "then": "C"},
    "rule2": {"if": ["D"], "then": "A"},
    "rule3": {"if": ["E"], "then": "A"},
    "rule4": {"if": ["F"], "then": "D"},
    "rule5": {"if": ["G"], "then": "B"},
}


def backward_chaining(goal, known_facts):
    if goal in known_facts:
        return True
    for rule, value in knowledge_base.items():
        if goal == value["then"]:
            for condition in value["if"]:
                if backward_chaining(condition, known_facts):
                    known_facts.append(goal)
            if all(cond in known_facts for cond in value["if"]):
                return True
    return False


if __name__ == "__main__":
    goal = "C"
    known_facts = ["G", "D", "E"]

    if backward_chaining(goal, known_facts):
        print(f"The Goal '{goal}' can be reached")
    else:
        print(f"The goal '{goal}' cannot be reached")
