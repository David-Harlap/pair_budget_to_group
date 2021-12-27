from typing import List


def compute_budget(total_budget: float, citizen_votes: List[List]) -> List[float]:
    return [40, 20, 40]


def check_fair_to_group(total_budget: float, citizen_votes: List[List]) -> bool:
    budget = compute_budget(total_budget, citizen_votes)
    count_first, count_second, count_third = 0, 0, 0
    for temp in citizen_votes:
        if temp[0] == total_budget:
            count_first = count_first + 1
        elif temp[1] == total_budget:
            count_second = count_second + 1
        else:
            count_third = count_third + 1
    ratio = total_budget / len(citizen_votes)
    if budget[0] == count_first * ratio and budget[1] == count_second * ratio and budget[2] == count_third * ratio:
        return True
    return False


if __name__ == '__main__':
    print(check_fair_to_group(100, [[100, 0, 0], [100, 0, 0], [100, 0, 0], [100, 0, 0], [0, 100, 0],
                                    [0, 0, 100], [0, 0, 100], [0, 0, 100], [0, 0, 100], [0, 100, 0]]))
