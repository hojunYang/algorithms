def solution(bandage, health, attacks):

    full_time, heal_per_sec, bonus_heal = bandage
    max_health = health
    accumulated_time = 0

    for time in range(1, 1000000):
        if attacks:
            attack_time, attack_damage = attacks[0]
        else:
            return health
        
        if attack_time == time:
            attacks.pop(0)
            health -= attack_damage
            accumulated_time = 0
            if health <= 0:
              return -1
            continue

        
        accumulated_time += 1
        health = min(max_health, health + heal_per_sec)
        
        if accumulated_time == full_time:
            health = min(max_health, health + bonus_heal)
            accumulated_time = 0

    return health

    
def test_solution():
    # Test case 1
    print("Test case 1:", solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
    
    # Test case 2
    print("Test case 2:", solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
    
    # Test case 3
    print("Test case 3:", solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
    
    # Test case 4
    print("Test case 4:", solution([1, 1, 1], 5, [[1, 2], [3, 2]]))
    
    print("모든 테스트 케이스 실행이 완료되었습니다.")


if __name__ == "__main__":
    test_solution()